import random
from math import sqrt

from game_logic.defaults import TILE_SIZE, COLORS
from game_logic.tile import Tile


class Field:
    def __init__(self, x, y, tiles_amount):
        self.__x = x
        self.__y = y
        self.__tiles_amount = tiles_amount
        self.__width = int(TILE_SIZE * tiles_amount / 2)
        self.__height = int(TILE_SIZE * tiles_amount / 2)
        self.__tiles = []
        self.__init_tiles()

    def __init_tiles(self):
        x, y = self.__x, self.__y
        for i in range(self.__tiles_amount):
            new_tile = Tile(x, y, TILE_SIZE, TILE_SIZE, random.choice(COLORS))
            x += TILE_SIZE
            if x >= self.__x + sqrt(self.__tiles_amount) * TILE_SIZE:
                x = self.__x
                y += TILE_SIZE
            self.__tiles.append(new_tile)

    def sizes(self):
        return self.__width, self.__height

    def get_tiles(self):
        return self.__tiles

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def width(self):
        return self.__width

    def height(self):
        return self.__height

