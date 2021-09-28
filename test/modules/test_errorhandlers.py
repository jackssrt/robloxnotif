import traceback
import pytest
from modules import errorhandlers as e
from inspect import signature


def test_num_args():
    t = [e.logError, e.logErrorWarn, e.handleMainLoopError, e.corruptedJson]
    for x in t:
        s = signature(x)
        assert len(s.parameters) == 2
    s = signature(e.handleUnexpectedError)
    assert len(s.parameters) == 1
