import pygame
from paths import Paths
from soldier import Soldier


class Scoreboard:
    def __init__(self, ms_game):
        self.soldier = Soldier(ms_game)
        self.screen = ms_game.screen
        self.hearts = self.prep_heart(self.soldier.hearts)
        self.times_touched = self.prep_touched(self.soldier.times_touched)

        
    def prep_heart(self, soldier_hearts):
        hearts = pygame.sprite.Group()
        position_x = 50

        for heart_number in range(soldier_hearts):
            heart = Heart()
            hearts.add(heart)
            heart.rect.x += position_x * heart_number + 20
            heart.rect.y += 20

        return hearts

    def prep_touched(self, times_soldier_touched):
        touched_group = pygame.sprite.Group()
        position_x = 1140

        for touched_number in range(times_soldier_touched):
            touched = Touched()
            touched_group.add(touched)
            touched_width = touched.rect.width
            touched.rect.x = position_x - (touched_width * touched_number) - (20 * touched_number)
            touched.rect.y += 20

        return touched_group


    def draw(self):
        for heart in self.hearts:
            self.screen.blit(heart.image, heart.rect)

        for touched in self.times_touched:
            self.screen.blit(touched.image, touched.rect)

            



class Heart(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.path_image = Paths('resources\\heart pixel art\\heart pixel art 32x32.png').__str__()
        self.image = pygame.image.load(self.path_image)
        self.rect = self.image.get_rect()


class Touched(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.path_image = Paths('resources\\pixel_char_pack\\Player\\Sprites\\player_be_shoted_adjusted_40x40.png').__str__()
        self.image = pygame.image.load(self.path_image)
        self.rect = self.image.get_rect()



