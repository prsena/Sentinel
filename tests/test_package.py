"""
Environment sanity checks for Sentinel.
"""

import sys

def test_python_version_is_supported() -> None:
    # Sentinel targets Python 3.11 or newer
    assert sys.version_info >= (3, 11)

def test_src_package_is_importable() -> None:
    # The pytest configuration should make 'src' importable from the repo root
    import src
    assert src.__doc__ is not None