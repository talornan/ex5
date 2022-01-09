import json

from graph.GeoLocation import GeoLocation
from graph.GraphAlgo import GraphAlgo


class Pokemon(object):
    """
        this object preset the pokemons in the game.
        this class is in use in order to simplify  the use in the json that return from the client
    """
    def __init__(self, pokemon, graph):

        self.value = pokemon["value"]
        pos = pokemon["pos"].split(",")
        x = float(pos[0])
        y = float(pos[1])
        z = float(pos[2])
        self.pos = (x,y,z)
        self.type = pokemon["type"]
        self.edge = self.getEdge(graph)
        self.src = self.edge[0]
        self.dest = self.edge[1]


    def getEdge(self,graph):
        """
        src < dest => type > 0\n
        dest < src => type < 0\n
        :param graph:
        :return:
        """
        edge = graph.getEdgePointIsOn(self.pos)
        src = edge[0]
        dest = edge[1]
        if self.type > 0 and src > dest:
            return (dest,src)
        elif self.type < 0 and dest > src:
            return (dest,src)
        return edge

class Pokemons(object):
    """
        simple wrapper to pokemons list
        this class is in use in order to simplify  the use in the json that return from the client
    """

    def __init__(self, pokemons_json_str, graph):
        if type(pokemons_json_str) is str:

            self.pokemons = []
            pokemons_json = json.loads(pokemons_json_str)
            if type(pokemons_json) is not int and type(pokemons_json["Pokemons"]) is not int:
                for pokemon in pokemons_json["Pokemons"]:
                    self.pokemons.append(Pokemon(pokemon["Pokemon"], graph))



