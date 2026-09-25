import json

payload_str = """[[[[null,null,[[["0-3s: A massive wooden cart wheel rolls past inches from the lens in a heavy wipe, revealing Mia standing near the dusty Euphrates riverbank. 3-6s: Mia extends her selfie stick, looks directly into the lens with wide sparkling eyes and says \\\"You guys... welcome to Babylon, 570 BC! And right behind me is the legendary Hanging Gardens!\\\" 6-10s: She points excitedly toward the colossal green terraces as desert palm fronds sway gently in the warm breeze. Audio: no background music. Keep character dialogue and natural ambient sounds. Negative: subtitles, captions, watermark, text on screen, logo, blurry faces, distorted hands."]]]],[[null,"3904fece-f12e-47ef-9018-361f1a74f315"],[null,"894e8d96-d6b1-4070-ba81-d358341ec5a4"]],"abra_r2v_4s",2,null,[null,null,null,null,"6262D394-497F-436A-A905-774053F81494","F51D52D5-72D0-4BBB-ABA6-AA4106589566"],null,[["achernar"]]]],[null,22,null,null,null,"6224591f-b884-42f2-8f57-613bc86d66fb",null,null,null,null,["0cAFcWeA",1]],["C17BB9C6-22A1-49BD-B99C-CBF6AF67386A",2]]"""

data = json.loads(payload_str)
print("Root length:", len(data))
item0 = data[0]
print("item0 length:", len(item0))
inner_spec = item0[0]
print("inner_spec length:", len(inner_spec))
for i, s in enumerate(inner_spec):
    print(f"  Slot {i}: {s}")

print("\nOuter context (item 1):")
print("item 1:", data[1])
print("\nOuter context (item 2):")
print("item 2:", data[2])
