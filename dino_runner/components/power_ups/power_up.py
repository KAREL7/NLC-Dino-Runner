import random
from turtle import Screen
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH


class PowerUp(Sprite):
    def __init__(self, image, type_pu):
        self.image = image
        self.rect = image.get_rect()
        self.type = type_pu
        self.rect.y = random.randint(100, 150)
        self.rect.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.start_time = 0


    def update(self, game_speed, power_ups):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            power_ups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)