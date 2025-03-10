# External Module used to draw shapes very nicely

import pygame

def draw_circle(screen, shape):
    pygame.draw.circle(screen, shape['color'], shape['position'], shape['radius'])
    
def draw_rect(screen, shape):
    pygame.draw.rect(screen, shape['color'], (shape['position'][0], shape['position'][1], shape['width'], shape['height']))
    
def draw_line(screen, shape):
    pygame.draw.line(screen, shape['color'], shape['start_pos'], shape['end_pos'], shape['width'])

def draw_square(screen, shape):
    pygame.draw.rect(screen, shape['color'], (shape['position'][0] - shape['radius'], shape['position'][1] - shape['radius'], shape['radius'] * 2, shape['radius'] * 2))

def draw_tri(screen, shape):
    pygame.draw.polygon(screen, shape['color'], [[(shape['position'][0]), (shape['position'][1] - shape['radius'])],[(shape['position'][0] - shape['radius']), (shape['position'][1] + shape['radius'])],[(shape['position'][0] + shape['radius']), (shape['position'][1] + shape['radius'])]])