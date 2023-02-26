from Lobby import Lobby


class LobbyManager:
    def __init__(self):
        self.lobbies: dict = {}

    def create_lobby(self, game, num_players):
        if game not in self.lobbies:
            self.lobbies[game] = []

        self.lobbies[game].append(Lobby(num_players=num_players))
        response = f"Creating lobby for <{game}> with party size <{num_players}>."
        return response

    def get_lobby_index(self, game, lobby_uuid=None):
        if game not in self.lobbies:
            return -1

        if lobby_uuid:
            return next((i for i, lobby in enumerate(self.lobbies) if lobby.lobby_uuid is lobby_uuid), -1)

        return 0

    def add_player(self, game, player, lobby_uuid=None):
        if game not in self.lobbies:
            raise RuntimeError("No lobby created for this game.")

        lobby_index = self.get_lobby_index(game, lobby_uuid)
        lobby_players = self.lobbies[game][lobby_index].players
        lobby_num_players = self.lobbies[game][lobby_index].num_players
        lobby_uuid = self.lobbies[game][lobby_index].lobby_uuid

        lobby_players.append(player)
        lobby_num_players -= 1

        self.lobbies[game][lobby_index].players = lobby_players
        self.lobbies[game][lobby_index].num_players = lobby_num_players

        response = f"Added <{player}> to {game} lobby. {lobby_num_players} spots remaining."
        return response
