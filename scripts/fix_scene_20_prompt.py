import sqlite3

conn = sqlite3.connect('flow_agent.db')
cur = conn.cursor()

fixed_vp = (
    "0-3s: Ultra-wide 0.5x vlog camera looking at Mia standing on the cantilevered stone balcony "
    "as desert winds whip through lush climbing vines and her blonde ponytail. "
    "3-7s: Mia beams directly into the camera lens with an engaging smile "
    "\"Historical myth busted: the gardens were not 'hanging' on ropes! "
    "The Greek term 'kremastos' means 'overhanging' - just like these dramatic terraces jutting out over the city!\" "
    "7-10s: She turns smoothly to walk toward the sparkling summit fountain pool in the background. "
    "Audio: no background music. Keep character dialogue and natural ambient sounds. "
    "Negative: holding phone in hand, smartphone, selfie stick, subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands."
)

cur.execute("UPDATE scene SET video_prompt=? WHERE id='0fa349bb-c3db-4049-bab8-de4ddf0c3a8a'", (fixed_vp,))
conn.commit()
print("Scene 20 video prompt successfully updated:")
print(fixed_vp)
