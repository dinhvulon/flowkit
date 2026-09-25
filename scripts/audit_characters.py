import sqlite3
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

conn = sqlite3.connect("flow_agent.db")
c = conn.cursor()
c.execute("""
    SELECT display_order+1, id, prompt, video_prompt, character_names 
    FROM scene 
    WHERE video_id = 'dc2afa55-8a7f-42c3-bf8c-a13f580b6830' 
    ORDER BY display_order
""")
rows = c.fetchall()

print("=" * 80)
print("DANH SÁCH CÁC CẢNH START FRAME THIẾU NHÂN VẬT HOẶC CÓ NGUY CƠ LỖI:")
print("=" * 80)

flagged = []
for idx, sid, p, vp, chars in rows:
    p_lower = p.lower()
    vp_lower = vp.lower()
    
    # Is Mia or a traveler explicitly placed in the start frame image?
    mia_in_img = any(w in p_lower for w in ["mia", "traveler", "young female", "cô gái", "her hand", "selfie"])
    
    # Does video prompt expect Mia to be seen on camera or step into camera?
    mia_in_vid = any(w in vp_lower for w in ["mia ", "mia,", "mia\"", "mia's voice", "she ", "selfie", "into the camera", "toward the camera"])
    
    # Is there a pop-in motion?
    pop_in = any(w in vp_lower for w in ["steps into", "walks into", "turns into frame", "enters the frame", "steps through"])
    
    # Categorize
    issue = None
    if not mia_in_img and ("mia says" in vp_lower or "mia shouts" in vp_lower or pop_in or "selfie" in vp_lower):
        issue = "CỰC KỲ NGUY HIỂM: Start frame hoàn toàn là cảnh vật không có người, nhưng video bắt Mia bước vào / nói chuyện!"
    elif not mia_in_img and "mia" in vp_lower:
        issue = "CẦN LƯU Ý: Start frame không có nhân vật, chỉ có voiceover dẫn chuyện hoặc Mia xuất hiện sau."
    elif pop_in:
        issue = "LƯU Ý POP-IN: Start frame có Mia nhưng video prompt lại mô tả Mia bước vào khung hình."
        
    if issue:
        flagged.append((idx, sid, issue, p, vp))

for idx, sid, issue, p, vp in flagged:
    print(f"\n🔴 [CẢNH {idx:02d}] (ID: {sid[:8]})")
    print(f"   Vấn đề: {issue}")
    print(f"   - Prompt ảnh hiện tại: {p[:180]}...")
    print(f"   - Video prompt hiện tại: {vp[:180]}...")

conn.close()
