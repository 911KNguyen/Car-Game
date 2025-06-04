import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

class My_sprite:
    def __init__(self, image_file_name: str, location: tuple[int, int] = (0, 0)):
        self.image = pygame.image.load(image_file_name)
        self.location = location

    def get_image(self) -> pygame.Surface:
        return self.image

    def get_width(self) -> int:
        return self.image.get_width()

    def get_height(self) -> int:
        return self.image.get_height()

