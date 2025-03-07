
import pygame
from paths import Paths

class Music():
    def __init__(self):
        self.relative_path = 'resources\\Sounds\\Music\\'
        self.flag_level = True
        

    def get_abs_path(self, song):
        path_song = self.relative_path + song
        absolute_path_song = Paths(path_song).__str__()
        return absolute_path_song
    
    def play_song(self, song):
        absolute_path_song = self.get_abs_path(song)
        pygame.mixer.music.load(absolute_path_song)
        pygame.mixer.music.play()

    def set_music_level(self, level):

        if self.flag_level:
            if level == 0:
                self.play_song('Lullaby p1.mp3')
            elif level == 1:
                self.play_song('On fire.mp3')
            elif level == 2:
                self.play_song('Funky.mp3')
            elif level == 3:
                self.play_song('On fire.mp3')
            self.flag_level = False

    def handle_transition_songs(self):
        self.flag_level = False
        pygame.mixer.music.stop()


class EffectsSound(Music):
    def __init__(self):
        self.relative_path = 'resources\\Sounds\\Effects Sound\\'
        self.voice_game_over_path = self.get_abs_path('Game Over Voice.mp3')
        self.game_over_sound_path = self.get_abs_path('Game Over Sound 2.mp3')

    def play_sound(self, sound):
        absolute_path_sound = self.get_abs_path(sound)
        sound = pygame.mixer.Sound(absolute_path_sound)
        sound.play()
    
    def sound_game_over(self, check_game_over):
        check_finish_game_over_sound = self.is_finish_sound_game_over()
        if check_game_over:
            pygame.mixer.music.load(self.game_over_sound_path)
            pygame.mixer.music.play()
        elif check_finish_game_over_sound:
            pygame.mixer.music.load(self.voice_game_over_path)
            pygame.mixer.music.play()
        

    def is_finish_sound_game_over(self):
        if not pygame.mixer.music.get_busy():
            return True

            
        

        

        



        
    
        



    