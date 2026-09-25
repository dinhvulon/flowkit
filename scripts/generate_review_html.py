import sqlite3
import json
import os

PID = "ac50c619-1b31-4847-95d6-5379d02554c7"
VID = "dc2afa55-8a7f-42c3-bf8c-a13f580b6830"
proj_dir = os.path.join("output", "time_travel_vlog_ancient_babylon_570_bc")

conn = sqlite3.connect("flow_agent.db")
conn.row_factory = sqlite3.Row

scenes_rows = conn.execute("""
    SELECT display_order, id, prompt, image_prompt, video_prompt, narrator_text, character_names,
           horizontal_image_media_id, horizontal_video_media_id, horizontal_video_url
    FROM scene
    WHERE video_id=?
    ORDER BY display_order
""", (VID,)).fetchall()

fixed_orders = {
    2: {
        "title": "Scene 03 — First Contact (Đoàn Thuyền Quffa & Người Chèo Sông Euphrates)",
        "fix_note": "✓ ĐÃ SỬA: Đã thêm người chèo thuyền cơ bắp đứng chèo thuyền quffa tròn chở đất và cây non; loại bỏ thuyền trôi dạt không người."
    },
    7: {
        "title": "Scene 08 — Table Prop-up Dining (Ngồi Ăn Quả Sung Tươi Trên Tầng Thượng)",
        "fix_note": "✓ ĐÃ SỬA: Loại bỏ hoàn toàn điện thoại di động trên bàn ăn; máy quay gác tĩnh tự nhiên nhìn Mia thưởng thức quả sung."
    },
    9: {
        "title": "Scene 10 — Ancient Trade: Silver Shekels (POV Bàn Tay Nữ Cầm Cuộn Bạc Shekel)",
        "fix_note": "✓ ĐÃ SỬA: Góc nhìn POV bàn tay nữ thanh mảnh của Mia cầm dây bạc cuộn đổi hương liệu núi; loại bỏ tay thô ráp của nam giới."
    },
    11: {
        "title": "Scene 12 — Reveal #1: Imperial Guards (Quay Gáy 180 Độ: 1 Cô Gái Mia Nhìn Lính Canh)",
        "fix_note": "✓ ĐÃ SỬA: Đã sửa lỗi nhân bản 2 cô gái. Khung hình chỉ có DUY NHẤT 1 nhân vật nữ Mia nấp sau cột đá nhìn 2 lính tuần."
    },
    14: {
        "title": "Scene 15 — Chase Behind Waterfall (Chạy Trốn Sau Màn Thác Nước Cổ)",
        "fix_note": "✓ ĐÃ SỬA: Mia chạy trốn sau màn thác nước với 2 TAY HOÀN TOÀN TỰ DO; không còn cầm đèn lồng vô lý."
    },
    15: {
        "title": "Scene 16 — The Upper Nursery (Chốt Then Cửa Thoát Hiểm Vào Vườn Ươm)",
        "fix_note": "✓ ĐÃ SỬA: Đã sửa lỗi gen; Mia kéo chốt then cửa gỗ tuyết tùng vào vườn ươm, dựa tường nghỉ ngơi, 2 tay tự do."
    },
    19: {
        "title": "Scene 20 — Myth Busted: Overhanging (Vlog Ban Công Đá Nhô Ra Vực Trời)",
        "fix_note": "✓ ĐÃ SỬA: Góc máy vlog siêu rộng 0.5x hướng về Mia; 2 tay hoàn toàn tự do, không cầm điện thoại bên tay phải."
    },
    22: {
        "title": "Scene 23 — Stone Balustrade Sign-off (Ngồi Lan Can Đá Ngắm Hoàng Hôn Tạm Biệt)",
        "fix_note": "✓ ĐÃ SỬA: Máy quay gác tĩnh trên lan can đá đối diện; Mia ngồi thư thái hai tay thả lỏng tự nhiên, không cầm điện thoại selfie."
    }
}

# Beat metadata for rich display
scene_beats = [
    ("Beat 01", "The Shock Arrival (Bờ sông Euphrates & Cỗ xe bò lướt sát ống kính)", "Hồi 1: Hook"),
    ("Beat 02", "Story of King & Queen (Vừa đi vừa kể chuyện Vua Nebuchadnezzar & Hoàng Hậu Amytis)", "Hồi 1: Hook"),
    ("Beat 03", "Euphrates Quffa Boats (POV sông Euphrates & thuyền thúng quffa chở đất, cây non)", "Hồi 2: Đời thường"),
    ("Beat 04", "Ancient Chain Pump (Ngước nhìn guồng nước / bơm xích khổng lồ nâng nước sông)", "Hồi 2: Đời thường"),
    ("Beat 05", "Waterproof Secret (POV xúc giác: Sờ lớp hắc ín bitum & chiếu cói chống thấm)", "Hồi 2: Đời thường"),
    ("Beat 06", "The Colossal Vaults (Đi dưới vòm gạch nung khổng lồ đỡ ngọn núi cây)", "Hồi 2: Đời thường"),
    ("Beat 07", "Garden Bazaar (Dạo chợ nông sản dưới bóng râm vườn treo, lựu đỏ & vả tươi)", "Hồi 2: Đời thường"),
    ("Beat 08", "Table Prop-up Dining #1 (Gác máy lên bàn: Ngồi ăn quả vả tươi hái tại vườn)", "Hồi 2: Đời thường"),
    ("Beat 09", "Gravity-Fed Aqueducts (Đi dọc kênh dẫn nước bậc thang đá vôi trong vắt)", "Hồi 2: Đời thường"),
    ("Beat 10", "Ancient Trade: Silver Shekels (POV xúc giác: Cân cuộn dây bạc shekel đổi hoa thơm)", "Hồi 2: Đời thường"),
    ("Beat 11", "Ascending Royal Terraces (Leo thang đá lên tầng cấm của hoàng gia)", "Hồi 3: Quyền lực"),
    ("Beat 12", "Reveal #1: Imperial Guards (Quay gáy 180 độ: Lính ngự lâm giáp vảy canh gác)", "Hồi 3: Quyền lực"),
    ("Beat 13", "Hidden in Flowers (Nấp sau giàn hoa giấy tím, lính tuần qua)", "Hồi 3: Quyền lực"),
    ("Beat 14", "Royal Procession (Đoàn ngự giá hoàng gia đi qua & bị lính phát hiện)", "Hồi 4: Cao trào"),
    ("Beat 15", "Chase Behind Waterfall (Rượt đuổi nghẹt thở sau màn thác nước cổ)", "Hồi 4: Cao trào"),
    ("Beat 16", "The Upper Nursery (Chốt cửa gỗ thoát hiểm vào vườn ươm trên cao)", "Hồi 4: Cao trào"),
    ("Beat 17", "The Kind Gardener (Gặp ông lão làm vườn hiền lành chỉ đường lên đỉnh)", "Hồi 5: Hạ nhịp"),
    ("Beat 18", "Reveal #2: Sky Oasis (Tầng thác nước ngoạn mục & hồ ngọc bích lơ lửng giữa trời)", "Hồi 6: Di sản"),
    ("Beat 19", "Lebanese Cedar Giant (Gốc cây tuyết tùng Lebanon khổng lồ bén rễ trên mái tháp)", "Hồi 6: Di sản"),
    ("Beat 20", "Myth Busted: Overhanging (Giải mã bí mật: Vườn nhô ra trên không chứ không treo)", "Hồi 6: Di sản"),
    ("Beat 21", "Summit Spring Water (POV xúc giác: Vốc dòng nước nguồn mát lạnh đỉnh tháp)", "Hồi 6: Di sản"),
    ("Beat 22", "Reveal #3: Crown of Ancient World (Toàn cảnh đỉnh: Cổng Ishtar xanh biếc & Ziggurat 90m)", "Hồi 6: Di sản"),
    ("Beat 23", "Stone Balustrade Sign-off #2 (Gác máy thành đá: Hoàng hôn tím vàng & lời tạm biệt)", "Hồi 7: Kết trầm"),
]

scenes_data = []
for s in scenes_rows:
    order = s['display_order']
    idx = order + 1
    sid = s['id']
    is_fixed = order in fixed_orders
    fix_info = fixed_orders.get(order, {})
    
    b_code, b_title, act = scene_beats[order] if order < len(scene_beats) else (f"Beat {idx:02d}", "Babylon Vlog", "Vlog")
    
    scenes_data.append({
        "index": idx,
        "scene_id": sid,
        "media_id": s['horizontal_image_media_id'],
        "video_media_id": s['horizontal_video_media_id'],
        "img_src": f"images/scene_{idx:02d}.jpg",
        "video_src": f"scenes/scene_{idx:02d}_{sid[:8]}.mp4",
        "beat_code": b_code,
        "beat_title": fix_info.get("title", b_title),
        "act": act,
        "is_fixed": is_fixed,
        "fix_note": fix_info.get("fix_note", ""),
        "prompt": s['prompt'],
        "video_prompt": s['video_prompt'],
        "narrator": s['narrator_text'] or ""
    })

scenes_json = json.dumps(scenes_data, ensure_ascii=False)

html_template = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Review 23 Ảnh Khung Đầu & Video — Vườn Treo Babylon (570 TCN)</title>
<style>
  :root {{
    --bg: #0d0f15;
    --card-bg: #161822;
    --card-border: #232636;
    --card-hover: #32374e;
    --accent: #6366f1;
    --accent-glow: rgba(99, 102, 241, 0.35);
    --gold: #f59e0b;
    --green: #10b981;
    --red: #ef4444;
    --text: #f3f4f6;
    --text-muted: #94a3b8;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", Roboto, sans-serif; }}
  body {{ background: var(--bg); color: var(--text); padding-bottom: 80px; }}
  
  header {{
    position: sticky; top: 0; z-index: 100;
    background: rgba(13, 15, 21, 0.94);
    backdrop-filter: blur(16px);
    border-bottom: 1px solid var(--card-border);
    padding: 16px 28px;
    display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px;
  }}
  .brand {{ display: flex; align-items: center; gap: 12px; }}
  .badge {{ background: #262947; color: var(--accent); padding: 4px 10px; border-radius: 999px; font-size: 12px; font-weight: 700; text-transform: uppercase; }}
  .title-area h1 {{ font-size: 18px; font-weight: 700; color: #fff; }}
  .title-area p {{ font-size: 13px; color: var(--text-muted); margin-top: 2px; }}
  
  .stats-bar {{ display: flex; align-items: center; gap: 16px; }}
  .stat-pill {{ font-size: 13px; display: flex; align-items: center; gap: 6px; background: #1b1e2b; padding: 6px 12px; border-radius: 8px; border: 1px solid var(--card-border); }}
  .dot {{ width: 10px; height: 10px; border-radius: 50%; }}
  .dot-green {{ background: var(--green); }}
  .dot-red {{ background: var(--red); }}
  .dot-gold {{ background: var(--gold); }}

  .actions-area {{ display: flex; gap: 10px; }}
  .btn {{
    padding: 8px 16px; border-radius: 8px; font-size: 13px; font-weight: 600;
    cursor: pointer; border: 1px solid transparent; transition: all 0.2s ease; display: inline-flex; align-items: center; gap: 6px;
  }}
  .btn-primary {{ background: var(--accent); color: white; }}
  .btn-primary:hover {{ background: #4f46e5; box-shadow: 0 4px 14px var(--accent-glow); }}
  .btn-secondary {{ background: #202334; color: var(--text); border-color: var(--card-border); }}
  .btn-secondary:hover {{ background: #2b2f46; }}
  .btn-gold {{ background: #92400e; color: #fef3c7; border-color: #d97706; }}
  .btn-gold:hover {{ background: #b45309; }}

  /* Filter toolbar */
  .toolbar {{
    max-width: 1440px; margin: 20px auto 0 auto; padding: 0 24px;
    display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;
  }}
  .filter-group {{ display: flex; gap: 8px; }}
  .filter-btn {{
    background: #1b1e2b; border: 1px solid var(--card-border); color: var(--text-muted);
    padding: 6px 14px; border-radius: 6px; font-size: 12px; font-weight: 600; cursor: pointer;
  }}
  .filter-btn.active {{ background: var(--accent); color: #fff; border-color: var(--accent); }}

  .container {{ max-width: 1440px; margin: 20px auto; padding: 0 24px; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(440px, 1fr)); gap: 24px; }}

  .card {{
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: 14px;
    overflow: hidden;
    transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
    display: flex; flex-direction: column;
  }}
  .card:hover {{ transform: translateY(-3px); border-color: var(--card-hover); box-shadow: 0 10px 30px rgba(0,0,0,0.5); }}
  .card.is-fixed {{ border: 2px solid var(--green); box-shadow: 0 0 18px rgba(16, 185, 129, 0.25); }}
  .card.needs-regen {{ border: 2px solid var(--red); box-shadow: 0 0 18px rgba(239, 68, 68, 0.25); }}
  .card.approved {{ border-color: var(--green); }}

  .card-media-wrapper {{
    position: relative; width: 100%; aspect-ratio: 16/9; background: #000;
  }}
  .card-media-wrapper img, .card-media-wrapper video {{
    width: 100%; height: 100%; object-fit: cover; display: block; cursor: pointer;
  }}
  .fixed-banner {{
    position: absolute; top: 10px; left: 10px; z-index: 10;
    background: rgba(16, 185, 129, 0.92); color: #000; font-weight: 800; font-size: 11px;
    padding: 4px 10px; border-radius: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.4);
    display: flex; align-items: center; gap: 4px;
  }}
  .zoom-hint {{
    position: absolute; right: 10px; bottom: 10px; z-index: 10;
    background: rgba(0,0,0,0.7); color: #fff; padding: 4px 8px; border-radius: 6px;
    font-size: 11px; opacity: 0; transition: opacity 0.2s; pointer-events: none;
  }}
  .card-media-wrapper:hover .zoom-hint {{ opacity: 1; }}

  .view-toggle-bar {{
    position: absolute; right: 10px; top: 10px; z-index: 10;
    display: flex; background: rgba(0,0,0,0.75); border-radius: 6px; overflow: hidden;
  }}
  .view-toggle-btn {{
    background: transparent; border: none; color: #cbd5e1; font-size: 11px; font-weight: 700;
    padding: 4px 8px; cursor: pointer; transition: background 0.15s;
  }}
  .view-toggle-btn.active {{ background: var(--accent); color: #fff; }}

  .card-body {{ padding: 16px; display: flex; flex-direction: column; gap: 12px; flex: 1; }}
  .card-header {{ display: flex; align-items: flex-start; justify-content: space-between; gap: 10px; }}
  .scene-tag {{
    font-size: 11px; font-weight: 700; color: var(--gold);
    background: rgba(245, 158, 11, 0.12); border: 1px solid rgba(245, 158, 11, 0.25);
    padding: 2px 8px; border-radius: 6px; white-space: nowrap;
  }}
  .act-tag {{ font-size: 11px; color: var(--text-muted); }}
  .beat-title {{ font-size: 14px; font-weight: 700; color: #fff; line-height: 1.35; }}

  .fix-note-box {{
    background: rgba(16, 185, 129, 0.1); border-left: 3px solid var(--green);
    border-radius: 6px; padding: 8px 10px; font-size: 12px; line-height: 1.4; color: #a7f3d0; font-weight: 500;
  }}

  .section-label {{ font-size: 11px; font-weight: 700; text-transform: uppercase; color: var(--text-muted); letter-spacing: 0.5px; margin-bottom: 2px; }}
  .text-box {{
    background: #0f111a; border: 1px solid #1f2233;
    border-radius: 8px; padding: 10px; font-size: 12px; line-height: 1.45; color: #d1d5db; max-height: 85px; overflow-y: auto;
  }}
  .narrator-box {{ background: #131624; border-left: 3px solid var(--accent); }}

  .card-footer {{
    margin-top: auto; padding-top: 12px; border-top: 1px solid var(--card-border);
    display: flex; flex-direction: column; gap: 10px;
  }}
  .status-controls {{ display: flex; gap: 8px; }}
  .btn-check {{
    flex: 1; padding: 8px; border-radius: 6px; border: 1px solid var(--card-border);
    background: #1b1e2c; color: var(--text-muted); font-size: 12px; font-weight: 700;
    cursor: pointer; transition: all 0.15s; text-align: center;
  }}
  .btn-check:hover {{ background: #262a3d; color: #fff; }}
  .btn-check.active-ok {{ background: rgba(16, 185, 129, 0.22); border-color: var(--green); color: var(--green); }}
  .btn-check.active-regen {{ background: rgba(239, 68, 68, 0.22); border-color: var(--red); color: var(--red); }}

  .notes-input {{
    width: 100%; background: #10121c; border: 1px solid #23263a;
    border-radius: 6px; padding: 7px 10px; font-size: 12px; color: #fff;
  }}
  .notes-input:focus {{ outline: none; border-color: var(--accent); }}

  /* Modal Lightbox */
  #lightbox {{
    display: none; position: fixed; inset: 0; z-index: 1000;
    background: rgba(0,0,0,0.94); backdrop-filter: blur(12px);
    align-items: center; justify-content: center; flex-direction: column; padding: 24px;
  }}
  #lightbox img, #lightbox video {{
    max-width: 92vw; max-height: 82vh; object-fit: contain; border-radius: 8px; box-shadow: 0 10px 40px rgba(0,0,0,0.8);
  }}
  #lightbox-caption {{ margin-top: 14px; font-size: 15px; color: #fff; font-weight: 600; text-align: center; max-width: 800px; }}
  #lightbox-close {{
    position: absolute; top: 20px; right: 30px; font-size: 34px; color: #fff;
    cursor: pointer; background: transparent; border: none;
  }}
</style>
</head>
<body>

<header>
  <div class="brand">
    <span class="badge">Babylon 570 TCN</span>
    <div class="title-area">
      <h1>Bảng Review 23 Cảnh — Vườn Treo Babylon (Start Frame & 10s Video)</h1>
      <p>Dự án: Time Travel Vlog (570 BC) • Khung Ngang 16:9 720p • Khóa Outfit "Mia Outfit" Toàn Bộ Phim</p>
    </div>
  </div>
  <div class="stats-bar">
    <div class="stat-pill"><span class="dot dot-gold"></span> Tổng: <strong id="stat-total">23</strong></div>
    <div class="stat-pill"><span class="dot dot-green"></span> Đã sửa: <strong id="stat-fixed">8</strong></div>
    <div class="stat-pill"><span class="dot dot-green"></span> Duyệt Đạt: <strong id="stat-ok">0</strong></div>
    <div class="stat-pill"><span class="dot dot-red"></span> Cần sửa thêm: <strong id="stat-regen">0</strong></div>
  </div>
  <div class="actions-area">
    <button class="btn btn-secondary" onclick="exportFeedback()">📋 Copy Góp Ý</button>
    <button class="btn btn-primary" onclick="markAllOk()">✔ Duyệt Toàn Bộ</button>
  </div>
</header>

<div class="toolbar">
  <div class="filter-group">
    <button class="filter-btn active" onclick="setFilter('all')">Tất cả (23)</button>
    <button class="filter-btn" onclick="setFilter('fixed')">Chỉ xem 8 cảnh vừa sửa</button>
    <button class="filter-btn" onclick="setFilter('regen')">Cảnh đánh dấu cần gen lại</button>
  </div>
  <div style="font-size: 13px; color: var(--text-muted);">
    💡 <i>Click vào ảnh để phóng to siêu nét (Lightbox) hoặc chuyển chế độ xem Video clip 10s</i>
  </div>
</div>

<div class="container">
  <div class="grid" id="scenes-grid"></div>
</div>

<div id="lightbox" onclick="closeLightbox(event)">
  <button id="lightbox-close" onclick="closeLightbox()">&times;</button>
  <div id="lightbox-media-container" onclick="event.stopPropagation()"></div>
  <div id="lightbox-caption"></div>
</div>

<script>
const scenes = {scenes_json};

let currentFilter = 'all';
let viewModes = {{}}; // idx -> 'img' or 'video'

function loadState() {{
  try {{
    return JSON.parse(localStorage.getItem('babylon_review_state_v4') || '{{}}');
  }} catch(e) {{
    return {{}};
  }}
}}

function saveState(state) {{
  localStorage.setItem('babylon_review_state_v4', JSON.stringify(state));
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

function setFilter(f) {{
  currentFilter = f;
  document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
  event.target.classList.add('active');
  render();
}}

function toggleMedia(idx, mode) {{
  viewModes[idx] = mode;
  render();
}}

function openLightbox(src, title, isVideo) {{
  const lb = document.getElementById('lightbox');
  const container = document.getElementById('lightbox-media-container');
  const caption = document.getElementById('lightbox-caption');
  
  if (isVideo) {{
    container.innerHTML = `<video controls autoplay style="max-width:92vw; max-height:80vh; border-radius:8px;"><source src="${{src}}" type="video/mp4"></video>`;
  }} else {{
    container.innerHTML = `<img src="${{src}}" alt="Zoomed" style="max-width:92vw; max-height:80vh; border-radius:8px; object-fit:contain;">`;
  }}
  caption.textContent = title;
  lb.style.display = 'flex';
}}

function closeLightbox(e) {{
  if (e && e.target.tagName === 'VIDEO') return;
  const lb = document.getElementById('lightbox');
  document.getElementById('lightbox-media-container').innerHTML = '';
  lb.style.display = 'none';
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
    navigator.clipboard.writeText("Tất cả 23 cảnh start frame và video đều ĐẠT chuẩn!");
    alert("Đã copy vào Clipboard: Toàn bộ 23 cảnh ĐẠT!");
  }} else {{
    const text = "DANH SÁCH CẦN SỬA LẠI:\\n" + regens.join('\\n');
    navigator.clipboard.writeText(text);
    alert("Đã copy danh sách " + regens.length + " cảnh cần sửa vào Clipboard!");
  }}
}}

function render() {{
  const grid = document.getElementById('scenes-grid');
  grid.innerHTML = '';

  const filtered = scenes.filter(s => {{
    if (currentFilter === 'fixed') return s.is_fixed;
    if (currentFilter === 'regen') return state[s.index]?.status === 'REGEN';
    return true;
  }});

  filtered.forEach(s => {{
    const st = state[s.index]?.status;
    const note = state[s.index]?.note || '';
    const mode = viewModes[s.index] || 'img';

    const card = document.createElement('div');
    let cardClass = 'card';
    if (s.is_fixed) cardClass += ' is-fixed';
    if (st === 'OK') cardClass += ' approved';
    if (st === 'REGEN') cardClass += ' needs-regen';
    card.className = cardClass;

    const bannerHtml = s.is_fixed 
      ? `<div class="fixed-banner"><span>✓ ĐÃ SỬA THEO YÊU CẦU</span></div>` 
      : '';

    const fixNoteHtml = s.fix_note 
      ? `<div class="fix-note-box">${{s.fix_note}}</div>` 
      : '';

    let mediaHtml = '';
    if (mode === 'img') {{
      mediaHtml = `
        <div class="card-media-wrapper" onclick="openLightbox('${{s.img_src}}', 'Cảnh ${{String(s.index).padStart(2, '0')}}: ${{s.beat_title}}', false)">
          ${{bannerHtml}}
          <div class="view-toggle-bar" onclick="event.stopPropagation()">
            <button class="view-toggle-btn active">Ảnh Đầu</button>
            <button class="view-toggle-btn" onclick="toggleMedia(${{s.index}}, 'video')">Clip 10s</button>
          </div>
          <img src="${{s.img_src}}" alt="Cảnh ${{s.index}}" loading="lazy">
          <div class="zoom-hint">🔍 Click phóng to ảnh</div>
        </div>
      `;
    }} else {{
      mediaHtml = `
        <div class="card-media-wrapper">
          ${{bannerHtml}}
          <div class="view-toggle-bar" onclick="event.stopPropagation()">
            <button class="view-toggle-btn" onclick="toggleMedia(${{s.index}}, 'img')">Ảnh Đầu</button>
            <button class="view-toggle-btn active">Clip 10s</button>
          </div>
          <video controls preload="metadata" style="width:100%; height:100%; object-fit:cover;">
            <source src="${{s.video_src}}" type="video/mp4">
          </video>
        </div>
      `;
    }}

    card.innerHTML = `
      ${{mediaHtml}}
      <div class="card-body">
        <div class="card-header">
          <div>
            <span class="scene-tag">Cảnh ${{String(s.index).padStart(2, '0')}}</span>
            <span class="act-tag" style="margin-left: 6px;">${{s.act}}</span>
          </div>
          <span style="font-size:11px; color:var(--text-muted); font-family:monospace;">${{s.media_id ? s.media_id.substring(0,8) : ''}}</span>
        </div>

        <div class="beat-title">${{s.beat_title}}</div>
        ${{fixNoteHtml}}

        <div>
          <div class="section-label">Prompt Tạo Ảnh (Start Frame):</div>
          <div class="text-box">${{s.prompt}}</div>
        </div>

        <div>
          <div class="section-label">Video Prompt (10s Native Audio):</div>
          <div class="text-box narrator-box">${{s.video_prompt}}</div>
        </div>

        <div class="card-footer">
          <div class="status-controls">
            <button class="btn-check ${{st === 'OK' ? 'active-ok' : ''}}" onclick="setStatus(${{s.index}}, 'OK')">
              ✔ ĐẠT CHUẨN
            </button>
            <button class="btn-check ${{st === 'REGEN' ? 'active-regen' : ''}}" onclick="setStatus(${{s.index}}, 'REGEN')">
              ✖ CẦN GEN LẠI
            </button>
          </div>
          <input type="text" class="notes-input" placeholder="Ghi chú nhận xét hoặc yêu cầu sửa..." value="${{note}}" oninput="setNote(${{s.index}}, this.value)">
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

out_html_path = os.path.join(proj_dir, "review_images.html")
with open(out_html_path, "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Generated comprehensive review HTML with {len(scenes_data)} scenes at: {out_html_path}")
conn.close()
