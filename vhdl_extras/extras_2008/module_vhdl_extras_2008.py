#!/usr/bin/env python3

from pathlib import Path
from tsfpga.module import BaseModule
from tsfpga.hdl_file import HdlFile# as BaseHdlFile
from typing import TYPE_CHECKING, Any, Callable, Iterable, Optional, Union
from hdl_registers.register import Register

# class HdlFile(BaseHdlFile):
#     vhdl_file_ending = ('.vhd', '.vhdl')
#     file_endings = (
#         vhdl_file_ending,
#         BaseHdlFile.verilog_source_file_ending,
#         BaseHdlFile.verilog_header_file_ending)


class Module(BaseModule):

    def __init__(
        self, path: Path, library_name: str, default_registers: Optional[list[Register]] = None
    ):
        super().__init__(path=Path(__file__).parent.resolve(), library_name='extras_2008')

    def get_synthesis_files(self, files_include=None, files_avoid=None, **kwargs):
        folders = [
            self.path / "../../rtl/extras_2008",
        ]

        return [
            HdlFile(file_path)
            for file_path in self._get_file_list(
                    folders=folders,
                    file_endings=('.vhd', 'vhdl'),
                    files_include=files_include,
                    files_avoid=files_avoid,
            )
            ]

if __name__ == "__main__":
    m = Module()
    print(m.get_synthesis_files())
