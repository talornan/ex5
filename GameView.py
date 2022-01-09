from types import SimpleNamespace

from Button import Button
from client import Client
import json
from pygame import gfxdraw
import pygame
from pygame import *

# init pygame


class GameView(object):
    WIDTH, HEIGHT = 1080, 720

    def __init__(self, graph):
        self.min_x = min(list(graph.get_all_v().values()), key=lambda n: n.location[0]).location[0]
        self.min_y = min(list(graph.get_all_v().values()), key=lambda n: n.location[1]).location[1]
        self.max_x = max(list(graph.get_all_v().values()), key=lambda n: n.location[0]).location[0]
        self.max_y = max(list(graph.get_all_v().values()), key=lambda n: n.location[1]).location[1]
        pygame.init()
        self.screen = display.set_mode((self.WIDTH, self.HEIGHT), depth=32, flags=RESIZABLE)
        self.clock = pygame.time.Clock()
        pygame.font.init()
        self.FONT = pygame.font.SysFont('Arial', 20, bold=True)
        self.radius = 15


    def scale(self, data, min_screen, max_screen, min_data, max_data):
        """
        get the scaled data with proportions min_data, max_data
        relative to min and max screen dimentions
        """
        return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen

    # decorate scale with the correct values

    def my_scale(self, data, x=False, y=False):
        if x:
            return self.scale(data, 50, self.screen.get_width() - 50, self.min_x, self.max_x)
        if y:
            return self.scale(data, 50, self.screen.get_height() - 50, self.min_y, self.max_y)


    def show_agents(self, agents):
        for agent in agents.agents:
            x = self.my_scale(agent.x, x=True)
            y = self.my_scale(agent.y, y=True)
            pygame.draw.circle(self.screen, Color(122, 61, 23),
                               (int(x), int(y)), 10)


    def show_nodes(self, graph):

        for node_id, data in graph.get_all_v().items():
            x = self.my_scale(data.location[0], x=True)
            y = self.my_scale(data.location[1], y=True)

    # its just to get a nice antialiased circle
            gfxdraw.filled_circle(self.screen, int(x), int(y), self.radius, Color(64, 80, 174))
            gfxdraw.aacircle(self.screen, int(x), int(y), self.radius, Color(255, 255, 255))
        # draw the node id
            id_srf = self.FONT.render(str(node_id), True, Color(255, 255, 255))
            rect = id_srf.get_rect(center=(x, y))
            self.screen.blit(id_srf, rect)
    def show_edges(self, graph):
        for src,dests in graph.get_all_edges().items():
            for dest, weight in dests.items():
                srcPos = graph.getNode(src).location
                destPos = graph.getNode(dest).location
                src_x = self.my_scale(srcPos[0], x=True)
                src_y = self.my_scale(srcPos[1], y=True)
                dest_x = self.my_scale(destPos[0], x=True)
                dest_y = self.my_scale(destPos[1], y=True)
                pygame.draw.line(self.screen, Color(61, 72, 126),(src_x, src_y), (dest_x, dest_y))

    def show_pokemons(self, pokemons):

        # draw pokemons (note: should differ (GUI wise) between the up and the down pokemons (currently they are marked in the same way).
        for p in pokemons.pokemons:
            x, y, _ = p.pos
            x = self.my_scale(x, x= True)
            y = self.my_scale(y, y= True)
            color = Color(255, 255	, 0) if p.type > 0 else Color(0, 255, 255)
            pygame.draw.circle(self.screen, color, (int(x), int(y)), 10)
            id_srf = self.FONT.render(str(p.value), True, Color(255, 255, 255))
            rect = id_srf.get_rect(center=(x, y))
            self.screen.blit(id_srf, rect)


    def show_info(self, game_info):
        text1 = "Remaining time in seconds {}".format(int(game_info.time_remaining) /1000)
        text2 = "moves {}, points {}".format(game_info.moves, game_info.grade)
        id_srf = self.FONT.render(str(text1), True, Color(255, 255, 255))
        rect = id_srf.get_rect(center=(170, 8))
        self.screen.blit(id_srf, rect)
        id_srf = self.FONT.render(str(text2), True, Color(255, 255, 255))
        rect = id_srf.get_rect(center=(170, 40))
        self.screen.blit(id_srf, rect)

    def button(self):
        # class up here
        btn = Button(pygame, (255, 0, 0), 100, 50, 200, 50, text="Exit")
        # do above before you start the loop
        # all of the pygame init and loop
        # Define screen as the window

        btn.draw(self.screen)
        #display.update()
        if btn.isOver(pygame.mouse.get_pos()) == True:
            pygame.quit()
            return False
        return True

    def show_all(self, agents, pokemons, graph, game_info):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        # refresh surface

        self.screen.fill(Color(0, 0, 0))
        if self.button() == False:
            return False


        self.show_nodes(graph)
        self.show_edges(graph)
        self.show_agents(agents)
        self.show_pokemons(pokemons)
        self.show_info(game_info)
        display.update()
        # refresh rate
        self.clock.tick(60)
