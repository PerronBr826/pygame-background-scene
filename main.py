# Pygame game template

import pygame
import sys
import config # Import the config module
import random
import shapes # Import the drawing module

def init_game ():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config

    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def darken_color(color, darkness):
    newcolor = []
    newcolor.append(color[0] * darkness)
    newcolor.append(color[1] * darkness)
    newcolor.append(color[2] * darkness)
    return newcolor

def main():

    def draw_cloud(location):
        height = location[1]
        position = location[0]

        if height < config.WINDOW_HEIGHT/2:
            shapes.draw_circle(screen, {"color" : darken_color(config.WHITE, random.randint(90,100)/100), "position" : [position, height], "radius" : 20 - pygame.math.clamp((height/config.WINDOW_HEIGHT) * 20, 3, 40)})
        
    def draw_tree(location):
        height = location[1]
        position = location[0]

        if height < (config.WINDOW_HEIGHT/2 + 30):
            shapes.draw_circle(screen, {"color" : darken_color(config.GREEN, random.randint(30,60)/100), "position" : [position, height], "radius" : pygame.math.clamp((height/config.WINDOW_HEIGHT) * 10, 3, 40)})
        else:
            # Variables
            leaf_color = darken_color(config.GREEN, random.randint(30,60)/100)
            size = round(pygame.math.clamp((height/(config.WINDOW_HEIGHT-20)) * 10, 3, 100))
            
            # Draw Shadow
            # shapes.draw_circle(screen, {"color" : darken_color(config.GREEN, random.randint(40,50)/100), "position" : [position, height], "radius" : size * 1.5})
            # shapes.draw_circle(screen, {"color" : darken_color(config.GREEN, random.randint(35,40)/100), "position" : [position, height], "radius" : size * 1.2})
            
            # Draw Tree
            shapes.draw_square(screen, {"color" : config.BROWN, "position" : [position, height], "radius" : size/4})
            shapes.draw_tri(screen, {"color" : leaf_color, "position" : [position, height - size * 1.2], "radius" : size})
            shapes.draw_tri(screen, {"color" : darken_color(leaf_color, 1.05), "position" : [position, height - size * 2.5], "radius" : size * 0.8})
            if random.randrange(2) == 1:
                shapes.draw_tri(screen, {"color" : darken_color(leaf_color, 1.1), "position" : [position, height - size * 3.6], "radius" : size * 0.6})

        
    pygame.font.init()
    font = pygame.font.SysFont("Comic Sans MS", 50)
    gar = font.render("gar", True, config.BLACK)
    field = font.render("Field", True, config.BLACK)
            
        
    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock here
    running = True
    while running:
        running = handle_events()
        screen.fill(config.BLUE) # Use color from config

        # Draw Clouds
        for i in range(200):
            draw_cloud([random.randint(0,config.WINDOW_WIDTH), config.WINDOW_HEIGHT-random.randint(((config.WINDOW_HEIGHT+50)/2),config.WINDOW_HEIGHT)])

        # Draw SUN
        shapes.draw_circle(screen, {"color" : config.YELLOW, "position" : [config.WINDOW_WIDTH/4, -10 + config.WINDOW_HEIGHT/2], "radius" : 70})
        
        # Draw Hill

        shapes.draw_circle(screen, {"color" : darken_color(config.GREEN, 0.8), "position" : [config.WINDOW_WIDTH - 300, 60 + config.WINDOW_HEIGHT/2], "radius" : 100})
        shapes.draw_circle(screen, {"color" : darken_color(config.GREEN, 0.8), "position" : [config.WINDOW_WIDTH - 200, 40 + config.WINDOW_HEIGHT/2], "radius" : 100})
        shapes.draw_circle(screen, {"color" : darken_color(config.GREEN, 0.8), "position" : [config.WINDOW_WIDTH - 20, 120 + config.WINDOW_HEIGHT/2], "radius" : 200})

        # Draw Floor
        shapes.draw_rect(screen, {"color" : darken_color(config.GREEN, 0.8), "position" : [0, config.WINDOW_HEIGHT/2], "width" : config.WINDOW_WIDTH, "height" : config.WINDOW_HEIGHT})

        # Closer Hill
        shapes.draw_circle(screen, {"color" : darken_color(config.GREEN, 0.75), "position" : [config.WINDOW_WIDTH - 250, 40 + config.WINDOW_HEIGHT/2], "radius" : 100})
        shapes.draw_rect(screen, {"color" : darken_color(config.GREEN, 0.75), "position" : [0, 10 + config.WINDOW_HEIGHT/2], "width" : config.WINDOW_WIDTH, "height" : config.WINDOW_HEIGHT})
        
        # Even Closer Hill
        shapes.draw_circle(screen, {"color" : darken_color(config.GREEN, 0.75), "position" : [config.WINDOW_WIDTH - 100, 180 + config.WINDOW_HEIGHT/2], "radius" : 200})
        shapes.draw_rect(screen, {"color" : darken_color(config.GREEN, 0.6), "position" : [0, 30 + config.WINDOW_HEIGHT/2], "width" : config.WINDOW_WIDTH, "height" : config.WINDOW_HEIGHT})
        shapes.draw_rect(screen, {"color" : darken_color(config.GREEN, 0.5), "position" : [0, 70 + config.WINDOW_HEIGHT/2], "width" : config.WINDOW_WIDTH, "height" : config.WINDOW_HEIGHT})

        # Draw Trees
        for i in range(200):
            draw_tree([random.randint(0,config.WINDOW_WIDTH), random.randint(config.WINDOW_HEIGHT/2,config.WINDOW_HEIGHT)])

        screen.blit(gar, (config.WINDOW_WIDTH // 2 - 370, config.WINDOW_HEIGHT // 2 - 60))
        screen.blit(field, (config.WINDOW_WIDTH // 2 - 100, config.WINDOW_HEIGHT // 2 - 60))

        pygame.display.flip()

        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS) # Use the clock to control the frame rate

    pygame.quit()

    sys.exit()

if __name__ == "__main__":
    main()