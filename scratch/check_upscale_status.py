import sqlite3

conn = sqlite3.connect('flow_agent.db')
cur = conn.cursor()
vid = '19cbad31-3cd4-49f8-80de-874c1093a8b4'
rows = cur.execute('''
    SELECT display_order, id, horizontal_video_status, horizontal_video_media_id,
           horizontal_upscale_status, horizontal_upscale_media_id, horizontal_upscale_url
    FROM scene
    WHERE video_id=?
    ORDER BY display_order ASC
''', (vid,)).fetchall()

print(f"Total scenes for video {vid}: {len(rows)}")
print(f"{'Scene':<6} | {'Scene ID':<10} | {'Video Status':<14} | {'Video Media ID':<38} | {'Upscale Status':<16} | {'Upscale Media ID'}")
print("-" * 120)
for r in rows:
    order, sid, v_status, v_media, u_status, u_media, u_url = r
    if order <= 8 or order == 31:
        print(f"S{order:02d}    | {sid[:8]}   | {str(v_status):<14} | {str(v_media):<38} | {str(u_status):<16} | {str(u_media)}")
