from GameInfo import GameInfo
from agent import Agents
from client import Client
from graph.GraphAlgo import GraphAlgo
from pokemon import Pokemons
import json
import time

class Game(object):
    # default port
    PORT = 6666
    # server host (default localhost 127.0.0.1)
    HOST = '127.0.0.1'

    def __init__(self,):
        self.client = Client()
        self.client.start_connection(self.HOST, self.PORT)
        self.game_info = GameInfo(self.client.get_info())
        self.graphAlgo = GraphAlgo()
        self.graphAlgo.load_graph_from_json(json.loads(self.client.get_graph()))
        self.graph = self.graphAlgo.get_graph()
        self.pokemons = Pokemons(self.client.get_pokemons(), self.graph)
        self.action = {}
        self.last_algorithem_run = -1

    def runAndUpdate(self):
        self.update()
        if self.last_algorithem_run == -1 or time.time()*1000 - self.last_algorithem_run > 100:
            actions = self.algorithem()
            self.updateClientMovement(actions)
            self.last_algorithem_run = time.time()*1000



    def init_game(self):
        poks = self.pokemons.pokemons
        poks.sort(key=lambda x: x.value, reverse=True)
        for i in range(self.game_info.agents):
            node = poks[i].edge[0]
            assignment_json = json.dumps({"id" : node})
            print("node " +str(poks[i].edge))
            self.client.add_agent(str(assignment_json))

        self.client.start()


    def update(self):
        self.agents = Agents(self.client.get_agents())
        self.pokemons = Pokemons(self.client.get_pokemons(), self.graph)
        self.game_info = GameInfo(self.client.get_info())

    def algorithem(self):
        agents_move = {}
        assign_agent = set()
        assign_pokemons = set()
        agents = [agent for agent in self.agents.agents if agent.isMoving() == False]
        agents_assign_edge = {agent.edge for agent in self.agents.agents if agent.isMoving() == True}

        pokemon_agents_not_already_assign_to = [pokemon for pokemon in self.pokemons.pokemons if pokemon.edge not in agents_assign_edge ]
        assign_pokemons = {pokemon for pokemon in self.pokemons.pokemons if pokemon.edge in agents_assign_edge }

        #remove pokemon where agents already assign to thir edge

        # check if there are pkemons is 2 edge distance or less then
        distance = {}
        #(agent_id, pokemon_id) -> path
        one_step_distance = {}
        pokemon_distance_from_agent = {}

        if len(agents) == 0:
            return {}

        for agent in agents:
            for pokemon in pokemon_agents_not_already_assign_to:
                pokemon_target = pokemon.src if agent.src != pokemon.src else pokemon.dest
                path = self.graphAlgo.shortest_path(agent.src, pokemon_target)[1]
                print("path from shortest  path for " +str(agent.src)+ " dest " + str(pokemon.src))
                print(path)

                # meaning only one hop since the first is the current node
                if len(path) <= 2:
                    if agent.id in one_step_distance:
                        one_step_distance[agent.id].append((pokemon, pokemon_target))
                    else:
                        one_step_distance[agent.id] =[(pokemon, pokemon_target)]
                #distance[(agent.id, pokemon.id)] =  (path, pokemon,agent)

                if pokemon in pokemon_distance_from_agent:
                    pokemon_distance_from_agent[pokemon].append((path, pokemon,agent))
                else :
                    pokemon_distance_from_agent[pokemon]= [(path, pokemon,agent)]

        for agent, pokemons in one_step_distance.items():
            pokemons.sort(key=lambda x: x[0].value, reverse=True)
            agents_move[agent] = pokemons[0][1]
            assign_agent.add(agent)
            assign_pokemons.add(pokemons[0])


        pokemon_agents_not_already_assign_to = [pokemon for pokemon in pokemon_agents_not_already_assign_to if pokemon not in assign_pokemons]
        pokemon_agents_not_already_assign_to.sort(key=lambda x: x.value, reverse=True)
        for pokemon in pokemon_agents_not_already_assign_to:
            data = pokemon_distance_from_agent[pokemon]
            data.sort(key=lambda x: len(x[0]) / x[2].speed, reverse=True)
            data = [elem for elem in data if elem[2] not in assign_agent]
            if len(data) > 0:
                (path, pokemon, agent) = data[0]
                print(path)
                agents_move[agent.id] = path[1] # target node
                assign_agent.add(agent)
                assign_pokemons.add(pokemon)
                for pk in pokemon_agents_not_already_assign_to:
                    if pk not in assign_pokemons and self.isInPath(path,pk.edge):
                        assign_pokemons.add(pk)

        return agents_move


    def isInPath(self, path, edge):
        for i in range(len(path) -1) :
            if path[i] == edge[0] and path[i + 1] == edge[1]:
                return True
        return False

    def updateClientMovement(self, actions):
        for agent, target in actions.items():
            self.client.choose_next_edge(
                '{"agent_id":' + str(agent) + ', "next_node_id":' + str(target) + '}')
        ttl = self.client.time_to_end()
        print(ttl, self.client.get_info())

        self.client.move()
















