import pygame

from turtle import delay

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS

class ObstacleManager:
    
    def __init__(self):
        self.obstacles = []
        
    def update(self, game):
        if len(self.obstacles) == 0:
            small_cactus = Cactus(SMALL_CACTUS)
            self.obstacles.append(small_cactus)

        for i in self.obstacles:
            i.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(i.rect):
                pygame.time.delay(500)
                game.playing = False
                break
    def draw(self, screen):
        for i in self.obstacles:
            i.draw(screen)
