from multiprocessing.pool import RUN
import pygame 

from pygame.sprite import Sprite
from dino_runner.utils.constants import DUCKING_SHIELD, JUMPING_SHIELD, RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, RUNNING_SHIELD, SHIELD_TYPE

DUCK_IMAGE = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD}
RUN_IMAGE = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD}
JUMP_IMAGE = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD}

class Dinosaur(Sprite):
    X_POS = 80
    Y_POS = 310
    JUMP_VEL = 8.5
    Y_POS_DUCK = 350

    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMAGE [self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.dino_jump_vel = self.JUMP_VEL
        self.setup_state()

    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.show_text = False
        self.shield_time_out = 0

    def verify(self):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

    def update(self, user_input):
        self.verify()
        
        if user_input [pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_jump = False
            self.dino_run = False
        elif (user_input [pygame. K_UP] or user_input[pygame.K_SPACE]) and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif not self.dino_jump:
            self.dino_run = True
            self.dino_jump = False
            self.dino_duck = False

        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        self.image = RUN_IMAGE[self.type][self.step_index // 5]  
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMAGE[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.dino_jump_vel * 4
            self.dino_jump_vel -= 0.8

        if self.dino_jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.dino_jump_vel = self.JUMP_VEL

    def duck(self):
        self.image = DUCK_IMAGE[self.type][self.step_index // 5] 
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def check_invi(self):
        pass


    def draw(self, screen: pygame.Surface):
        screen.blit(self.image , (self.dino_rect.x , self.dino_rect.y))
        