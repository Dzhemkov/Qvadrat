import os, pygame
from enum import Enum
from helperFunctions.timer import *


# WIDTH_TILES = 10
# HEIGHT_TILES = 10
SCREEN_SIZE = 800
N = 7
TILE_SIZE = SCREEN_SIZE // N

base_path = os.path.dirname(__file__)

IMAGES = {
    'BLUE_BLOCK_IMAGE': pygame.image.load("Sprites/blue_block.png"),
    'GREEN_BLOCK_IMAGE': pygame.image.load("Sprites/green_block.png"),
    'ORANGE_BLOCK_IMAGE': pygame.image.load("Sprites/orange_block.png"),
    'PINK_BLOCK_IMAGE': pygame.image.load("Sprites/pink_block.png"),
    'PURPLE_BLOCK_IMAGE': pygame.image.load("Sprites/purple_block.png"),
    'RED_BLOCK_IMAGE': pygame.image.load("Sprites/red_block.png"),
    'YELLOW_BLOCK_IMAGE': pygame.image.load("Sprites/yellow_block.png"),
    'OPEN_FIELD_IMAGE': pygame.image.load("Sprites/open_field.png"),
    'BLOCK_FIELD_IMAGE': pygame.image.load("Sprites/block_field.png"),
    'HIGHLIGHT_IMAGE': pygame.image.load("Sprites/highlight.png"),
}


class TileColor(Enum):
    OPEN = 0
    RED = 1
    ORANGE = 2
    YELLOW = 3
    GREEN = 4
    BLUE = 5
    PURPLE = 6
    PINK = 7
    BLOCK = 8
    

COLOR_VALUES = {

    TileColor.RED: (255, 0, 0),
    TileColor.ORANGE: (255, 165, 0),
    TileColor.YELLOW: (255, 255, 0),
    TileColor.GREEN: (0, 255, 0),
    TileColor.BLUE: (0, 255, 255),
    TileColor.PURPLE: (128, 0, 128),
    TileColor.PINK: (255, 105, 180),

}

double_click = Timer(250)

LEVELS = [
       [
            [0, 0, 5, TileColor.RED],
            [3, 3, 9, TileColor.BLUE],
            [3, 6, 10, TileColor.GREEN],
            [4, 3, 7, TileColor.YELLOW],
            [5, 0, 7, TileColor.PURPLE],
            [5, 5, 4, TileColor.ORANGE],
            [6, 0, 4, TileColor.PINK],
            [1, 4, None, TileColor.BLOCK],
            [2, 4, None, TileColor.BLOCK],
            [2, 5, None, TileColor.BLOCK],
       ],
       [
            [0, 5, 3, TileColor.RED],
            [1, 1, 6, TileColor.BLUE],
            [3, 4, 12, TileColor.GREEN],
            [5, 2, 8, TileColor.YELLOW],
            [5, 6, 6, TileColor.PURPLE],
            [6, 0, 7, TileColor.ORANGE],
            [6, 6, 5, TileColor.PINK],
            [1, 6, None, TileColor.BLOCK],
            [5, 3, None, TileColor.BLOCK],
        ],
        [
            [0, 1, 9, TileColor.RED],
            [1, 5, 3, TileColor.BLUE],
            [3, 1, 6, TileColor.GREEN],
            [3, 6, 5, TileColor.YELLOW],
            [4, 3, 4, TileColor.PURPLE],
            [4, 6, 7, TileColor.ORANGE],
            [6, 2, 7, TileColor.PINK],
            [2, 2, None, TileColor.BLOCK],
            [2, 3, None, TileColor.BLOCK],
            [3, 2, None, TileColor.BLOCK],
            [3, 3, None, TileColor.BLOCK],
            [3, 4, None, TileColor.BLOCK],
            [4, 4, None, TileColor.BLOCK],
            [5, 1, None, TileColor.BLOCK],
            [5, 2, None, TileColor.BLOCK],
        ],
]