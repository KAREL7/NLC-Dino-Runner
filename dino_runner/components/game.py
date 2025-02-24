
import pygame
import math
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import BG, CLOUD, ICON, POINTS_SOUND, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.playing = False
        self.runing = False
        self.game_speed = 15
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.points = 0
        self.points_max = 0
        self.points_game = 0
        self.death_count = 0
        self.lives = 3


    def font_custom (self, font, size):
        font_style = pygame.font.SysFont(font, size)
        return font_style

    def execute_game(self):
        self.runing = True
        while self.runing:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def run(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.playing = True
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.update_score()
        user_input = pygame.key.get_pressed()     #Return the key pressed
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(math.trunc(self.points), math.trunc(self.game_speed), self.player)

    def reset_game(self):
        self.points = 0
        self.game_speed = 15    
    
    def update_score(self):
        self.points += 0.2
        if math.trunc (self.points) % 10 == 0:
            self.game_speed += 0.2

        """if math.trunc (self.points) > 0 and math.trunc (self.points) % 100 == 0:
                POINTS_SOUND.play()"""
    
        self.points_game = self.points
        if self.points_game >= self.points_max:
            self.points_max = self.points_game
          
    def draw_score(self):
        font = self.font_custom('rockwellnegritacursiva', 30)
        text = font.render (f'Points : {math.trunc(self.points)}', True, (128,128,128))
        text_rect = text.get_rect()
        text_rect.center = (150,50)
        self.screen.blit(text, text_rect)

        if self.points % 100 == 0:
            POINTS_SOUND.play()

        """text1 = font.render (f'Points Max : {self.points_max}', True, (128,128,128))
        text_rect1 = text.get_rect()
        text_rect1.center = (100,50)
        self.screen.blit(text1, text_rect1)"""

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.runing = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0: 
            font = self.font_custom('garamondcursiva', 40)
            text = font.render ('Press any Key to Start the Game', True, (0,0,0))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width, half_screen_height)
            self.screen.blit(text, text_rect)

        elif self.death_count > 0 :
            font = self.font_custom('garamondcursiva', 40)
            text = font.render ('GAME OVER', True, (0,0,0))
            text_restart = font.render ('Press any key to Start a new Game', True, (0,0,0))
            text_score = font.render (f'Score : {math.trunc(self.points_game)}', True, (128,128,128))
            text_score_max = font.render (f'Score Max : {math.trunc(self.points_max)}', True, (128,128,128))
            text_rect = text.get_rect()
            text_rect.center = (half_screen_width - 25, half_screen_height)
            self.screen.blit(text, text_rect)
            self.screen.blit(text_score, (half_screen_width - 100 , half_screen_height + 50))
            self.screen.blit(text_score_max, (half_screen_width - 135, half_screen_height + 80))
            self.screen.blit(text_restart, (half_screen_width - 262 , half_screen_height + 120))
            
        self.screen.blit(RUNNING[0], (half_screen_width - 53, half_screen_height - 120))
        pygame.display.update()
        self.handle_key_events_on_menu()

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.draw_score()
        self.player.draw(self.screen)
        self.player.check_invi(self.screen)
        self.player.check_hammer(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed


        
        
    

