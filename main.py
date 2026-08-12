import pygame, sys
from helperFunctions.global_constants import *
from helperFunctions.field import make_field
from helperFunctions.generate import *


def main():
    pygame.init()
    pygame.display.set_caption('Qvadrat')


    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    display = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE))
    clock = pygame.time.Clock()


    dragging = False
    drag_start = None
    drag_end = None
    start_button = None
    selection_rect = None

    field = make_field()


    #game loop
    while True:
        #clock
        dt = clock.tick(60) / 1000

        # if start_button.draw(screen):
        # 	print('START')
        # if exit_button.draw(screen):
        # 	print('EXIT')

        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()

                    for row in field.buttons:
                        for button in row:

                            if button.rect.collidepoint(mouse_pos) and button.color != TileColor.BLOCK and button.color != TileColor.OPEN and button.number != None:

                                # Double-click detected
                                if double_click.active and button == start_button:

                                    for row2 in field.buttons:
                                        for button2 in row2:

                                            #if button2.color == start_button.color:
                                            if button2.color == start_button.color and button2.number == None:
                                                button2.color = TileColor.OPEN

                                    double_click.deactivate()
                                    dragging = False
                                    selection_rect = None

                                else:
                                    double_click.activate()
                                    dragging = True
                                    start_button = button
                                    selection_rect = pygame.Rect(button.rect)


            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    dragging = False
                    if selection_rect is not None:
                        for row in field.buttons:
                            for button in row:
                                if selection_rect.colliderect(button.rect):
                                    if button.color == TileColor.OPEN:
                                        button.color = start_button.color
                    selection_rect = None


        #update

        double_click.update()


        if dragging and start_button is not None:
            mouse_pos = pygame.mouse.get_pos()

            current_button = None

            for row in field.buttons:
                for button in row:
                    if button.rect.collidepoint(mouse_pos):
                        current_button = button
                        break

                if current_button is not None:
                    break

            if current_button is not None:

                x = min(start_button.x, current_button.x)
                y = min(start_button.y, current_button.y)

                width = (abs(start_button.x - current_button.x) + 1)
                height = (abs(start_button.y - current_button.y) + 1)

                selection_rect = pygame.Rect(x * field.tile_size, y * field.tile_size, width * field.tile_size, height * field.tile_size)

        #draw

        render(field, display)

        # Draw selection
        if selection_rect is not None and start_button is not None:

            color = COLOR_VALUES[start_button.color]

            selection_surface = pygame.Surface(selection_rect.size, pygame.SRCALPHA)

            selection_surface.fill((*color, 100))

            display.blit(selection_surface, selection_rect.topleft)

            pygame.draw.rect(display, color, selection_rect, 3)



        #display
        screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
        pygame.display.update()
        
main()