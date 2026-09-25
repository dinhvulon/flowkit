import json
import os
import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8")

PROJECT_DIR = os.path.join("output", "time_travel_vlog_hanging_gardens_of_babylon_570_bc")
IMAGES_DIR = os.path.join(PROJECT_DIR, "images")
HTML_FILE = os.path.join(PROJECT_DIR, "review_images.html")

conn = sqlite3.connect("flow_agent.db")
c = conn.cursor()
c.execute("""
    SELECT display_order, id, horizontal_image_media_id, prompt, video_prompt, narrator_text, chain_type, character_names
    FROM scene
    WHERE video_id = '71909a60-29f7-460e-807c-ed48b8a12ad1'
    ORDER BY display_order ASC
""")
rows = c.fetchall()

scenes_data = []
beats = [
    ("Beat 1", "The Shock Arrival (Cú ngã xuyên không đến Cổng Ishtar)", "Act 1: Arrival & Orientation"),
    ("Beat 2", "Orientation & Disbelief (Chạm vào gạch men ngọc lưu ly xanh biếc)", "Act 1: Arrival & Orientation"),
    ("Beat 3", "First Contact (Né tránh xe thồ lương thực & đoàn lính Babylon)", "Act 1: Arrival & Orientation"),
    ("Beat 4", "Grand Reveal 1 (Tầm nhìn bao quát Vườn Treo vươn lên mây trời)", "Act 2: The Approach"),
    ("Beat 5", "Tasting Ancient Babylon (Thử quả chà là tươi và bánh mật ong)", "Act 2: The Approach"),
    ("Beat 6", "Sensory Immersion (Hương nhựa thông tuyết tùng & hương trầm)", "Act 2: The Approach"),
    ("Beat 7", "The Crowded Market (Len lỏi qua khu chợ ồn ào)", "Act 2: The Approach"),
    ("Beat 8", "Table Prop-up Dining (Gác máy ăn bánh dẹt nướng lò đất)", "Act 3: Deep Culture Dive"),
    ("Beat 9", "Curiosity Detour (Chạm trán người thợ khắc chữ hình nêm)", "Act 3: Deep Culture Dive"),
    ("Beat 10", "Ancient Tech (Đồng hồ nước Klepsydra nhỏ giọt)", "Act 3: Deep Culture Dive"),
    ("Beat 11", "Ascending the Base (Bước lên chân tháp đá Vườn Treo)", "Act 4: Entering the Wonders"),
    ("Beat 12", "Archimedes Screw (Bộ máy trục xoắn guồng nước sông Euphrates)", "Act 4: Entering the Wonders"),
    ("Beat 13", "The Shaded Archways (Lối đi vòm gạch mát lạnh rủ dây leo)", "Act 4: Entering the Wonders"),
    ("Beat 14", "Grand Reveal 2 (Tầng thượng uy nghi của Hoàng hậu Amytis)", "Act 4: Entering the Wonders"),
    ("Beat 15", "Suspense / Tension (Vệ binh hoàng gia tuần tra - Mia nấp)", "Act 5: Conflict & Discovery"),
    ("Beat 16", "The Escape (Luồn qua cửa hẹp rực rỡ hoa dạ yến thảo)", "Act 5: Conflict & Discovery"),
    ("Beat 17", "Safe Sanctuary (Góc vườn bí mật ngập tràn hoa hồng Media)", "Act 5: Conflict & Discovery"),
    ("Beat 18", "The Hydraulic Wonder (Cận cảnh hệ thống dẫn nước ngầm trong tường gạch)", "Act 6: Climax Wonder"),
    ("Beat 19", "Grand Reveal 3 (Tầng thượng tuyệt đỉnh nhìn ra dòng Euphrates)", "Act 6: Climax Wonder"),
    ("Beat 20", "Golden Hour Sunset (Hoàng hôn vàng rực nhuộm đỏ Lưỡng Hà)", "Act 6: Climax Wonder"),
    ("Beat 21", "Touching Euphrates Water (Chạm tay vào dòng nước trong vắt)", "Act 7: Decompression & Return"),
    ("Beat 22", "Decompression Ox-cart Ride (Ngồi trên xe bò nhìn lại kỳ quan)", "Act 7: Decompression & Return"),
    ("Beat 23", "Final Sign-off & Temporal Glitch (Tạm biệt khán giả & hiệu ứng glitch)", "Act 7: Decompression & Return")
]

for i, r in enumerate(rows):
    order, sid, mid, prompt, vprompt, narrator, chain_type, char_names = r
    idx = order + 1
    beat_info = beats[i] if i < len(beats) else (f"Beat {idx}", "Scene", "General")
    scenes_data.append({
        "index": idx,
        "scene_id": sid,
        "media_id": mid,
        "img_src": f"images/scene_{idx:02d}.jpg",
        "beat_code": beat_info[0],
        "beat_title": beat_info[1],
        "act": beat_info[2],
        "chain_type": chain_type,
        "prompt": prompt or "",
        "narrator": narrator or ""
    })

scenes_json = json.dumps(scenes_data, ensure_ascii=False)

html_template = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Review 23 Ảnh Khung Đầu — Vườn Treo Babylon (570 TCN)</title>
<style>
  :root {{
    --bg: #0f1015;
    --card-bg: #181924;
    --card-border: #28293d;
    --card-hover: #353754;
    --accent: #6366f1;
    --accent-glow: rgba(99, 102, 241, 0.25);
    --gold: #f59e0b;
    --green: #10b981;
    --red: #ef4444;
    --text: #f3f4f6;
    --text-muted: #9ca3af;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", Roboto, sans-serif; }}
  body {{ background: var(--bg); color: var(--text); padding-bottom: 80px; }}
  header {{
    position: sticky; top: 0; z-index: 100;
    background: rgba(15, 16, 21, 0.92);
    backdrop-filter: blur(16px);
    border-bottom: 1px solid var(--card-border);
    padding: 16px 32px;
    display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px;
  }}
  .brand {{ display: flex; align-items: center; gap: 12px; }}
  .badge {{ background: #262947; color: var(--accent); padding: 4px 10px; border-radius: 999px; font-size: 12px; font-weight: 600; text-transform: uppercase; }}
  .title-area h1 {{ font-size: 18px; font-weight: 700; color: #fff; }}
  .title-area p {{ font-size: 13px; color: var(--text-muted); }}
  .stats-bar {{ display: flex; align-items: center; gap: 20px; }}
  .stat-pill {{ font-size: 13px; display: flex; align-items: center; gap: 6px; }}
  .dot {{ width: 10px; height: 10px; border-radius: 50%; }}
  .dot-green {{ background: var(--green); }}
  .dot-red {{ background: var(--red); }}
  .dot-gold {{ background: var(--gold); }}

  .actions-area {{ display: flex; gap: 10px; }}
  .btn {{
    padding: 8px 16px; border-radius: 8px; font-size: 13px; font-weight: 600;
    cursor: pointer; border: 1px solid transparent; transition: all 0.2s ease;
  }}
  .btn-primary {{ background: var(--accent); color: white; }}
  .btn-primary:hover {{ background: #4f46e5; box-shadow: 0 4px 12px var(--accent-glow); }}
  .btn-secondary {{ background: #232538; color: var(--text); border-color: var(--card-border); }}
  .btn-secondary:hover {{ background: #2e3049; }}

  .container {{ max-width: 1440px; margin: 24px auto; padding: 0 24px; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(420px, 1fr)); gap: 24px; }}

  .card {{
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 14px;
    overflow: hidden;
    transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
    display: flex; flex-direction: column;
  }}
  .card:hover {{ transform: translateY(-3px); border-color: var(--card-hover); box-shadow: 0 8px 24px rgba(0,0,0,0.4); }}
  .card.needs-regen {{ border-color: var(--red); box-shadow: 0 0 16px rgba(239, 68, 68, 0.2); }}
  .card.approved {{ border-color: var(--green); }}

  .card-media {{ position: relative; width: 100%; aspect-ratio: 16/9; background: #000; cursor: pointer; }}
  .card-media img {{ width: 100%; height: 100%; object-fit: cover; display: block; }}
  .card-media .zoom-hint {{
    position: absolute; right: 10px; bottom: 10px;
    background: rgba(0,0,0,0.6); padding: 4px 8px; border-radius: 6px;
    font-size: 11px; opacity: 0; transition: opacity 0.2s;
  }}
  .card-media:hover .zoom-hint {{ opacity: 1; }}

  .card-body {{ padding: 16px; display: flex; flex-direction: column; gap: 12px; flex: 1; }}
  .card-header {{ display: flex; align-items: flex-start; justify-content: space-between; gap: 10px; }}
  .scene-tag {{
    font-size: 11px; font-weight: 700; color: var(--gold);
    background: rgba(245, 158, 11, 0.12); border: 1px solid rgba(245, 158, 11, 0.25);
    padding: 2px 8px; border-radius: 6px;
  }}
  .act-tag {{ font-size: 11px; color: var(--text-muted); }}
  .beat-title {{ font-size: 15px; font-weight: 600; color: #fff; line-height: 1.3; }}

  .section-label {{ font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--text-muted); letter-spacing: 0.5px; margin-bottom: 2px; }}
  .text-box {{
    background: #11121b; border: 1px solid #23253a;
    border-radius: 8px; padding: 10px; font-size: 12px; line-height: 1.45; color: #d1d5db;
  }}
  .narrator-box {{ background: #161826; border-left: 3px solid var(--accent); }}

  .card-footer {{
    margin-top: auto; padding-top: 12px; border-top: 1px solid var(--card-border);
    display: flex; flex-direction: column; gap: 10px;
  }}
  .status-controls {{ display: flex; gap: 8px; }}
  .btn-check {{
    flex: 1; padding: 7px; border-radius: 6px; border: 1px solid var(--card-border);
    background: #202235; color: var(--text-muted); font-size: 12px; font-weight: 600;
    cursor: pointer; transition: all 0.15s; text-align: center;
  }}
  .btn-check:hover {{ background: #282a42; color: #fff; }}
  .btn-check.active-ok {{ background: rgba(16, 185, 129, 0.2); border-color: var(--green); color: var(--green); }}
  .btn-check.active-regen {{ background: rgba(239, 68, 68, 0.2); border-color: var(--red); color: var(--red); }}

  .notes-input {{
    width: 100%; background: #12131d; border: 1px solid #282a40;
    border-radius: 6px; padding: 6px 10px; font-size: 12px; color: #fff;
  }}
  .notes-input:focus {{ outline: none; border-color: var(--accent); }}

  /* Modal Lightbox */
  #lightbox {{
    display: none; position: fixed; inset: 0; z-index: 1000;
    background: rgba(0,0,0,0.92); backdrop-filter: blur(10px);
    align-items: center; justify-content: center; flex-direction: column; padding: 20px;
  }}
  #lightbox img {{ max-width: 90vw; max-height: 80vh; object-fit: contain; border-radius: 8px; box-shadow: 0 10px 40px rgba(0,0,0,0.8); }}
  #lightbox-caption {{ margin-top: 14px; font-size: 15px; color: #fff; font-weight: 600; text-align: center; }}
  #lightbox-close {{
    position: absolute; top: 20px; right: 30px; font-size: 32px; color: #fff;
    cursor: pointer; background: transparent; border: none;
  }}
</style>
</head>
<body>

<header>
  <div class="brand">
    <span class="badge">Babylon 570 TCN</span>
    <div class="title-area">
      <h1>Review Khung Ảnh Đầu (Scene Images)</h1>
      <p>Dự án Time Travel Vlog • Tỉ lệ 16:9 • Nhân vật: Mia</p>
    </div>
  </div>
  <div class="stats-bar">
    <div class="stat-pill"><span class="dot dot-gold"></span> Tổng: <strong id="stat-total">23</strong></div>
    <div class="stat-pill"><span class="dot dot-green"></span> Đạt: <strong id="stat-ok">0</strong></div>
    <div class="stat-pill"><span class="dot dot-red"></span> Cần Gen Lại: <strong id="stat-regen">0</strong></div>
  </div>
  <div class="actions-area">
    <button class="btn btn-secondary" onclick="exportFeedback()">📋 Copy Danh Sách Cần Gen Lại</button>
    <button class="btn btn-primary" onclick="markAllOk()">✔ Đánh Dấu Tất Cả Đạt</button>
  </div>
</header>

<div class="container">
  <div class="grid" id="scenes-grid"></div>
</div>

<div id="lightbox" onclick="closeLightbox(event)">
  <button id="lightbox-close" onclick="closeLightbox()">&times;</button>
  <img id="lightbox-img" src="" alt="Zoomed view">
  <div id="lightbox-caption"></div>
</div>

<script>
const scenes = {scenes_json};

function loadState() {{
  try {{
    return JSON.parse(localStorage.getItem('babylon_review_state') || '{{}}');
  }} catch(e) {{
    return {{}};
  }}
}}

function saveState(state) {{
  localStorage.setItem('babylon_review_state', JSON.stringify(state));
  updateStats();
}}

const state = loadState();

function updateStats() {{
  let okCount = 0;
  let regenCount = 0;
  scenes.forEach(s => {{
    const st = state[s.index]?.status;
    if (st === 'OK') okCount++;
    if (st === 'REGEN') regenCount++;
  }});
  document.getElementById('stat-ok').textContent = okCount;
  document.getElementById('stat-regen').textContent = regenCount;
}}

function setStatus(idx, st) {{
  if (!state[idx]) state[idx] = {{}};
  state[idx].status = st;
  saveState(state);
  render();
}}

function setNote(idx, note) {{
  if (!state[idx]) state[idx] = {{}};
  state[idx].note = note;
  saveState(state);
}}

function markAllOk() {{
  scenes.forEach(s => {{
    if (!state[s.index]) state[s.index] = {{}};
    state[s.index].status = 'OK';
  }});
  saveState(state);
  render();
}}

function exportFeedback() {{
  const regens = [];
  scenes.forEach(s => {{
    const st = state[s.index]?.status;
    const note = state[s.index]?.note || '';
    if (st === 'REGEN') {{
      regens.push(`- Cảnh ${{String(s.index).padStart(2, '0')}} (${{s.beat_title}}): ${{note || 'Yêu cầu gen lại hình ảnh'}}`);
    }}
  }});

  if (regens.length === 0) {{
    alert('Hiện chưa có cảnh nào được đánh dấu "Cần Gen Lại". Tất cả đều Đạt!');
    return;
  }}

  const text = "DANH SÁCH CẢNH CẦN GEN LẠI HÌNH ẢNH:\\n" + regens.join("\\n");
  navigator.clipboard.writeText(text).then(() => {{
    alert(`Đã copy danh sách ${{regens.length}} cảnh cần gen lại vào clipboard! Bạn có thể dán trực tiếp vào chat.`);
  }}).catch(() => {{
    alert(text);
  }});
}}

function openLightbox(src, caption) {{
  const lb = document.getElementById('lightbox');
  document.getElementById('lightbox-img').src = src;
  document.getElementById('lightbox-caption').textContent = caption;
  lb.style.display = 'flex';
}}

function closeLightbox(e) {{
  if (!e || e.target.id === 'lightbox' || e.target.id === 'lightbox-close') {{
    document.getElementById('lightbox').style.display = 'none';
  }}
}}

function render() {{
  const grid = document.getElementById('scenes-grid');
  grid.innerHTML = '';

  scenes.forEach(s => {{
    const st = state[s.index]?.status || '';
    const note = state[s.index]?.note || '';

    const card = document.createElement('div');
    card.className = `card ${{st === 'REGEN' ? 'needs-regen' : (st === 'OK' ? 'approved' : '')}}`;

    card.innerHTML = `
      <div class="card-media" onclick="openLightbox('${{s.img_src}}', 'Cảnh ${{String(s.index).padStart(2, '0')}} - ${{s.beat_title}}')">
        <img src="${{s.img_src}}" alt="Cảnh ${{s.index}}" loading="lazy">
        <div class="zoom-hint">🔍 Bấm để phóng to</div>
      </div>
      <div class="card-body">
        <div class="card-header">
          <div>
            <span class="scene-tag">Cảnh ${{String(s.index).padStart(2, '0')}} • ${{s.beat_code}}</span>
            <div class="act-tag">${{s.act}}</div>
          </div>
          <span style="font-size: 11px; color: #64748b; font-family: monospace;">UUID: ${{s.media_id ? s.media_id.substring(0,8) : 'N/A'}}</span>
        </div>
        <div class="beat-title">${{s.beat_title}}</div>

        <div>
          <div class="section-label">Hành động Prompt:</div>
          <div class="text-box">${{s.prompt}}</div>
        </div>

        <div>
          <div class="section-label">Lời thoại / Thuyết minh:</div>
          <div class="text-box narrator-box">${{s.narrator || 'Không có thoại'}}</div>
        </div>

        <div class="card-footer">
          <div class="status-controls">
            <button class="btn-check ${{st === 'OK' ? 'active-ok' : ''}}" onclick="setStatus(${{s.index}}, 'OK')">✔ Đạt</button>
            <button class="btn-check ${{st === 'REGEN' ? 'active-regen' : ''}}" onclick="setStatus(${{s.index}}, 'REGEN')">🔄 Cần Gen Lại</button>
          </div>
          <input type="text" class="notes-input" placeholder="Ghi chú chỉnh sửa (nếu cần)..." value="${{note}}" onchange="setNote(${{s.index}}, this.value)">
        </div>
      </div>
    `;
    grid.appendChild(card);
  }});
  updateStats();
}}

render();
</script>
</body>
</html>
"""

with open(HTML_FILE, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Generated review HTML gallery: {HTML_FILE}")
