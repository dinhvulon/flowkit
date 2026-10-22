// Rule 68 hook: nhắc chạy /fk-review-prompt sau khi viết/sửa prompt,
// và nhắc trước khi gửi batch sinh (GENERATE_* / REGENERATE_* / EDIT_* / UPSCALE_*).
// Chống lặp: mỗi mục tiêu (scene id / file) chỉ nhắc 1 lần cho tới khi chạy lint/review;
// chạy tools/lint_prompt.py hoặc /fk-review-prompt xoá danh sách đã nhắc.
import fs from 'node:fs';
import os from 'node:os';
import nodePath from 'node:path';

let raw = '';
process.stdin.on('data', (c) => (raw += c));
process.stdin.on('end', () => {
  let ev;
  try { ev = JSON.parse(raw); } catch { process.exit(0); }
  const event = ev.hook_event_name || '';
  const input = ev.tool_input || {};
  const cmd = String(input.command || '');
  const path = String(input.file_path || '').replace(/\\/g, '/');
  const body = String(input.content || '') + String(input.new_string || '');

  const stateFile = nodePath.join(os.tmpdir(), `fk-prompt-review-${ev.session_id || 'nosession'}.json`);
  let state = { reminded: [] };
  try { state = JSON.parse(fs.readFileSync(stateFile, 'utf8')); } catch {}
  const save = () => { try { fs.writeFileSync(stateFile, JSON.stringify(state)); } catch {} };

  // Review đã chạy -> mọi mục tiêu được nhắc lại nếu sau đó sửa tiếp.
  if (event === 'PostToolUse' && /lint_prompt\.py|fk-review-prompt/.test(cmd)) {
    state.reminded = [];
    save();
    process.exit(0);
  }

  const remindOnce = (key, msg) => {
    if (state.reminded.includes(key)) return;
    state.reminded.push(key);
    save();
    out(event, msg);
  };

  if (event === 'PreToolUse') {
    if (/api\/requests\/batch\b/.test(cmd) && !/batch-status/.test(cmd)
        && /(RE)?GENERATE_|EDIT_IMAGE|EDIT_CHARACTER_IMAGE|UPSCALE_/.test(cmd)) {
      const ids = (cmd.match(/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/g) || []).sort().join(',');
      remindOnce(`batch:${ids || cmd.slice(0, 200)}`,
        'Rule 29 + 68: request sinh tốn credit. Chỉ gửi khi user đã duyệt VÀ báo cáo /fk-review-prompt cho đúng prompt này đã được trình. Nếu chưa: dừng, chạy review, hỏi user.');
    }
    process.exit(0);
  }

  // PostToolUse
  const REVIEW = 'Rule 68: chạy /fk-review-prompt cho prompt vừa viết/sửa (lint_prompt.py 0 CRITICAL/HIGH -> bảng chủ thể theo giây -> checklist B prompt-lock.md -> vật lý & liên tục clip trước/sau -> chọn cỡ cảnh/góc máy). Gửi báo cáo tự đánh giá kèm khi hỏi user duyệt sinh.';
  const promptField = /video_prompt|image_prompt|storyboard_image_prompt/;
  if (/api\/scenes/.test(cmd) && /PATCH|POST|requests\.(patch|post)/i.test(cmd) && promptField.test(cmd)) {
    const sid = (cmd.match(/api\/scenes\/([0-9a-f-]{36})/) || [])[1];
    remindOnce(`scene:${sid || 'new'}`, REVIEW);
  } else if (/(^|\/)(prompts[^/]*\.json|[^/]*storyboard[^/]*\.(json|txt|md))$/i.test(path)
      || (/\.json$/i.test(path) && promptField.test(body))) {
    remindOnce(`file:${path.toLowerCase()}`, REVIEW);
  }
  process.exit(0);
});

function out(event, msg) {
  process.stdout.write(JSON.stringify({ hookSpecificOutput: { hookEventName: event, additionalContext: msg } }));
}
