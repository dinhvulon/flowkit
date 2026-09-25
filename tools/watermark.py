"""Re-export watermark removal functions from agent.services.watermark."""

import os
import sys

# Ensure flowkit root is in sys.path
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from agent.services.watermark import (
    ALPHA_THRESHOLD,
    MAX_ALPHA,
    LOGO_VALUE,
    VIDEO_ALPHA_SCALE,
    SYNTHID_DISRUPT_STRENGTH,
    SYNTHID_BLUR_RADIUS,
    _load_alpha_map,
    get_alpha_map,
    disrupt_synthid_signal,
    detect_watermark_config,
    _match_watermark,
    locate_watermark_consensus,
    locate_watermark_image,
    _edge_band_mask,
    remove_watermark_yuv_frame,
    remove_watermark_video,
    remove_watermark_image,
)

__all__ = [
    "ALPHA_THRESHOLD",
    "MAX_ALPHA",
    "LOGO_VALUE",
    "VIDEO_ALPHA_SCALE",
    "SYNTHID_DISRUPT_STRENGTH",
    "SYNTHID_BLUR_RADIUS",
    "get_alpha_map",
    "disrupt_synthid_signal",
    "detect_watermark_config",
    "locate_watermark_consensus",
    "locate_watermark_image",
    "remove_watermark_yuv_frame",
    "remove_watermark_video",
    "remove_watermark_image",
]
