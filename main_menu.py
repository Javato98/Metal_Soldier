import pygame.font
from paths import Paths


class Menu():
    def __init__(self, ms_game):
        self.button_texts = ["Play", "Instructions", "Exit"]
        self.ms_game = ms_game
        self.screen = ms_game.screen
        self.screen_rect = self.screen.get_rect()
        self.desplace_button_position = 0
        self.buttons = []

        self.create_buttons()

    def title(self, path="resources/fonts/title.png"):
        create_title_image = pygame.image.load(path).convert_alpha()
        title_image = create_title_image.copy()
        title_image_rect = title_image.get_rect()
        title_image_rect.center = self.screen_rect.center
        title_image_rect.y -= 200
        self.screen.blit(title_image, title_image_rect)


    def title_level(self, level):
        title_image = level.copy()  
        title_image_rect = title_image.get_rect()
        title_image_rect.center = self.screen_rect.center
        title_image_rect.y += 50
        self.screen.blit(title_image, title_image_rect)


    def create_buttons(self):
        for text in self.button_texts:
            button = Button(self.ms_game, text)
            button.rect.y = button.rect.y - self.desplace_button_position
            button.msg_image_rect.y = button.rect.y + 10
            self.buttons.append(button)
            self.desplace_button_position -= 100

            
    def create_menu(self):
        for button in self.buttons:
            button.draw_button()


    def show_instructions(self):
        pygame.display.set_caption("Juego con Instrucciones")

        # Colores
        WHITE = (59, 86, 97) 
        YELLOW = (255, 255, 58)

        # Fuente
        font = pygame.font.Font("resources/fonts/Retro Gaming.ttf", 30)
        running = True

        # Imagenes
        def save_images_keyboard():
            images_keys = []
            paths_keys = ["left-right.png", "up.png", "down.png", "space.png", "letter-k.png"]
            
            for path in paths_keys:
                image_key_path = Paths(f'resources\\Images keys instructions\\{path}').__str__()
                image_key = pygame.image.load(image_key_path).convert_alpha()
                images_keys.append(image_key)
            return images_keys
        
        images_keys = save_images_keyboard()


        while running:
            self.screen.fill(WHITE)

            # Texto de instrucciones
            instructions = (
                "Instrucciones del Juego:",
                ("1. Usa las flechas para moverte", images_keys[0]),
                ("2. Presiona UP para saltar", images_keys[1]),
                ("3. Presiona DOWN para agacharte", images_keys[2]),
                ("4. Presiona ESPACIO para disparar", images_keys[3]),
                ("5. Presiona K para apuñalar", images_keys[4]),
                "Presiona ESC para volver",
            )

            y = 60
            x = 230

            for line in instructions:
                if isinstance(line, tuple):
                    for item in line:
                        if isinstance(item, str):
                           text = font.render(item, True, YELLOW)
                           self.screen.blit(text, (x, y))
                        else:
                            self.screen.blit(item, (980, y-30))

                else:
                    text = font.render(line, True, (255, 150, 0))
                    self.screen.blit(text, (x-50, y))
                y += 105

            pygame.display.flip()

            # Manejo de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # Volver al juego
                        running = False
            



class Button():

    def __init__(self, ms_game, msg):
        '''Inicializa los atributos del botón'''
        self.screen = ms_game.screen
        self.screen_rect = self.screen.get_rect()

        # EConfigura las dimensiones y propiedades del botón
        self.width, self.height = 200, 80
        self.text_color = (255, 255, 58)
        self.font = pygame.font.Font("resources/fonts/Retro Gaming.ttf", 48)

        # Creamos el objeto rect botón y lo centramos 
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # Preparamos el mensaje del botón
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        '''Convierte el texto en una imagen renderizada y lo centra en el centro'''
        self.msg_image = self.font.render(msg, True, self.text_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center



    def draw_button(self):
        '''Dibuja un botón en blanco y luego el mensaje'''
        self.screen.blit(self.msg_image, self.msg_image_rect)


