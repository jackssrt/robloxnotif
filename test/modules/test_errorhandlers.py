from inspect import signature
from typing import Callable, List

from modules import errorhandlers as e


def test_num_args():
    t: List[Callable] = [e.logError, e.logErrorWarn, e.corruptedJson, e.handleApiError]
    for x in t:
        s = signature(x)
        assert len(s.parameters) == 2
    t = [e.handleUnexpectedError, e.handleMainLoopError]
    for x in t:
        s = signature(x)
        assert len(s.parameters) == 1
