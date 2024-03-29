import dataclasses
from typing import Dict


@dataclasses.dataclass(eq=True)
class Presence:
    userPresenceType: int
    lastLocation: str
    placeId: int
    rootPlaceId: int
    gameId: str
    universeId: int
    userId: int
    lastOnline: str = dataclasses.field(compare=False)


@dataclasses.dataclass
class ApiError:
    code: int
    message: str
    userFacingMessage: str


@dataclasses.dataclass
class Config:
    usernames: Dict[str, str]
    loggedIn: bool
    cookie: str
