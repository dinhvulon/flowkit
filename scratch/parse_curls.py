import urllib.parse
import json

def parse_file(filename):
    print("=== Parsing", filename, "===")
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()

    for line in text.splitlines():
        idx = line.find('f.req=')
        if idx != -1:
            qs = line[idx:].strip()
            while qs and qs[-1] in ("'", '"', ';', '\\'):
                qs = qs[:-1]
            parsed = urllib.parse.parse_qs(qs)
            freq = parsed.get('f.req', [''])[0]
            outer = json.loads(freq)
            rpc_id = outer[0][0][0]
            inner_str = outer[0][0][1]
            print("RPC ID:", rpc_id)
            inner = json.loads(inner_str)
            # Hide the long captcha token for clean display
            if len(inner) > 1 and inner[1] and len(inner[1]) > 10 and inner[1][10]:
                inner[1][10] = ["<CAPTCHA_OR_RECAPTCHA_TOKEN>", inner[1][10][1] if len(inner[1][10]) > 1 else None]
            print("INNER JSON:")
            print(json.dumps(inner, indent=2))
            break

parse_file('scratch/step_534.txt')
parse_file('scratch/step_547.txt')
