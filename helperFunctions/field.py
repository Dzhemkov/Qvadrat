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


def set_buttons(field, level):

    #print(F"Row: {LEVELS[0][1][0]}, Col: {LEVELS[0][1][1]}, Number: {LEVELS[0][1][2]}, Color: {LEVELS[0][1][3]}")
    for row in field.buttons:
        for button in row:
            button.color = TileColor.OPEN
            button.number = None

    for row, col, number, color in LEVELS[level - 1]:
        #print(F"Row: {row}, Col: {col}, Number: {number}, Color: {color}")
        set_button(field, row, col, number, color)



def make_field():
    field = Field(N, SCREEN_SIZE)

    #set_buttons(field)

    #field.display()
    return field