import pytest
from modules import console as c
from inspect import signature
from datetime import datetime


class TestConsole:
    def test_num_args(self, capfd):
        t = [c.log, c.error, c.warn]
        for x in t:
            s = signature(x)
            assert len(s.parameters) == 2

    def test_error_out(self, capfd: pytest.CaptureFixture):
        test_str = "Testing..."
        now = datetime.now().strftime("%X")
        c.error(None, test_str)
        out, err = capfd.readouterr()
        assert "[ERROR]" in out
        assert test_str in out
        assert f"[{now}]:" in out

    def test_warn_out(self, capfd: pytest.CaptureFixture):
        test_str = "Testing..."
        now = datetime.now().strftime("%X")
        c.warn(None, test_str)
        out, err = capfd.readouterr()
        assert "[WARN]" in out
        assert test_str in out
        assert f"[{now}]:" in out

    def test_log_out(self, capfd: pytest.CaptureFixture):
        test_str = "Testing..."
        now = datetime.now().strftime("%X")
        c.error(None, test_str)
        out, err = capfd.readouterr()
        assert test_str in out
        assert f"[{now}]:" in out
