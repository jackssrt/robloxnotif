from modules import classes as c
from dataclasses import fields


class TestPresence:
    def test___init__(self):
        a = c.Presence(1, "A", 2, 3, "B", 4, 5, "C")
        assert a.userPresenceType == 1
        assert a.lastLocation == "A"
        assert a.placeId == 2
        assert a.rootPlaceId == 3
        assert a.gameId == "B"
        assert a.universeId == 4
        assert a.userId == 5
        assert a.lastOnline == "C"

    def test___eq__(self):
        a = c.Presence(1, "A", 2, 3, "B", 4, 5, "C")
        b = c.Presence(1, "A", 2, 3, "B", 4, 5, "C")
        assert a == b
        b = c.Presence(1, "A", 2, 3, "B", 4, 5, "D")
        assert a == b
        b = c.Presence(2, "A", 2, 3, "B", 4, 5, "C")
        assert a != b
        b = c.Presence(1, "B", 2, 3, "B", 4, 5, "C")
        assert a != b


class TestApiError:
    def test___init__(self):
        a = c.ApiError(0, "A", "B")
        assert a.code == 0
        assert a.message == "A"
        assert a.userFacingMessage == "B"


class TestConfig:
    def test___init__(self):
        a = c.Config({"0": "testing...", "3": "testing."}, True, "haha yeah no")
        assert a.usernames.get("0") == "testing..."
        assert a.usernames.get("3") == "testing."
        assert a.loggedIn == True
        assert a.cookie == "haha yeah no"
