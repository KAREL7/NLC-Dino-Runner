import random

from dino_runner.components.obstacles.obstacle import Obstacle

class Bird(Obstacle):

    def __init__(self, image):
        self.type_image = random.randint(0, 1)
        super().__init__(image, self.type_image)
        rand_position = random.randint(0, 1)
        
        if rand_position == 1:
            self.rect.y = 240
        else:
            self.rect.y = 310