import random
import sys

import pygame as pg

from app.button import Button
from game_logic.defaults import RED, BUTTON_SIZE, BLUE, GREEN, YELLOW, AQUA, ORANGE
from app import drawer
from game_logic.field import Field
from game_logic.game import Game

pg.init()
FPS = 60
screen = pg.display.set_mode((600, 700), pg.RESIZABLE)
clock = pg.time.Clock()
field = Field(120, 120, 144)
game = Game(field, 22)

button_red = Button(10, 600, BUTTON_SIZE, BUTTON_SIZE, RED)
button_blue = Button(110, 600, BUTTON_SIZE, BUTTON_SIZE, BLUE)
button_green = Button(210, 600, BUTTON_SIZE, BUTTON_SIZE, GREEN)
button_yellow = Button(310, 600, BUTTON_SIZE, BUTTON_SIZE, YELLOW)
button_aqua = Button(410, 600, BUTTON_SIZE, BUTTON_SIZE, AQUA)
button_pink = Button(510, 600, BUTTON_SIZE, BUTTON_SIZE, ORANGE)

buttons = [button_aqua, button_blue, button_green, button_pink, button_red, button_yellow]

VOLUME = 0.1
sound1 = pg.mixer.Sound('sound/ah.mp3')
sound2 = pg.mixer.Sound('sound/ah1.mp3')
sound3 = pg.mixer.Sound('sound/ah2.mp3')
sound4 = pg.mixer.Sound('sound/ah3.mp3')
# victory_sound = pg.mixer.Sound('sound/victory.mp3')

sounds = [sound1, sound2, sound3, sound4]
ambient = pg.mixer.Sound('sound/ambient.mp3')


def clicked_button(event):
    if event.type == pg.MOUSEBUTTONDOWN and game.can_play():
        if event.button == 1:
            for button in buttons:
                if button.is_inside_point(event.pos[0], event.pos[1]) and button.color != game.current_color():
                    # click = pg.mixer.Sound('sound/click.wav')
                    click = random.choice(sounds)
                    click.set_volume(VOLUME)
                    click.play()
                    return button


def draw_buttons():
    for button in buttons:
        drawer.draw_button(screen, button)


def retry(event):
    if event.type == pg.KEYDOWN and event.key == pg.K_r:
        game.retry()


def show():
    ambient.set_volume(VOLUME)
    ambient.play()
    while 1:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            retry(event)
            game.button_on_click(clicked_button(event))
        screen.fill((0, 0, 0))
        drawer.draw_all(screen, game)
        draw_buttons()
        pg.display.update()
