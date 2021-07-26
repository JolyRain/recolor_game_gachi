import pygame
from game_logic.field import Field
pygame.font.init()

FONT = pygame.font.SysFont('sans', 48)


def draw_tile(surf, tile):
    pygame.draw.rect(surf, tile.color(), tile.rect())


def draw_field(surf, field):
    field_surf = pygame.Surface((field.width(), field.height()))
    surf.blit(field_surf, (field.x(), field.y()))
    for tile in field.get_tiles():
        draw_tile(surf, tile)


def draw_button(surf, button):
    pygame.draw.rect(surf, button.color, button.bounds())



def draw_counter(surf, counter, total):
    click_counter = FONT.render(str(counter) + '/' + str(total), False, (255, 255, 255))
    surf.blit(click_counter, (10, 10))


def draw_main_string(surf, string):
    state_string = FONT.render(string, True, (255, 255, 255))
    surf.blit(state_string, (200, 500))

def draw_all(surf, game):
    draw_field(surf, game.field())
    draw_counter(surf, game.clicks(), game.total_clicks())
    draw_main_string(surf, game.state())