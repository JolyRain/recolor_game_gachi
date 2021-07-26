import pygame


class Button:
    def __init__(self, x, y, width, height, color, on_click=lambda x: None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.state = 'normal'
        self.on_click = on_click
        self.color = color

    def bounds(self):
        return self.x, self.y, self.width, self.height

    def is_inside_point(self, x, y):
        return self.x <= x <= self.x + self.width and self.y <= y <= self.y + self.height
