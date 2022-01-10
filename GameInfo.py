import json

class GameInfo(object):
    
"""
        this object present  the game info  in the game.
        this class is in use in order to simplify the the use in the json that return from the client
    """
    def __init__(self, info_json_str, time_remaning):
        """
        returns the current game info. for example:\n
        {
            "GameServer":{
                "pokemons" : 1,
                "is_logged_in":false,
                "moves":1,
                "grade":0,
                "game_level":0,
                "max_user_level":-1,
                "id":0,
                "graph":"data/A0",
                "agents":1
            }
        }
        """

        game_json = json.loads(info_json_str)["GameServer"]
        self.num_of_poks = game_json["pokemons"]
        self.is_logged_in = game_json["is_logged_in"]
        self.moves = game_json["moves"]
        self.grade = game_json["grade"]
        self.game_level = game_json["game_level"]
        self.max_user_level = game_json["max_user_level"]
        self.id = game_json["id"]
        self.graph = game_json["graph"]
        self.agents = game_json["agents"]
        self.time_remaining = time_remaning

