class Tile:
    def __init__(self, x, y, width, height, color):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__color = color
        self.__colorable = False

    def rect(self):
        return self.__x, self.__y, self.__width, self.__height

    def coordinates(self):
        return [self.__x, self.__y]

    def set_color(self, color):
        self.__color = color

    def set_colorable(self):
        self.__colorable = True

    def x(self):
        return self.__x

    def y(self):
        return self.__y

    def width(self):
        return self.__width

    def height(self):
        return self.__height

    def color(self):
        return self.__color

    def is_colorable(self):
        return self.__colorable

    def __str__(self):
        return '(' + str(self.__x) + ',' + str(self.__y) + ')'
