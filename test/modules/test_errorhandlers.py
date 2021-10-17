from typing import Callable
from modules import errorhandlers as e
from inspect import signature


def test_num_args():
    t: list[Callable] = [e.logError, e.logErrorWarn,
                         e.corruptedJson, e.handleApiError]
    for x in t:
        s = signature(x)
        assert len(s.parameters) == 2
    t = [e.handleUnexpectedError, e.handleMainLoopError]
    for x in t:
        s = signature(x)
        assert len(s.parameters) == 1
