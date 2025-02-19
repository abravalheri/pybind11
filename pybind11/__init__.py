import sys

if sys.version_info < (3, 5):
    msg = "pybind11 does not support Python < 3.5. 2.9 was the last release supporting older Pythons."
    raise ImportError(msg)


from ._version import __version__, version_info
from .commands import get_cmake_dir, get_include

__all__ = (
    "version_info",
    "__version__",
    "get_include",
    "get_cmake_dir",
)
