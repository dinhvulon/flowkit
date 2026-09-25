"""Unit tests for FlowKit watermark removal and SynthID disruption service."""

import numpy as np
import pytest

from agent.services.watermark import (
    VIDEO_ALPHA_SCALE,
    detect_watermark_config,
    disrupt_synthid_signal,
    get_alpha_map,
    remove_watermark_image,
    remove_watermark_yuv_frame,
)


def test_detect_watermark_config_720x1280():
    """Verify watermark anchor coordinates for standard 720x1280 resolution."""
    config = detect_watermark_config(720, 1280, is_video=True)
    assert config["logo_size"] == 48
    assert config["x"] == 576
    assert config["y"] == 1136


def test_detect_watermark_config_1080x1920():
    """Verify watermark scales proportionally for 1080x1920 upscaled resolution."""
    config = detect_watermark_config(1080, 1920, is_video=True)
    assert config["logo_size"] == 72
    assert config["x"] == 864
    assert config["y"] == 1704


def test_alpha_map_caching_and_bounds():
    """Alpha map must be float32 in [0, 1] range and cached properly."""
    alpha_48 = get_alpha_map(48)
    assert alpha_48.shape == (48, 48)
    assert alpha_48.dtype == np.float32
    assert 0.0 <= alpha_48.min() <= alpha_48.max() <= 1.0

    # Ensure cache returns identical object
    assert get_alpha_map(48) is alpha_48


def test_disrupt_synthid_signal():
    """SynthID signal disruption preserves plane dimensions and uint8 dtype."""
    plane = np.full((100, 100), 128, dtype=np.uint8)
    disrupted = disrupt_synthid_signal(plane)
    assert disrupted.shape == (100, 100)
    assert disrupted.dtype == np.uint8
    # Not identical due to gaussian noise, but near original mean
    assert abs(float(disrupted.mean()) - 128.0) < 5.0


def test_remove_watermark_yuv_frame():
    """remove_watermark_yuv_frame processes a full YUV420p buffer without errors."""
    w, h = 720, 1280
    y_size = w * h
    uv_size = (w // 2) * (h // 2)
    total_bytes = y_size + 2 * uv_size

    fake_yuv = np.full(total_bytes, 128, dtype=np.uint8).tobytes()
    config = detect_watermark_config(w, h, is_video=True)

    result_bytes = remove_watermark_yuv_frame(fake_yuv, w, h, config)
    assert len(result_bytes) == total_bytes


def test_remove_watermark_image_roundtrip(tmp_path):
    """Test removing watermark from a synthetic image file."""
    import cv2

    img_path = str(tmp_path / "test_frame.png")
    out_path = str(tmp_path / "test_frame_clean.png")

    w, h = 720, 1280
    img = np.full((h, w, 3), 100, dtype=np.uint8)

    # Simulate watermark glyph
    config = detect_watermark_config(w, h, is_video=False)
    x, y, size = config["x"], config["y"], config["logo_size"]
    alpha = get_alpha_map(size)
    for c in range(3):
        img[y:y + size, x:x + size, c] = np.clip(
            alpha * 255 + (1 - alpha) * img[y:y + size, x:x + size, c], 0, 255
        ).astype(np.uint8)

    cv2.imwrite(img_path, img)

    cleaned_file = remove_watermark_image(img_path, out_path)
    assert cleaned_file == out_path

    cleaned_img = cv2.imread(out_path)
    assert cleaned_img is not None
    assert cleaned_img.shape == (h, w, 3)
