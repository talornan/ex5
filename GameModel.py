from GameInfo import GameInfo
from agent import Agents
from client import Client
from graph.GraphAlgo import GraphAlgo
from pokemon import Pokemons
import json
import time


class GameModel(object):
    """
        The logic of the game. in the class the main algorithem is implementes. the target of this class in to maximize
        the grade of all the agents.
        The  Algorithm contains three main parts:
            1. init - we are init each agent in closest as possible to the most valuable pokemons. in order to do so,
            Merging is executeed over the pokemons object(the value fielst), and agent is assign using to the closet node.
            2.  Algorithm -
                1. check if there are agent that already on the way of eating pokemons, if so, we should ignore those agents, and those pokemons
                2. we are using the closet path  Algorithm, between each agent and pokemons.
                3. if we are close(decided on 1 edges) to a pokemon - we are assign the the agent to this pokemon.
                4. take all the unassign pokemons are sort them by thier value.
                5. take the dikstra of each agent and divide by the speed - we want to send the first agent(ascnding order)
                6. run this algorithem over and over until the game is ending.
            3. for all pokemons that are "on the way on the agent, add them to the assign pokemons list
        this class is in use in order to simplify the the use in the json that return from the client
    """
    # default port
    PORT = 6666
    # server host (default localhost 127.0.0.1)
    HOST = '127.0.0.1'


    def __init__(self, ):
        """
            init the client and the graph. this class is the model of in the mvs model
        """
        self.client = Client()
        self.client.start_connection(self.HOST, self.PORT)
        self.game_info = GameInfo(self.client.get_info(), self.client.time_to_end())
        self.graphAlgo = GraphAlgo()
        self.graphAlgo.load_graph_from_json(json.loads(self.client.get_graph()))
        self.graph = self.graphAlgo.get_graph()
        self.pokemons = Pokemons(self.client.get_pokemons(), self.graph)
        self.action = {}
        ## just to make sure we are not exceeding the 10 times moves in second
        self.last_algorithem_run = -1

    def runAndUpdate(self):
        #get update from the client regarding the pokemon/agent/game status
        self.update()
        #if we can run the algorithem without exceeding the move limitation
        if self.last_algorithem_run == -1 or time.time() * 1000 - self.last_algorithem_run > 100:
            #runt the algorithem
            actions = self.gameAlgo()
            #update client movement
            self.updateClientMovement(actions)
            self.last_algorithem_run = time.time() * 1000


    def init_game(self):
        """
            init each agent near the most valuable pokemon the list
        """
        poks = self.pokemons.pokemons
        poks.sort(key=lambda x: x.value, reverse=True)
        for i in range(self.game_info.agents):
            node = poks[i].edge[0]
            assignment_json = json.dumps({"id": node})
            print("node " + str(poks[i].edge))
            self.client.add_agent(str(assignment_json))

        self.client.start()

    def update(self):
        """
            update data from the client regardsing the agents, polemons and game info
        """
        self.agents = Agents(self.client.get_agents())
        self.pokemons = Pokemons(self.client.get_pokemons(), self.graph)
        self.game_info = GameInfo(self.client.get_info(), self.client.time_to_end())

    def gameAlgo(self):
        """
        The  Algorithm contains three main parts:
            1. init - we are init each agent in closest as possible to the most valuable pokemons. in order to do so,
            Merging is executeed over the pokemons object(the value fielst), and agent is assign using to the closet node.
            2.  Algorithm -
                1. check if there are agent that already on the way of eating pokemons, if so, we should ignore those agents, and those pokemons
                2. we are using the closet path  Algorithm, between each agent and pokemons.
                3. if we are close(decided on 1 edges) to a pokemon - we are assign the the agent to this pokemon.
                4. take all the unassign pokemons are sort them by thier value.
                5. take the dikstra of each agent and divide by the speed - we want to send the first agent(ascnding order)
                6. run this algorithem over and over until the game is ending.
            3. for all pokemons that are "on the way on the agent, add them to the assign pokemons list

        """

        # dictinery for the agents movement
        agents_move = {}
        # empty set for all assign agent
        assign_agent = set()
        # filter out agents that are on the move
        agents = [agent for agent in self.agents.agents if agent.isMoving() == False]
        # in order to remove pokemons that agents are currently "fighting for", saving the edge that are walking on
        agents_assign_edge = {agent.edge for agent in self.agents.agents if agent.isMoving() == True}

        pokemon_agents_not_already_assign_to = [pokemon for pokemon in self.pokemons.pokemons if
                                                pokemon.edge not in agents_assign_edge]
        assign_pokemons = {pokemon for pokemon in self.pokemons.pokemons if pokemon.edge in agents_assign_edge}


        # (agent_id, pokemon_id) -> path
        # save all pokemon and agent that are 1 point distance
        one_step_distance = {}
        pokemon_distance_from_agent = {}

        if len(agents) == 0:
            return {}


        # create mapping between the distance of each pokemon and each agent
        for agent in agents:
            for pokemon in pokemon_agents_not_already_assign_to:
                pokemon_target = pokemon.src if agent.src != pokemon.src else pokemon.dest
                path = self.graphAlgo.shortest_path(agent.src, pokemon_target)[1]
                # meaning only one hop since the first is the current node
                if len(path) <= 2:
                    if agent.id in one_step_distance:
                        one_step_distance[agent.id].append((pokemon, pokemon_target))
                    else:
                        one_step_distance[agent.id] = [(pokemon, pokemon_target)]
                # distance[(agent.id, pokemon.id)] =  (path, pokemon,agent)

                if pokemon in pokemon_distance_from_agent:
                    pokemon_distance_from_agent[pokemon].append((path, pokemon, agent))
                else:
                    pokemon_distance_from_agent[pokemon] = [(path, pokemon, agent)]

        # if the distance is one - assign agent
        for agent, pokemons in one_step_distance.items():
            pokemons.sort(key=lambda x: x[0].value, reverse=True)
            agents_move[agent] = pokemons[0][1]
            assign_agent.add(agent)
            assign_pokemons.add(pokemons[0])

        pokemon_agents_not_already_assign_to = [pokemon for pokemon in pokemon_agents_not_already_assign_to if
                                                pokemon not in assign_pokemons]
        pokemon_agents_not_already_assign_to.sort(key=lambda x: x.value, reverse=True)
        # assigna gent to the mose valuable pokemons - asign the agent that is the both fast and close -> with len(x[0]) / x[2].speed
        for pokemon in pokemon_agents_not_already_assign_to:
            data = pokemon_distance_from_agent[pokemon]
            data.sort(key=lambda x: len(x[0]) / x[2].speed, reverse=True)
            data = [elem for elem in data if elem[2] not in assign_agent]
            if len(data) > 0:
                (path, pokemon, agent) = data[0]
                print(path)
                agents_move[agent.id] = path[1]  # target node
                assign_agent.add(agent)
                assign_pokemons.add(pokemon)
                # in case we already assign agent, this agent may take also anothe pokemon that are "on the way",
                # so no need to handle them
                for pk in pokemon_agents_not_already_assign_to:
                    if pk not in assign_pokemons and self.isInPath(path, pk.edge):
                        assign_pokemons.add(pk)

        return agents_move


    def isInPath(self, path, edge):
        """
            if edge is in path, it means we will take this pokemons on our path anyway
        :param path:
        :param edge:
        :return:
        """
        for i in range(len(path) - 1):
            if path[i] == edge[0] and path[i + 1] == edge[1]:
                return True
        return False

    def updateClientMovement(self, actions):
        """
            update clients move
        """
        for agent, target in actions.items():
            self.client.choose_next_edge(
                '{"agent_id":' + str(agent) + ', "next_node_id":' + str(target) + '}')
        self.client.move()
