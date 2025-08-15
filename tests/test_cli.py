import subprocess
import sys
import pytest


@pytest.mark.parametrize(
    "name,expected",
    [
        ("Alice", "Hello Alice!"),
        ("Bob", "Hello Bob!"),
        ("", "Hello !"),
    ],
)
def test_greet_cli(name, expected):
    result = subprocess.run(
        [sys.executable, "-m", "demo_python_package.cli", "--name", name],
        capture_output=True,
        text=True,
        check=True,
    )
    assert expected in result.stdout
