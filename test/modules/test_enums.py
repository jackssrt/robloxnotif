from modules import enums as e


def test_PresenceType():
    assert len(e.PresenceType) == 4
    assert e.PresenceType.Offline.value == "0"
    assert e.PresenceType.Online.value == "1"
    assert e.PresenceType.Playing.value == "2"
    assert e.PresenceType.InStudio.value == "3"
