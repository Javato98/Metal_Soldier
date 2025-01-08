import pygame
from environment_frames import EnvironmentFrames



class Coordinates(EnvironmentFrames):

    def __init__(self, ms_game) -> None:
        super().__init__(ms_game)

        self.flag_cave = False


    def level1(self):

        self.flag_cave = True

        background = [
						
            # Platform 1
            (self.land_middle1, 9, 0, 620),
            (self.land_middle1, 9, 0, 640),
            (self.land_middle1, 9, 0, 660),
            (self.land_middle1, 9, 0, 680),
            (self.land_middle1, 9, 0, 700),
            (self.land_middle1, 9, 0, 720),
            (self.land_middle1, 9, 0, 740),
            (self.land_middle1, 9, 0, 760),
            (self.land_middle1, 9, 0, 780),
            (self.land_middle1, 9, 0, 800), 
            (self.land_middle2, 9, 620, 180, 'y'),
            
            # Platform 2
            (self.land_middle1, 48, 260, 620),
            (self.land_middle1, 48, 260, 640),
            (self.land_middle1, 48, 260, 660),
            (self.land_middle1, 48, 260, 680),
            (self.land_middle1, 48, 260, 700),
            (self.land_middle1, 48, 260, 720),
            (self.land_middle1, 48, 260, 740),
            (self.land_middle1, 48, 260, 760),
            (self.land_middle1, 48, 260, 780),
            (self.land_middle0, 9, 620, 260, 'y'),
            (self.land_up0, 1, 600, 260, 'y'),
            
            # Platform 3
            (self.land_up0, 1, 560, 560, 'y'),
            (self.land_middle0, 1, 580, 560, 'y'),
            (self.land_middle1, 32, 560, 600),
            (self.land_middle1, 32, 580, 580),
            (self.land_middle0, 1, 600, 560, 'y'),
            
            # Platform 4
            (self.land_up0, 1, 520, 800, 'y'),
            (self.land_middle0, 1, 540, 800, 'y'),
            (self.land_middle1, 20, 800, 560),
            (self.land_middle0, 1, 800, 560),

            # Platform 5
            (self.land_middle1, 60, 0, 280),
            (self.land_down1, 60, 0, 300),
            (self.grass1, 1, 100, 240),
            (self.grass1, 1, 300, 240),
            (self.grass0, 1, 340, 240),
            (self.grass1, 1, 500, 240),
            (self.grass0, 1, 900, 240),
            (self.grass0, 1, 140, 240),
            (self.grass1, 1, 200, 240),
            (self.grass1, 1, 220, 240),
            (self.grass0, 1, 700, 240),

            # Prueba
            (self.ivy, 1, 100, 340)
          
          
	]

        platform1 = [(self.land_up2, 10, 0, 600)]
                    
        platform2 = [(self.land_up2, 27, 260, 600)]

        platform3 = [
            (self.land_up2, 12, 560, 560),
            (self.land_middle1, 12, 560, 580)
            ]
            
        platform4 = [
            (self.land_up2, 20, 800, 520),
            (self.land_middle1, 20, 800, 540)
            ]
            
        platform5 = [ 
            (self.land_up2, 60, 0, 260),
            (self.land_middle1, 60, 0, 280),
            (self.land_down1, 60, 0, 300)
            ]
        
  
        stairs = [
            (self.stairs, 10, 260, 1000, 'y')
            ]

        level = {
            'platform1' : platform1,
            'platform2' : platform2,
            'platform3' : platform3,
            'platform4' : platform4,
            'platform5' : platform5,
            'background' : background, 
            'stairs' : stairs
            }

        return level






    
    # def level2(self):

    #     background = [
    #         #Platform 1
    #         (self.land_up[1], 1, 140, 230),
    #         (self.land_middle[0], 1, 140, 250),
    #         (self.land_middle[2], 1, 300, 250),
    #         (self.land_down[0], 1, 140, 270),
    #         (self.land_down[2], 1, 300, 270),

    #         #Platform 2
    #         (self.land_up[1], 1, 380, 230),
    #         (self.land_middle[0], 1, 380, 250),
    #         (self.land_middle[2], 1, 540, 250),
    #         (self.land_down[0], 1, 380, 270),
    #         (self.land_down[2], 1, 540, 270),

    #         #Platform 3
    #         (self.land_up[1], 1, 620, 230),
    #         (self.land_middle[0], 1, 620, 250),
    #         (self.land_middle[2], 1, 780, 250),
    #         (self.land_down[0], 1, 620, 270),
    #         (self.land_down[2], 1, 780, 270),

    #         #Platform 4
    #         (self.land_up[1], 1, 860, 230),
    #         (self.land_middle[0], 1, 860, 250),
    #         (self.land_middle[2], 1, 1020, 250),
    #         (self.land_down[0], 1, 860, 270),
    #         (self.land_down[2], 1, 1020, 270),

    #         #Platform 5
    #         (self.land_up[0], 1, 500, 600),

    #         #Platform 6
            
    #     ]


    #     platform1 = [
    #         (self.land_up[2], 9, 160, 230),
    #         (self.land_middle[1], 9, 160, 250),
    #         (self.land_down[1], 9, 160, 270)
    #     ]
        

    #     platform2 = [
    #         (self.land_up[2], 9, 400, 230),
    #         (self.land_middle[1], 9, 400, 250),
    #         (self.land_down[1], 9, 400, 270)
    #     ]

    #     platform3 = [
    #         (self.land_up[2], 9, 640, 230),
    #         (self.land_middle[1], 9, 640, 250),
    #         (self.land_down[1], 9, 640, 270)
    #     ]

    #     platform4 = [
    #         (self.land_up[2], 9, 880, 230),
    #         (self.land_middle[1], 9, 880, 250),
    #         (self.land_down[1], 9, 880, 270)
    #     ]

    #     platform5 = [
    #         (self.land_down[1], 4, 80, 270)]


    #     platform6 = [
    #         (self.land_up[2], 9, 400, 540),
    #         (self.land_middle[1], 9, 400, 560),
    #         (self.land_down[1], 9, 400, 580)
    #     ]


    #     platform7 = [
    #         (self.land_up[1], 26, 580, 580)
    #     ]

    #     stairs = [
    #         (self.stairs, 3, 230, 520, 'y', 'stairs')
    #     ]



    #     level = [platform1, platform2, platform3, platform4, platform5, platform6, platform7, stairs]

    #     return level
    



    # def level3(self):

    #     platform1 = [
    #         (self.land_up[2], 9, 0, 600),
    #         (self.land_middle[1], 9, 0, 620),
    #         (self.land_middle[1], 9, 0, 640),
    #         (self.land_middle[1], 9, 0, 660),
    #         (self.land_middle[1], 9, 0, 680),
    #         (self.land_middle[1], 9, 0, 700),
    #         (self.land_middle[1], 9, 0, 720),
    #         (self.land_middle[1], 9, 0, 740),
    #         (self.land_middle[1], 9, 0, 760),
    #         (self.land_middle[1], 9, 0, 780),
    #         (self.land_middle[1], 9, 0, 800)

    #         # (self.land_middle[1], 9, 620, 40, 'y'),
    #         # (self.land_middle[1], 9, 620, 60, 'y'),
    #         # (self.land_middle[1], 9, 620, 80, 'y'),
    #         # (self.land_middle[1], 9, 620, 100, 'y'),
    #         # (self.land_middle[1], 9, 620, 120, 'y'),
    #         # (self.land_middle[1], 9, 620, 140, 'y'),
    #         # (self.land_middle[2], 9, 620, 160, 'y'),

    #     ]
        

    #     platform2 = [
    #         (self.land_up[2], 1, 400, 600)
    #     ]

    #     platform3 = [
    #         (self.land_up[2], 6, 700, 600), 
    #         (self.land_up[2], 6, 700, 620),
    #         (self.land_up[2], 6, 700, 640),
    #         (self.land_up[2], 6, 700, 660),
    #         (self.land_up[2], 6, 700, 680),
    #         (self.land_up[2], 6, 700, 700)
    #     ]

    #     platform4 = [
    #         (self.land_up[2], 6, 900, 600), 
    #         (self.land_up[2], 6, 900, 620),
    #         (self.land_up[2], 6, 900, 640),
    #         (self.land_up[2], 6, 900, 660),
    #         (self.land_up[2], 6, 900, 680),
    #         (self.land_up[2], 6, 900, 700)
    #     ]

    #     level = [platform1, platform2, platform3, platform4]

    #     return level






    # self.repeat(self.cave_edges_up[0], 44, 320, 350)
    # self.repeat(self.cave_edges_middle[0], 44, 320, 370)
    # self.repeat(self.cave_edges_down[0], 44, 320, 390)
    

    # self.screen.blit(self.stone_grass[3], (160, 270))
    # self.screen.blit(self.stone_grass[1], (330, 250))
    # self.screen.blit(self.stone_grass[2], (360, 250))
    # self.screen.blit(self.stone_grass[3], (390, 250))
    # self.screen.blit(self.stone_grass[0], (160, 270))


class Platform(pygame.sprite.Sprite):
    def __init__(self, rect):
        super().__init__()
        self.id = id
        self.image = pygame.Surface((rect.width, rect.height))
        self.rect = rect


class Stairs(pygame.sprite.Sprite):
    def __init__(self, rect):
        super().__init__()
        self.id = id
        self.image = pygame.Surface((rect.width, rect.height))
        self.rect = rect