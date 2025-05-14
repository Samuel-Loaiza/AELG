from button import *
from resources import *
import pygame

class Window:
    def __init__(self, background_image_path):
        self.background = loadImage(background_image_path)
        self.background = pygame.transform.scale(self.background, (WINDOW_WIDTH, WINDOW_HIGH))
        self.position = 0
        self.image = self.background
        print(f"Inicializando ventana con imagen: {background_image_path}")
        
    def render_background(self):
        window.blit(self.background, (0, 0))
        
    def handle_events(self, events):
        pass
        
    def render(self):
        self.render_background()

class MainMenuWindow(Window):
    def __init__(self):
        super().__init__("./images/background/background1.png")
        self.title = {
            "text": ["—————————————", "Aprendizaje", "en la Granja", "—————————————"],
            "letter": FONT9,
            "color": LIGHT_BLUE,
            "x": 250,
            "y": 180,
            "size": 30
        }
        print("Inicializando ventana del menú principal")
        
    def render(self):
        super().render()
        MainTitle(self.title)
        viewButtons()
        
class StartGameWindow(Window):
    def __init__(self):
        super().__init__("./images/background/background2.png")
        print("Inicilizando ventana de inicio de juego")
            
    def render(self):
        super().render()
        viewBackButton()
        if DEBUG_MODE:
            print("Renderizando StartGameWindow y botón de regreso")

class CreditsGameWindow(Window):
    def __init__(self):
        super().__init__("./images/background/background2.png")
        self.credits = {
            "text": ["Samuel Loaiza González", "Juan David", "Luis Fernando Contreras"],
            "letter": FONT9,
            "color": LIGHT_GREEN,
            "x": 400,
            "y": 100,
            "size": 24
        }
        print("Inicializando ventana de créditos")
            
    def render(self):
        super().render()
        MainTitle(self.credits)
        viewBackButton()
        if DEBUG_MODE:
            print("Renderizando CreditsGameWindow y botón de regreso")