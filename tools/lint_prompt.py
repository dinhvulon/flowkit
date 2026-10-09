"""Prompt Linter for FlowKit — Enforces Optical Viewpoint, Anti-Ghost Device, Body Lock, Physics Rules & JSON Prompts."""

import re
import sys
import argparse
import sqlite3
import json

sys.stdout.reconfigure(encoding='utf-8')

FORBIDDEN_GHOST_DEVICE_PATTERNS = [
    (r"\b(phone|smartphone)\b", "FORBIDDEN: Mentioning 'phone' or 'smartphone' causes AI to render a 3D phone device in hand and switches camera to 3rd-person spectator."),
    (r"\b(selfie[- ]?stick)\b", "FORBIDDEN: Mentioning 'selfie stick' renders a physical stick in the shot."),
    (r"\b(device)\b", "FORBIDDEN: Mentioning 'device' causes AI to render gadgets or screens."),
    (r"(?<!off-)(?<!on-)\bscreen\b", "FORBIDDEN: Mentioning 'screen' (except 'off-screen' / 'on-screen') may cause AI to render a phone or monitor screen. Use 'in the frame' instead."),
    (r"\bnegative:\b", "FORBIDDEN: 'Negative:' lines are banned in plain-text prompts. Use plain constraint sentences in prompt body, or use 'negative_constraints' in JSON prompts."),
    (r"\b(?:starts?\s+(?:from\s+)?(?:just\s+)?behind|from\s+just\s+behind)\s+(?:her|his|their)\s+(?:head|back)\b", "FORBIDDEN (Rule 41): Starting behind character's head/back and turning around switches to 3rd-person and causes AI to render a physical camera/lens in hand (Camera Materialization Glitch)."),
    (r"\b(?:brings?|turns?)\s+the\s+camera\s+around\s+(?:her|his|their)\s+side\b", "FORBIDDEN (Rule 41): 'brings the camera around' causes AI to treat camera as a physical handheld prop/lens. Use 'pivots extended arm back toward herself'."),
    (r"\bholds?\s+the\s+camera\s+in\s+(?:her|his|their)\s+hand\b", "FORBIDDEN (Rule 41): Camera must NOT be described as an object held in hand. The viewer looks directly through the lens; gripping hand is off-screen."),
    (r"\b(?:180-degree|180\s*deg|whip\s+pan|pivoting\s+the\s+viewpoint)\b.*\b(?:turning\s+to\s+face|turning\s+around\s+to\s+face|settles?\s+.*selfie|back\s+toward\s+(?:nora|her|him|herself|himself))\b", "FORBIDDEN (Rule 42): 180° camera flip between 1st-person POV and selfie in a single shot breaks single-perspective vlog purity. Use 100% Selfie (over-the-shoulder) or 100% POV."),
]

def is_json_prompt(prompt: str) -> tuple[bool, dict | None]:
    """Check if prompt is a JSON string and parse it if valid."""
    s = prompt.strip()
    if (s.startswith("{") and s.endswith("}")) or (s.startswith("[") and s.endswith("]")):
        try:
            parsed = json.loads(s)
            if isinstance(parsed, dict):
                return True, parsed
        except Exception:
            return True, None  # intended as JSON but malformed
    return False, None


def extract_text_from_json(obj, exclude_keys: tuple = ("negative_constraints", "constraints")) -> str:
    """Extract all text values recursively from a JSON structure for keyword rule checking."""
    texts = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k.lower() in exclude_keys:
                continue
            texts.append(extract_text_from_json(v, exclude_keys))
    elif isinstance(obj, list):
        for item in obj:
            texts.append(extract_text_from_json(item, exclude_keys))
    elif isinstance(obj, str):
        texts.append(obj)
    return " ".join(texts)


def lint_json_prompt(data: dict) -> list[dict]:
    """Check structured JSON prompt against FlowKit rules and schema requirements."""
    issues = []

    # 1. Schema Structure Checks
    required_keys = ["camera", "setting", "characters", "timeline_action"]
    for k in required_keys:
        if k == "timeline_action" and not any(alias in data for alias in ["timeline_action", "timeline", "action"]):
            issues.append({
                "severity": "HIGH",
                "type": "JSON_SCHEMA_MISSING_KEY",
                "message": "JSON prompt missing required 'timeline_action' key (or 'timeline' / 'action')."
            })
        elif k != "timeline_action" and k not in data:
            issues.append({
                "severity": "HIGH",
                "type": "JSON_SCHEMA_MISSING_KEY",
                "message": f"JSON prompt missing required '{k}' key."
            })

    # 2. Camera field checks
    camera_data = data.get("camera", {})
    if isinstance(camera_data, dict):
        cam_text = " ".join(str(v) for v in camera_data.values()).lower()
        if "selfie" in cam_text or "front-lens" in cam_text or "vlog" in cam_text:
            constraints_text = " ".join(str(x) for x in data.get("negative_constraints", [])).lower()
            if not ("off-screen" in cam_text or "outside the visible frame" in cam_text or "outside the frame" in cam_text or "outside the frame" in constraints_text or "off-screen" in constraints_text):
                issues.append({
                    "severity": "HIGH",
                    "type": "OPTICAL_VIEWPOINT",
                    "message": "JSON camera or negative_constraints is missing explicit camera blind-spot constraint: 'the camera lens itself and her right gripping hand are completely outside the visible frame and never seen'."
                })

    # 3. Characters field checks
    chars_data = data.get("characters", [])
    if isinstance(chars_data, list):
        for idx, ch in enumerate(chars_data):
            if isinstance(ch, dict):
                has_lock = any(k in ch for k in ["visual_lock", "reference_lock", "visual_reference", "reference"])
                if not has_lock:
                    issues.append({
                        "severity": "MEDIUM",
                        "type": "CHARACTER_REF_LOCK",
                        "message": f"Character [{ch.get('name', idx)}] in JSON prompt is missing 'visual_lock' or 'reference_lock' attribute."
                    })

    # 4. Timeline action breakdown checks
    action_data = data.get("timeline_action") or data.get("timeline") or data.get("action", {})
    if isinstance(action_data, dict):
        has_subclips = any(re.search(r"\b\d+-\d+s\b", k) for k in action_data.keys())
        if not has_subclips:
            issues.append({
                "severity": "MEDIUM",
                "type": "TIMELINE_SUBCLIPS",
                "message": "JSON 'timeline_action' should use sub-clip keys (e.g. '0-3s', '3-6s', '6-8s') for precise temporal pacing."
            })

    # 5. Extract all text for keyword rule checking (excluding negative_constraints key)
    extracted_text = extract_text_from_json(data)
    text_lower = extracted_text.lower()

    # 6. Ghost Device patterns on extracted text
    for pat, msg in FORBIDDEN_GHOST_DEVICE_PATTERNS:
        if pat == r"\bnegative:\b":
            continue  # JSON uses "negative_constraints" array, which is valid and encouraged
        matches = list(re.finditer(pat, text_lower))
        if matches:
            for m in matches:
                issues.append({
                    "severity": "CRITICAL",
                    "type": "GHOST_DEVICE",
                    "token": m.group(0),
                    "position": m.start(),
                    "message": msg
                })

    # 7. Camera Touch / Lens Blocking
    if "selfie" in text_lower or "front-lens" in text_lower:
        m_reach = re.search(r"\b(?:reaches?|extends?|brings?)\s+(?:her|his|their)?\s*(?:free\s*)?(?:hand|arm)\s+toward\s+(?:the\s+)?(?:camera|lens|screen)\b", text_lower)
        if m_reach:
            issues.append({
                "severity": "CRITICAL",
                "type": "CAMERA_TOUCH_GLITCH",
                "token": m_reach.group(0),
                "position": m_reach.start(),
                "message": "FORBIDDEN (Lesson 46): Reaching hand toward camera/lens blocks the frame and causes camera materialization."
            })

    return issues


def lint_prompt(prompt: str) -> list[dict]:
    """Check prompt against FlowKit rules. Supports both plain text and JSON structured prompts."""
    is_json, json_obj = is_json_prompt(prompt)
    if is_json:
        if json_obj is None:
            return [{
                "severity": "CRITICAL",
                "type": "MALFORMED_JSON",
                "message": "Prompt appears to be JSON but failed to parse with json.loads."
            }]
        return lint_json_prompt(json_obj)

    issues = []
    p_lower = prompt.lower()

    # 1. Check Ghost Device patterns
    for pat, msg in FORBIDDEN_GHOST_DEVICE_PATTERNS:
        matches = list(re.finditer(pat, p_lower))
        if matches:
            for m in matches:
                issues.append({
                    "severity": "CRITICAL",
                    "type": "GHOST_DEVICE",
                    "token": m.group(0),
                    "position": m.start(),
                    "message": msg
                })

    # 2. Check Optical Viewpoint: If selfie/front lens, check if off-screen constraint exists
    if "selfie" in p_lower or "front-lens" in p_lower or "vlog" in p_lower:
        if not ("off-screen" in p_lower or "outside the visible frame" in p_lower or "outside the frame" in p_lower):
            issues.append({
                "severity": "HIGH",
                "type": "OPTICAL_VIEWPOINT",
                "message": "Selfie shot is missing explicit camera blind-spot constraint: 'the camera lens itself and her right gripping hand are completely outside the visible frame and never seen'."
            })
        if not ("empty" in p_lower and "hand" in p_lower):
            issues.append({
                "severity": "MEDIUM",
                "type": "FREE_HAND_CONSTRAINT",
                "message": "Selfie shot should specify that the free hand is completely empty ('her free left hand is completely empty and flails naturally')."
            })

    # 3. Check Body Lock Early Conditioning
    if "body lock" in p_lower:
        pos_body_lock = p_lower.find("body lock")
        m_timed = re.search(r"\b0-[1-3]s:", p_lower)
        if m_timed and m_timed.start() < pos_body_lock:
            issues.append({
                "severity": "HIGH",
                "type": "BODY_LOCK_POSITION",
                "message": "BODY LOCK is placed AFTER timed action segments (0-2s/0-3s). Rule 39 requires BODY LOCK placed EARLY right after Shot: before timed segments to prevent attention decay."
            })

    # 4. Check Camera Touch / Lens Blocking (Lesson 46)
    if "selfie" in p_lower or "front-lens" in p_lower:
        m_reach = re.search(r"\b(?:reaches?|extends?|brings?)\s+(?:her|his|their)?\s*(?:free\s*)?(?:hand|arm)\s+toward\s+(?:the\s+)?(?:camera|lens|screen)\b", p_lower)
        if m_reach:
            issues.append({
                "severity": "CRITICAL",
                "type": "CAMERA_TOUCH_GLITCH",
                "token": m_reach.group(0),
                "position": m_reach.start(),
                "message": "FORBIDDEN (Lesson 46): Reaching hand toward camera/lens blocks the frame and causes camera materialization. Character must never reach toward or touch the camera lens."
            })
        if not ("never reaches toward" in p_lower or "never touches" in p_lower or "never covers" in p_lower):
            issues.append({
                "severity": "MEDIUM",
                "type": "CAMERA_TOUCH_CONSTRAINT",
                "message": "Selfie shot should specify explicit camera touch prohibition: 'she never reaches toward, touches, covers, or points at the camera lens'."
            })

    # 5. Check Functional Prop Dressing (Lesson 46 / Rule 45)
    if any(k in p_lower for k in ["mitten", "glove", "parka", "cloak", "goggles"]) and any(k in p_lower for k in ["ties", "gives", "hands", "fastens", "slips"]):
        has_dressing_verb = any(v in p_lower for v in ["slips", "slides", "pulls over", "fits over", "wears", "wearing"])
        if not has_dressing_verb:
            issues.append({
                "severity": "HIGH",
                "type": "INDIRECT_PROP_DESCRIPTION",
                "message": "Prop/clothing interaction detected, but missing direct functional dressing verbs ('slips and slides directly onto', 'fits securely over', 'wearing'). Simply tying cords or handing props causes AI to omit actual dressing."
            })

    return issues


def clean_prompt_of_ghost_devices(prompt: str) -> str:
    """Automatically cleans ghost device keywords from a prompt."""
    cleaned = prompt
    cleaned = re.sub(r"\bnever drops the phone\b", "never drops the camera", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\bnever drops, releases, or lets go of the phone\b", "never drops, releases, or lets go of the camera", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\bsmartphone footage\b", "handheld footage", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\braw unstabilized smartphone footage\b", "raw unstabilized footage", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\bnatural smartphone perspective\b", "natural wide-angle handheld perspective", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\bphone\b", "camera", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\bsmartphone\b", "camera", cleaned, flags=re.IGNORECASE)
    return cleaned


def run_json_prompt_tests():
    """Built-in test suite for JSON structured prompts."""
    print("Running JSON Prompt Linter Test Suite...")

    # Test 1: Valid clean JSON prompt (Scene 27 format)
    valid_json = {
        "camera": {
            "type": "over-the-shoulder handheld tracking shot",
            "position": "chest level behind Nora's right shoulder looking toward the Chief",
            "framing": "Nora right foreground, Chief center midground beside hearth"
        },
        "setting": {
            "location": "Pech de l'Aze limestone cave hearth workspace",
            "elements": [
                "circular stone hearth with glowing red-orange oak embers",
                "dried red deer pelt pad on flat cave stone floor",
                "large faceted black Levallois flint core on pelt pad",
                "rounded quartzite hammerstone held bare-handed"
            ]
        },
        "characters": [
            {
                "name": "Nora",
                "visual_lock": "matches Nora face and Nora Body reference images",
                "outfit": "golden-tan deer suede tunic, dark corset belt, high blonde ponytail",
                "action": "observes flint knapping intently from right foreground"
            },
            {
                "name": "Neanderthal Chief",
                "visual_lock": "matches Leader reference image",
                "outfit": "draped untailored deer pelts, bare muscular shoulders",
                "position": "seated cross-legged on deer pelt pad"
            }
        ],
        "timeline_action": {
            "0-3s": "Chief turns the faceted black flint core with both hands inspecting platform angle while Nora watches.",
            "3-6s": "Chief raises quartzite hammerstone in right hand hovering precisely above platform.",
            "6-8s": "Chief locks elbows preparing for final strike while Nora watches his hand position with admiration."
        },
        "speech": {
            "speaker": "Nora",
            "voice_profile": "Laomedeia conversational energetic vlog delivery",
            "dialogue": "The Leader is pulling out a massive black flint nodule from the hearth side. Watch his hand position—this is pure prehistoric engineering!"
        },
        "negative_constraints": [
            "the camera lens itself and her gripping hand are completely outside the visible frame and never seen",
            "strictly no wooden handle on hammerstone, bare-handed only",
            "no modern tools or devices",
            "no subtitles, no text on screen, no watermark",
            "no morphing or vanishing characters"
        ]
    }

    issues_valid = lint_prompt(json.dumps(valid_json, indent=2))
    assert len(issues_valid) == 0, f"Expected 0 issues for valid JSON, got: {issues_valid}"
    print("  [PASS] Test 1: Valid JSON prompt passed cleanly with 0 issues.")

    # Test 2: JSON with Ghost Device ('phone' mentioned)
    invalid_ghost_json = json.loads(json.dumps(valid_json))
    invalid_ghost_json["timeline_action"] = {
        "0-3s": "Nora checks her phone screen while Chief works."
    }
    issues_ghost = lint_prompt(json.dumps(invalid_ghost_json))
    ghost_types = [iss["type"] for iss in issues_ghost]
    assert "GHOST_DEVICE" in ghost_types, f"Expected GHOST_DEVICE issue, got: {ghost_types}"
    print("  [PASS] Test 2: Ghost device ('phone') successfully caught in JSON prompt.")

    # Test 3: JSON with Camera Touch Glitch
    invalid_touch_json = json.loads(json.dumps(valid_json))
    invalid_touch_json["camera"] = {"type": "selfie front-lens shot"}
    invalid_touch_json["timeline_action"] = {
        "0-3s": "Nora reaches her free hand toward the camera lens to adjust it."
    }
    issues_touch = lint_prompt(json.dumps(invalid_touch_json))
    touch_types = [iss["type"] for iss in issues_touch]
    assert "CAMERA_TOUCH_GLITCH" in touch_types, f"Expected CAMERA_TOUCH_GLITCH, got: {touch_types}"
    print("  [PASS] Test 3: Camera touch glitch successfully caught in JSON prompt.")

    # Test 4: JSON missing required schema keys
    invalid_schema_json = {"camera": {"type": "wide"}}
    issues_schema = lint_prompt(json.dumps(invalid_schema_json))
    schema_types = [iss["type"] for iss in issues_schema]
    assert "JSON_SCHEMA_MISSING_KEY" in schema_types, f"Expected JSON_SCHEMA_MISSING_KEY, got: {schema_types}"
    print("  [PASS] Test 4: Missing schema keys successfully caught.")

    print("\nAll JSON Prompt Linter Tests PASSED! 🎉")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lint video prompts for FlowKit rules")
    parser.add_argument("prompt", nargs="?", help="Prompt string to lint")
    parser.add_argument("--scene", help="Scene ID from DB to lint")
    parser.add_argument("--file", help="Path to JSON or text file containing prompt to lint")
    parser.add_argument("--auto-fix", action="store_true", help="Auto-fix ghost device tokens in DB scene")
    parser.add_argument("--test-json", action="store_true", help="Run JSON prompt test suite")
    args = parser.parse_args()

    if args.test_json:
        run_json_prompt_tests()
        sys.exit(0)

    prompt_to_check = args.prompt
    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                prompt_to_check = f.read()
        except Exception as e:
            print(f"Error reading file {args.file}: {e}")
            sys.exit(1)
    elif args.scene:
        conn = sqlite3.connect("flow_agent.db")
        row = conn.execute("SELECT video_prompt FROM scene WHERE id = ?", (args.scene,)).fetchone()
        if not row or not row[0]:
            print(f"Scene {args.scene} not found or has no video_prompt.")
            sys.exit(1)
        prompt_to_check = row[0]

    if not prompt_to_check:
        print("Usage: python tools/lint_prompt.py \"<prompt>\" OR --file <path> OR --scene <scene_id> OR --test-json")
        sys.exit(0)

    issues = lint_prompt(prompt_to_check)
    if not issues:
        print("✅ PROMPT LINT PASSED! No ghost devices or viewpoint issues found.")
    else:
        print(f"⚠️ FOUND {len(issues)} ISSUES:")
        for idx, iss in enumerate(issues, 1):
            print(f"  [{idx}] [{iss['severity']}] {iss['type']}: {iss['message']}")

        if args.auto_fix and args.scene:
            fixed = clean_prompt_of_ghost_devices(prompt_to_check)
            conn = sqlite3.connect("flow_agent.db")
            conn.execute("UPDATE scene SET video_prompt = ? WHERE id = ?", (fixed, args.scene))
            conn.commit()
            print("\n✨ Auto-fixed prompt saved to DB!")
