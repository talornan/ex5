from GameModel import GameModel
from GameView import GameView




class GameController(object):
    """
        controller of the game, this class contains the model of the game- algorithem & communication
        and the view - the gui logic. this class in use in order to use the mvs design pattern
    """
    def __init__(self):
        self.game_model = GameModel()
        self.game_view = GameView(self.game_model.graph)

    def execute_game(self):
        self.game_model.init_game()
        while self.game_model.client.is_running() == 'true':
            self.game_model.runAndUpdate()
            res = self.game_view.show_all(self.game_model.agents, self.game_model.pokemons, self.game_model.graph, self.game_model.game_info)
            if res == False:
                self.game_model.client.stop_connection()
                return
            print(self.game_model.client.time_to_end(),  self.game_model.client.get_info())




