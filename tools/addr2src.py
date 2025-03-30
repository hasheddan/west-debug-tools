import os
import importlib
import importlib.util
import sys

ZCMAKE_PATH = "scripts/west_commands/zcmake.py"


def addr2src(topdir, zephyr_base, address):
    spec = importlib.util.spec_from_file_location(
        "zcmake",
        os.path.join(topdir, zephyr_base, ZCMAKE_PATH),
    )
    zcmake = importlib.util.module_from_spec(spec)
    sys.modules["zcmake"] = zcmake
    spec.loader.exec_module(zcmake)
    cache = zcmake.CMakeCache.from_build_dir("build")
    return (
        [cache.get("CMAKE_GDB")]
        + ["-q"]
        + [cache.get("BYPRODUCT_KERNEL_ELF_NAME")]
        + ["-ex", f"list *{address}"]
        + ["-ex", "quit"]
    )
