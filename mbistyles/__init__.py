"""Matplotlib styles inspired by the MBI design.

The styles select the light weight of Fira Sans by its family name
``Fira Sans Light``. matplotlib >= 3.11 registers the light font files under
this name, while older versions only register them as ``Fira Sans`` of the
weight 300. Hence, the light font files are also registered as ``Fira Sans
Light`` here, which runs on ``import mbistyles`` and on the first use of a
style, e.g. ``plt.style.use("mbistyles.base")``.
"""

import dataclasses

from matplotlib import font_manager

FAMILY = "Fira Sans"
LIGHT_FAMILY = "Fira Sans Light"


def _register_light_family():
    """Register the light font files of ``FAMILY`` also as ``LIGHT_FAMILY``
    of regular weight, if matplotlib does not know this family."""
    entries = font_manager.fontManager.ttflist
    if any(entry.name == LIGHT_FAMILY for entry in entries):
        return
    light = [
        dataclasses.replace(entry, name=LIGHT_FAMILY, weight=400)
        for entry in entries
        if entry.name == FAMILY and entry.weight == 300
    ]
    if light:
        entries.extend(light)
        # former lookups may have cached the fallback font
        font_manager.FontManager._findfont_cached.cache_clear()


_register_light_family()
