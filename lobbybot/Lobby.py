import uuid
from Game import Game


class Lobby:
    def __init__(self, game: Game):
        self.players: list = []
        self.game = game
        self.lobby_uuid = uuid.uuid4()
