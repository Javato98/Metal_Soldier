import pygame
from environment_frames import EnvironmentFrames



class Coordinates(EnvironmentFrames):

    def __init__(self, ms_game) -> None:
        super().__init__(ms_game)
        



    def level1(self):


        platform1 = [
            (self.land_up[0], 1, 0, 230),
            (self.land_up[1], 10, 0, 230),
            (self.land_middle[2], 28, 250, 180, 'y'),
            (self.land_middle[1], 28, 250, 160, 'y'),
            (self.land_middle[1], 28, 250, 140, 'y'),
            (self.land_middle[1], 28, 250, 120, 'y'),
            (self.land_middle[1], 28, 250, 100, 'y'),
            (self.land_middle[1], 28, 250, 80, 'y'),
            (self.land_middle[1], 28, 250, 60, 'y'),
            (self.land_middle[1], 28, 250, 40, 'y'),
            (self.land_middle[1], 28, 250, 20, 'y'),
            (self.land_middle[1], 28, 250, 0, 'y')
        ]
        
        platform2 = [
            (self.land_up[0], 1, 300, 230),
            (self.land_up[1], 44, 320, 230),
            (self.land_middle[0], 5, 250, 300, 'y'),
            (self.land_middle[1], 44, 320, 250),
            (self.land_middle[1], 44, 320, 270),
            (self.land_middle[1], 44, 320, 290),
            (self.land_middle[1], 44, 320, 310),
            (self.land_down[0], 44, 320, 330)
        ]

        level = [platform1, platform2]

        return level

    
    def level2(self):

        background = [
            #Platform 1
            (self.land_up[1], 1, 140, 230),
            (self.land_middle[0], 1, 140, 250),
            (self.land_middle[2], 1, 300, 250),
            (self.land_down[0], 1, 140, 270),
            (self.land_down[2], 1, 300, 270),

            #Platform 2
            (self.land_up[1], 1, 380, 230),
            (self.land_middle[0], 1, 380, 250),
            (self.land_middle[2], 1, 540, 250),
            (self.land_down[0], 1, 380, 270),
            (self.land_down[2], 1, 540, 270),

            #Platform 3
            (self.land_up[1], 1, 620, 230),
            (self.land_middle[0], 1, 620, 250),
            (self.land_middle[2], 1, 780, 250),
            (self.land_down[0], 1, 620, 270),
            (self.land_down[2], 1, 780, 270),

            #Platform 4
            (self.land_up[1], 1, 860, 230),
            (self.land_middle[0], 1, 860, 250),
            (self.land_middle[2], 1, 1020, 250),
            (self.land_down[0], 1, 860, 270),
            (self.land_down[2], 1, 1020, 270),

            #Platform 5
            (self.land_up[0], 1, 500, 600),

            #Platform 6
            
        ]


        platform1 = [
            (self.land_up[2], 9, 160, 230),
            (self.land_middle[1], 9, 160, 250),
            (self.land_down[1], 9, 160, 270)
        ]
        

        platform2 = [
            (self.land_up[2], 9, 400, 230),
            (self.land_middle[1], 9, 400, 250),
            (self.land_down[1], 9, 400, 270)
        ]

        platform3 = [
            (self.land_up[2], 9, 640, 230),
            (self.land_middle[1], 9, 640, 250),
            (self.land_down[1], 9, 640, 270)
        ]

        platform4 = [
            (self.land_up[2], 9, 880, 230),
            (self.land_middle[1], 9, 880, 250),
            (self.land_down[1], 9, 880, 270)
        ]

        platform5 = [
            (self.land_down[1], 4, 80, 270)]

        

        platform6 = [
            (self.land_up[2], 9, 400, 540),
            (self.land_middle[1], 9, 400, 560),
            (self.land_down[1], 9, 400, 580)
        ]

        platform6 = [
            (self.land_up[2], 9, 400, 540),
            (self.land_middle[1], 9, 400, 560),
            (self.land_down[1], 9, 400, 580)
        ]


        platform7 = [
            (self.land_up[1], 31, 520, 580)
        ]

        stairs = [
            (self.stairs, 3, 230, 520, 'y', 'stairs')
        ]



        level = [platform1, platform2, platform3, platform4, platform5, platform6, platform7, stairs]

                    


        return level

    

    # self.repeat(self.cave_edges_up[0], 44, 320, 350)
    # self.repeat(self.cave_edges_middle[0], 44, 320, 370)
    # self.repeat(self.cave_edges_down[0], 44, 320, 390)
    

    # self.screen.blit(self.stone_grass[3], (160, 270))
    # self.screen.blit(self.stone_grass[1], (330, 250))
    # self.screen.blit(self.stone_grass[2], (360, 250))
    # self.screen.blit(self.stone_grass[3], (390, 250))
    # self.screen.blit(self.stone_grass[0], (160, 270))


class Platform(pygame.sprite.Sprite):
    def __init__(self, rect, id='platform'):
        super().__init__()
        self.id = id
        self.image = pygame.Surface((rect.width, rect.height))
        self.rect = rect