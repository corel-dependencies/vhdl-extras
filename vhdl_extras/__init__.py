import importlib.metadata
from typing import Optional

from tsfpga.module_list import ModuleList
from corel_modules.module.sysutils import get_modules
from . import extras, extras_2008

__version__ = importlib.metadata.version(__package__ or __name__)

def get_hdl_modules(
    names_include: Optional[set[str]] = None, names_avoid: Optional[set[str]] = None
) -> "ModuleList":

    return get_modules(
        pymodules = [extras, extras_2008],
        names_include=names_include,
        names_avoid=names_avoid
    )
