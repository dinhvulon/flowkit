import json
import urllib.parse

with open('scratch/step_534.txt', 'r', encoding='utf-8') as f:
    text = f.read()

for line in text.splitlines():
    if 'f.req=' in line:
        qs = line[line.find('f.req='):].strip().rstrip("';\\\"")
        freq = urllib.parse.parse_qs(qs)['f.req'][0]
        outer = json.loads(freq)
        inner = json.loads(outer[0][0][1])
        item = inner[0][0]
        print(f"Length of inner[0][0]: {len(item)}")
        for idx, val in enumerate(item):
            if val is not None:
                print(f"Slot {idx}: {repr(val)}")
        break
