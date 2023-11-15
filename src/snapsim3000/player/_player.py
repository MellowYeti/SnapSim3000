from dataclasses import dataclass


@dataclass(frozen=True)
class SnapResult:
    snap: bool
    player: object


class Player:
    def __init__(self, name: str):
        self._name = name
        self._hand = []
        self._last_played_card = None
        self._score = 0

    @property
    def name(self):
        return self._name

    @property
    def score(self):
        return self._score

    def take_card(self, card):
        self._hand.append(card)

    def play_card(self):
        return self._hand.pop()

    async def check_for_snap(self, card):
        if not self._last_played_card:
            self._last_played_card = card
            return SnapResult(False, self)

        if (
            self._last_played_card.face == card.face
            or self._last_played_card.value == card.value
        ):
            self._last_played_card = None
            return SnapResult(True, self)

        self._last_played_card = card
        return SnapResult(False, self)

    def add_score(self, score):
        self._score += score
