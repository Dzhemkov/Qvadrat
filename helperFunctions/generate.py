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


            #print(button.__dict__)
            if button.left_clicked:
                print(f"{button.number}, {button.color}")

def get_button_at_mouse(self):
    mouse_pos = pygame.mouse.get_pos()

    for row in self.buttons:
        for button in row:
            if button.rect.collidepoint(mouse_pos):
                return button

    return None