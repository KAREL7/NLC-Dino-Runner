import pygame
import random

from turtle import delay
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS


class ObstacleManager:
    
    def __init__(self):
        self.obstacles = []
        
    def update(self, game):

        if len(self.obstacles) == 0:
            small_cactus = Cactus(SMALL_CACTUS)
            large_cactus = Cactus(LARGE_CACTUS)
            change_cactus = random.randint(0,1)
            if change_cactus == 1:
                self.obstacles.append(small_cactus)
            else:
                self.obstacles.append(large_cactus)

        for i in self.obstacles:
            i.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(i.rect):
                pygame.time.delay(500)
                game.points = 0
                game.game_speed = 20
                game.playing = False
                game.death_count += 1
                break

    def draw(self, screen):
        for i in self.obstacles:
            i.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
