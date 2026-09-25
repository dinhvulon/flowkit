import sqlite3
import json

conn = sqlite3.connect('flow_agent.db')
cursor = conn.cursor()
scenes = cursor.execute("""
    SELECT display_order, character_names, video_prompt, duration 
    FROM scene 
    WHERE video_id='71909a60-29f7-460e-807c-ed48b8a12ad1' 
    ORDER BY display_order LIMIT 5
""").fetchall()

for s in scenes:
    print(f"Scene {s[0]} (dur: {s[3]}): chars={s[1]}")
    print(f"Prompt: {s[2][:150]}...")
    print("-" * 40)

chars = cursor.execute("""
    SELECT c.name, c.voice_description, c.media_id 
    FROM character c
    JOIN project_character pc ON c.id = pc.character_id
    WHERE pc.project_id='6224591f-b884-42f2-8f57-613bc86d66fb'
""").fetchall()
print("Characters:")
for c in chars:
    print(f"Name: {c[0]}, media_id: {c[2]}")
    print(f"Voice: {c[1]}")

