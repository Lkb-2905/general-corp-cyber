import subprocess
import sys
from pathlib import Path


def run(cmd: list[str], cwd: Path) -> None:
    result = subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True)
    assert result.returncode == 0


def test_demo_runs() -> None:
    repo = Path(__file__).resolve().parents[1]
    run(
        [sys.executable, str(repo / "01-keylogger-educatif" / "keylogger.py"), "--demo", "--output", "keys.demo.log"],
        cwd=repo / "01-keylogger-educatif",
    )
    run(
        [sys.executable, str(repo / "02-steganography-tool" / "stegano.py"), "--demo"],
        cwd=repo / "02-steganography-tool",
    )
    run(
        [sys.executable, str(repo / "04-exif-analyseur" / "exif_reader.py"), "--demo"],
        cwd=repo / "04-exif-analyseur",
    )
    run(
        [sys.executable, str(repo / "05-encrypted-chat" / "server.py"), "--demo"],
        cwd=repo / "05-encrypted-chat",
    )
    run(
        [sys.executable, str(repo / "05-encrypted-chat" / "client.py"), "--demo"],
        cwd=repo / "05-encrypted-chat",
    )
