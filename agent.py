import json


class Agent(object):
    """
        this object represet the agent(pokemons master) in the game.
        this class is in use in order to simplify  the use in the json that return from the client
    """

    def __init__(self, agent_json):
        """
        returns: agent_json
        {
            "Agents":[
                {
                    "Agent":
                    {
                        "id":0,
                        "value":0.0,
                        "src":0,
                        "dest":1,
                        "speed":1.0,
                        "pos":"35.18753053591606,32.10378225882353,0.0"
                    }
                }
            ]
        }
        """
        self.id = agent_json["id"]
        self.value = agent_json["value"]
        self.src = agent_json["src"]
        self.dest = agent_json["dest"]
        self.speed = agent_json["speed"]
        self.pos = agent_json["pos"].split(",")
        self.x = float(self.pos[0])
        self.y = float(self.pos[1])

        self.edge = (self.src, self.dest)



    def isMoving(self):
        """
            is case the test is different then ie the agent is on the move on an edge
        :return:
        """
        return self.dest != -1


class Agents(object):
    """
        simpel wrapper for list of agents
        this class is in use in order to simplify the  use in the json that return from the client
    """
    def __init__(self, agents_json_str):
        self.agents = []
        agents_json = json.loads(agents_json_str)
        for agent in agents_json["Agents"]:
            self.agents.append(Agent(agent["Agent"]))



