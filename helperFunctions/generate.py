from helperFunctions.button import Button
from helperFunctions.global_constants import *


def render(field, display):
    for row_idx, row in enumerate(field.buttons):  #(row_idx is y) and (col_idx is x)
        for col_idx, button in enumerate(row):

            button.draw(field, row_idx, col_idx)

            image = field.tile_images[button.color]
            display.blit(image, (col_idx * field.tile_size, row_idx * field.tile_size))

            if button.number is not None:
                text = field.font.render(str(button.number), True, (0, 0, 0))

                text_rect = text.get_rect(center=(col_idx * field.tile_size + field.tile_size // 2, row_idx * field.tile_size + field.tile_size // 2))

                display.blit(text, text_rect)

            if button.hover and button.number != None:
                display.blit(field.highlight, (col_idx * field.tile_size, row_idx * field.tile_size))


            # if button.left_clicked:
            #     print(f"{button.number}, {button.color}")


def get_button_at_mouse(self):
    mouse_pos = pygame.mouse.get_pos()

    for row in self.buttons:
        for button in row:
            if button.rect.collidepoint(mouse_pos):
                return button

    return None


def check_win(field, level):    

    for row, col, number, color in LEVELS[level - 1]:
        if color == TileColor.BLOCK:
            continue
        if not count_contiguous(field, row, col, number, color):
            return False

    return True


def count_contiguous(field, start_row, start_col, number, color):

    buttons = field.buttons
    visited = set()

    def flood_fill(row, col):

        if row < 0 or row >= N:        # Outside board
            return 0
        if col < 0 or col >= N:
            return 0

        if (row, col) in visited:        # Already visited
            return 0

        if buttons[row][col].color != color:        # Wrong color
            return 0

        visited.add((row, col))

        count = 1

        count += flood_fill(row + 1, col)        # Down
        count += flood_fill(row - 1, col)        # Up
        count += flood_fill(row, col + 1)        # Right
        count += flood_fill(row, col - 1)        # Left

        return count

    return flood_fill(start_row, start_col) == number







# def if_count_contiguous(field, row, col, number, color):

#     buttons = field.buttons
#     visited = set()
    
#     if buttons[row][col].color != TileColor.BLOCK:
#         if row + 1 < N:
#             if buttons[row + 1][col].color == color:
#                 count += 1
#                 if_count_contiguous(field, row + 1, col, buttons[row + 1][col].number, color)
#         if row - 1 >= 0:
#             if buttons[row - 1][col].color == color:
#                 count += 1
#                 if_count_contiguous(field, row - 1, col, buttons[row - 1][col].number, color)
#         if col + 1 < N:
#             if buttons[row][col + 1].color == color:
#                 count += 1
#                 if_count_contiguous(field, row, col + 1, buttons[row][col + 1].number, color)
#         if col - 1 >= 0:
#             if buttons[row][col - 1].color == color:
#                 count += 1
#                 if_count_contiguous(field, row, col - 1, buttons[row][col - 1].number, color)
#         if count == number:
#             win = True
#         else:
#             return False

#     count = 1
#     return win