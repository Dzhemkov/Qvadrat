from helperFunctions.global_constants import *


class Button:
    def __init__(self, x, y, tile_size):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x * tile_size, self.y * tile_size, tile_size, tile_size)
        self.left_clicked = False
        self.right_clicked = False
        self.hover = False
        self.number = None
        self.color = TileColor.OPEN
        self.clear = False
        #self.selected = False

    def draw(self, field, row_idx, col_idx):
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            self.hover = True
            if pygame.mouse.get_pressed()[0] == 1 and not self.left_clicked:
                self.left_clicked = True
                #self.clear = True

                if self.clear:
                    self.clear_tiles(field, self.y, self.x)
                    self.clear = False

            if pygame.mouse.get_pressed()[2] == 1 and not self.right_clicked:
                self.right_clicked = True
        else:
            self.hover = False

        if pygame.mouse.get_pressed()[0] == 0:
            self.left_clicked = False
        if pygame.mouse.get_pressed()[2] == 0:
            self.right_clicked = False


    def clear_tiles(self, field, row_idx, col_idx):
        pass