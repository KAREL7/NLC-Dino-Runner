import pygame
import random
from dino_runner.components.obstacles.bird import Bird

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import BIRD, DEAD_IMAGE, DEAD_SOUND, SMALL_CACTUS, LARGE_CACTUS, EXPLOSION

class ObstacleManager:
    
    def __init__(self):
        self.obstacles = []
        
    def update(self, game):

        if len(self.obstacles) == 0:
            small_cactus = Cactus(SMALL_CACTUS)
            large_cactus = Cactus(LARGE_CACTUS)
            bird = Bird(BIRD)
            change_cactus = random.randint(0,2)
            if change_cactus == 0:
                self.obstacles.append(small_cactus)
            elif change_cactus == 1:
                self.obstacles.append(large_cactus)
            else:
                self.obstacles.append(bird)


        for i in self.obstacles:
            i.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(i.rect):
                if not game.player.shield:
                    game.player.image = DEAD_IMAGE
                    DEAD_SOUND.play()
                    pygame.time.delay(800)
                    game.playing = False
                    game.death_count += 1
                else:
                    self.obstacles.remove(i)
                break

    def draw(self, screen):
        for i in self.obstacles:
            i.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
