from modules import utils as u
import pytest


def test_loadJson():

    with pytest.raises(FileNotFoundError):
        assert u.loadJson("./test/modules/testJsons/doesntExist.json")
        assert u.loadJson("./testJsons")
    assert u.loadJson(
        "./test/modules/testJsons/comments.jsonc")["test"] == "testing"
    assert u.loadJson(
        "./test/modules/testJsons/withoutcomments.json")["test"] == "testing"


def test_loadConfig():
    x = u.loadConfig("./test/modules/testJsons/c.jsonc", "./test")
    assert x.loggedIn == False
    assert x.usernames == {"0": "name"}
    x = u.loadConfig("./test/modules/testJsons/c.jsonc",
                     "./test/modules/testJsons/r.jsonc")
    assert x.loggedIn == True
    assert x.usernames == {"0": "name"}
    assert x.cookie == "testing..."
