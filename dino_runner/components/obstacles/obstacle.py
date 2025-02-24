from pygame.sprite import Sprite
from dino_runner.utils.constants import BIRD, SCREEN_WIDTH

class Obstacle(Sprite):

    def __init__(self, image, type_image):
        self.image = image
        self.type_image = type_image
        self.rect = self.image[self.type_image].get_rect()
        self.rect.x = SCREEN_WIDTH
        
    def update(self, game_speed, obstacles):

        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()


    def draw(self, screen):
        screen.blit(self.image[self.type_image] , self.rect)
