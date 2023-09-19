import hashlib
import os
import subprocess
from pathlib import Path

import portalocker


def assert_command_executed(cmd: str):
    cmd_id = hashlib.md5(cmd.encode()).hexdigest()
    lock_path = Path(f"/tmp/{cmd_id}.lock")
    ok_path = Path(f"/tmp/{cmd_id}.ok")

    with portalocker.Lock(lock_path, timeout=60):
        if os.path.exists(ok_path):
            return
        print(f"{cmd} not executed yet, executing now")
        subprocess.run(["/bin/bash", "-c", cmd], check=True)
        ok_path.touch()


def assert_pip_packages_installed(packages: list[str]):
    assert_command_executed(f'pip install {" ".join(packages)}')


def assert_sage_pip_packages_installed(packages: list[str]):
    assert_command_executed(f'sage -pip install {" ".join(packages)}')


def assert_apt_packages_installed(packages: list[str]):
    assert_command_executed(
        f'apt-get update && apt-get install -y {" ".join(packages)}'
    )
