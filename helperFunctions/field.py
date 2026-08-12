from helperFunctions.button import Button
from helperFunctions.global_constants import *

class Field:
    def __init__(self, n, screen_size):
        self.n = n
        self.tile_size = screen_size // n
        self.field = [[0] * n for _ in range(n)]
        self.buttons = [[Button(col, row, TILE_SIZE) for col in range(n)] for row in range(n)]
        self.font = pygame.font.Font(None, 36)

        self.tile_images = {
            TileColor.OPEN: pygame.transform.scale(
                IMAGES['OPEN_FIELD_IMAGE'],
                (self.tile_size, self.tile_size)
            ),
            TileColor.BLOCK: pygame.transform.scale(
                IMAGES['BLOCK_FIELD_IMAGE'],
                (self.tile_size, self.tile_size)
            ),

            TileColor.RED: pygame.transform.scale(
                IMAGES['RED_BLOCK_IMAGE'],
                (self.tile_size, self.tile_size)
            ),
            TileColor.ORANGE: pygame.transform.scale(
                IMAGES['ORANGE_BLOCK_IMAGE'],
                (self.tile_size, self.tile_size)
            ),
            TileColor.YELLOW: pygame.transform.scale(
                IMAGES['YELLOW_BLOCK_IMAGE'],
                (self.tile_size, self.tile_size)
            ),
            TileColor.GREEN: pygame.transform.scale(
                IMAGES['GREEN_BLOCK_IMAGE'],
                (self.tile_size, self.tile_size)
            ),
            TileColor.BLUE: pygame.transform.scale(
                IMAGES['BLUE_BLOCK_IMAGE'],
                (self.tile_size, self.tile_size)
            ),
            TileColor.PURPLE: pygame.transform.scale(
                IMAGES['PURPLE_BLOCK_IMAGE'],
                (self.tile_size, self.tile_size)
            ),
            TileColor.PINK: pygame.transform.scale(
                IMAGES['PINK_BLOCK_IMAGE'],
                (self.tile_size, self.tile_size)
            )
        }

        self.highlight = pygame.transform.scale(IMAGES['HIGHLIGHT_IMAGE'], (self.tile_size, self.tile_size))




    def display(self):
        for row in self.field:
            for col in row:
                print(col, end="")
            print()
        print("--------------------------------")



def set_button(field, row, col, number, color):
    button = field.buttons[row][col]

    button.number = number
    button.color = color


def set_buttons(field):
    set_button(field, 0, 0, 5, TileColor.RED)
    set_button(field, 3, 3, 9, TileColor.BLUE)
    set_button(field, 3, 6, 10, TileColor.GREEN)
    set_button(field, 4, 3, 7, TileColor.YELLOW)
    set_button(field, 5, 0, 7, TileColor.PURPLE)
    set_button(field, 5, 5, 4, TileColor.ORANGE)
    set_button(field, 6, 0, 4, TileColor.PINK)
    set_button(field, 1, 4, None, TileColor.BLOCK)
    set_button(field, 2, 4, None, TileColor.BLOCK)
    set_button(field, 2, 5, None, TileColor.BLOCK)


def make_field():
    field = Field(N, SCREEN_SIZE)
    set_buttons(field)

    #field.display()
    return field