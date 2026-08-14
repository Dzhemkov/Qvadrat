import pygame, sys
from helperFunctions.global_constants import *
from helperFunctions.field import make_field, set_buttons
from helperFunctions.generate import *


def main():
    pygame.init()
    pygame.display.set_caption('Qvadrat')

    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    display = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE))
    clock = pygame.time.Clock()

    # font_size = max(12, int(SCREEN_SIZE * 0.5))
    # FONT = pygame.font.Font(None, font_size)

    dragging = False
    start_button = None
    selection_rect = None
    current_button = None

    level = 1

    field = make_field()
    set_buttons(field, level)

    #---------------------------------------------game loop---------------------------------------------
    while True:
        #---------------------------------------------clock---------------------------------------------
        dt = clock.tick(60) / 1000

        #---------------------------------------------event handler---------------------------------------------
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

                                if double_click.active and button == start_button:

                                    for row2 in field.buttons:
                                        for button2 in row2:
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

                                if button.color == start_button.color and button.number == None and current_button != start_button:
                                    button.color = TileColor.OPEN
                                if selection_rect.colliderect(button.rect):
                                    if button.color == TileColor.OPEN:
                                        button.color = start_button.color
                    selection_rect = None


        #---------------------------------------------update---------------------------------------------
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

        # if check_win(field, level):
        #     win_msg = field.font.render("Solved!", True, (0, 0, 0))
        #     text_rect = win_msg.get_rect(center=(SCREEN_SIZE // 2, SCREEN_SIZE // 2))
        #     display.blit(win_msg, text_rect)

        #     pygame.display.flip()
        #     pygame.time.delay(2000)

        #     if level + 1 <= len(LEVELS):
        #         level += 1
        #     else:
        #         level = 1
        #     set_buttons(field, level)


        #---------------------------------------------draw---------------------------------------------
        render(field, display)
            
        # Draw selection
        if selection_rect is not None and start_button is not None:

            color = COLOR_VALUES[start_button.color]

            selection_surface = pygame.Surface(selection_rect.size, pygame.SRCALPHA)
            selection_surface.fill((*color, 100))

            display.blit(selection_surface, selection_rect.topleft)
            pygame.draw.rect(display, color, selection_rect, 3)



        #---------------------------------------------check_win() and render message---------------------------------------------

        is_won = check_win(field, level)

        # if is_won:
        #     win_msg = field.font.render("Solved!", True, (0, 0, 0))
        #     text_rect = win_msg.get_rect(center=(SCREEN_SIZE // 2, SCREEN_SIZE // 2))

        #     bg_rect = text_rect.inflate(40, 20)
        #     pygame.draw.rect(display, (0, 0, 0), bg_rect)

        #     display.blit(win_msg, text_rect)


        #---------------------------------------------display---------------------------------------------
        screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
        pygame.display.update()


        #---------------------------------------------Level transition delay---------------------------------------------
        if is_won:
            pygame.time.delay(2000)

            if level + 1 <= len(LEVELS):
                level += 1
            else:
                level = 1

            dragging = False
            start_button = None
            selection_rect = None
            current_button = None

            set_buttons(field, level)

            #pygame.event.clear()

main()