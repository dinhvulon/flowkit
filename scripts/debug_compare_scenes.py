import sqlite3
import sys

sys.stdout.reconfigure(encoding="utf-8")

conn = sqlite3.connect("flow_agent.db")
c = conn.cursor()

c.execute("SELECT display_order+1, prompt, video_prompt, narrator_text FROM scene WHERE video_id='71909a60-29f7-460e-807c-ed48b8a12ad1' ORDER BY display_order")
old_scenes = c.fetchall()

c.execute("SELECT display_order+1, prompt, video_prompt, narrator_text FROM scene WHERE video_id='dc2afa55-8a7f-42c3-bf8c-a13f580b6830' ORDER BY display_order")
new_scenes = c.fetchall()

print(f"Old scenes count: {len(old_scenes)}")
print(f"New scenes count: {len(new_scenes)}")

print("\n--- FIRST 6 SCENES IN OLD PROJECT (71909a60...) ---")
for r in old_scenes[:6]:
    print(f"Scene {r[0]:02d}:")
    print(f"  Prompt: {r[1][:100]}...")
    print(f"  Narrator: {r[3]}")

print("\n--- FIRST 6 SCENES IN NEW PROJECT (dc2afa55...) ---")
for r in new_scenes[:6]:
    print(f"Scene {r[0]:02d}:")
    print(f"  Prompt: {r[1][:100]}...")
    print(f"  Narrator: {r[3]}")
