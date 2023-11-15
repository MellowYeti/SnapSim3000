from dataclasses import dataclass
from enum import Enum
from itertools import product


class CardFace(Enum):
    SPADES = "SPADES"
    HEARTS = "HEARTS"
    CLUBS = "CLUBS"
    DIAMONDS = "DIAMONDS"


class CardValue(Enum):
    ACE = "ONE"
    TWO = "TWO"
    THREE = "THREE"
    FOUR = "FOUR"
    FIVE = "FIVE"
    SIX = "SIX"
    SEVEN = "SEVEN"
    EIGHT = "EIGHT"
    NINE = "NINE"
    TEN = "TEN"
    JACK = "JACK"
    QUEEN = "QUEEN"
    KING = "KING"


@dataclass(frozen=True)
class Card:
    face: CardFace
    value: CardValue

    def __repr__(self) -> str:
        return f"{self.value.value} of {self.face.value}"


class Deck(list):
    def __init__(self):
        super().__init__()
        for face, value in product(CardFace, CardValue):
            self.append(Card(face, value))
