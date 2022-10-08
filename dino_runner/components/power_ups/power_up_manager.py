import pygame
import random
from dino_runner.components.power_ups.shield import Shield
from dino_runner.components.power_ups.hammer import Hammer

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.spawn = 0

    def generate_porwer_ups(self, points):
        
        if len(self.power_ups) == 0:
            if self.spawn == points:
                self.spawn = random.randint(self.spawn * 2, self.spawn * 3)
                change_power_up = random.randint(0,1)

                if change_power_up == 1:
                    self.power_ups.append(Shield())
                else:
                    self.power_ups.append(Hammer())

    def update(self, points, game_speed, player):
        self.generate_porwer_ups(points)
        for i in self.power_ups:
            i.update(game_speed, self.power_ups)
            
            if player.dino_rect.colliderect(i.rect):
                i.start_time = pygame.time.get_ticks()
                player.shield = True
                player.show_text = True
                player.type = i.type
                time_random = random.randint(5, 8)
                player.shield_time_out = i.start_time + (time_random * 1000)
                self.power_ups.remove(i)

    def draw(self, screen):
        for i in self.power_ups:
            i.draw(screen)

    def reset_power_ups(self):
        self.power_ups = []
        self.spawn = random.randint(50, 100)
