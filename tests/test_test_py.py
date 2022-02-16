"""Test module for test_py module."""
from pytest import CaptureFixture

import test_py


def test_my_function(capsys: CaptureFixture) -> None:
    """Test test_py.my_function."""
    test_py.my_function()
    captured = capsys.readouterr()
    assert captured.out == "Hello World\n"
