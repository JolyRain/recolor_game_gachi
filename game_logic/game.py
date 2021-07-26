import random

from game_logic import defaults
from game_logic.field import Field
import networkx as nx


class Game:
    def __init__(self, field: Field, total_clicks: int):
        self.__field = field
        self.__total_clicks = total_clicks
        self.__colorable_tiles = []
        self.__graph = nx.Graph()
        self.__counter = 0
        self.__init_graph()
        self.__colorable_tiles.append(field.get_tiles()[0])

    def __edges_x(self):
        sorted_tiles = sorted(self.__field.get_tiles(), key=lambda tile: tile.y())
        for i in range(len(sorted_tiles)):
            if i == len(sorted_tiles) - 1:
                return
            current_tile = sorted_tiles[i]
            next_tile = sorted_tiles[i + 1]
            if current_tile.y() == next_tile.y():
                self.__graph.add_edge(current_tile, next_tile)

    def __edges_y(self):
        sorted_tiles = sorted(self.__field.get_tiles(), key=lambda tile: tile.x())
        for i in range(len(sorted_tiles)):
            if i == len(sorted_tiles) - 1:
                return
            current_tile = sorted_tiles[i]
            next_tile = sorted_tiles[i + 1]
            if current_tile.x() == next_tile.x():
                self.__graph.add_edge(current_tile, next_tile)

    def __init_graph(self):
        self.__graph.add_nodes_from(self.__field.get_tiles())
        self.__edges_x()
        self.__edges_y()

    def button_on_click(self, button):
        if button is None:
            return
        self.__recolor(button.color)
        self.__counter += 1

    def __colorable_neighbours(self):
        start_tile = random.choice(self.__colorable_tiles)
        stack = [start_tile]
        visited = dict.fromkeys(self.__colorable_tiles, False)
        visited.update({start_tile: True})
        while len(stack) > 0:
            current_tile = stack.pop()
            self.__colorable_tiles.append(current_tile)
            for tile in self.__graph.neighbors(current_tile):
                if not visited.get(tile) and tile.color() == start_tile.color():
                    stack.append(tile)
                    visited.update({tile: True})

    def __recolor(self, color):
        self.__colorable_neighbours()
        for tile in self.__colorable_tiles:
            tile.set_color(color)

    def graph(self):
        return self.__graph

    def current_color(self):
        return self.__colorable_tiles[0].color()

    def clicks(self):
        return self.__counter

    def total_clicks(self):
        return self.__total_clicks

    def field(self):
        return self.__field

    def is_victory(self):
        return self.state() == 'Victory'

    def state(self):
        color = self.__colorable_tiles[0].color()
        for tile in self.__field.get_tiles():
            if color != tile.color():
                if self.__counter == self.__total_clicks:
                    return 'You lost'
                return 'Recolor!'
        if self.__counter <= self.__total_clicks:
            return 'Victory'

    def can_play(self):
        return self.state() == 'Recolor!'

    def retry(self):
        new_field = Field(self.__field.x(), self.__field.y(), len(self.__field.get_tiles()))
        self.__init__(new_field, self.__total_clicks)