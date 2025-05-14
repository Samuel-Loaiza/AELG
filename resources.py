import pygame
from pygame.locals import  QUIT, KEYDOWN, K_DOWN

pygame.init()
pygame.font.init()

FPS = 30

CLOCK = pygame.time.Clock()

window = pygame.display.set_mode((1024, 600))

pygame.display.set_caption('Aprendizaje en la Granja')

WINDOW_WIDTH, WINDOW_HIGH = size = window.get_size()

class GameResources:

    pygame.init()

    EVENTS = pygame.event.get()

    GAMES_ACTIVE = True

# Activar o desactivar el modo de depuración
DEBUG_MODE = False

#COLORES: 

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
ORANGE = (255,165,0)
PURPLE = (128,0,128)
CYAN = (0,255,255)
BROWN = (165,42,42)
PINK = (255,192,203)
LIGHT_GRAY = (211, 211, 211)
DARK_GRAY = (169, 169, 169)
LIGHT_BLUE = (173, 216, 230)
LIGHT_GREEN = (144, 238, 144)
LIGHT_RED = (255, 182, 193)

#FONTS:

FONT1 = '2Dumb.ttf'
FONT2 = 'ChancesSketch.ttf'
FONT3 = 'alpha_echo.ttf'
FONT4 = 'plexifont.ttf'
FONT5 = 'Top_Secret.ttf'
FONT6 = 'VT323-Regular.ttf'
FONT7 = 'ChancesSolid.ttf'
FONT8 = 'Happy Farmhouse.otf'
FONT9 = 'PressStart2P.ttf'

#FUNCIONES GLOBALES:

def DrawTextWithBorder(text, font, color, border_color, border_offset, center):
    text_surface = font.render(text, True, color)
    border_surface = pygame.Surface(
        (text_surface.get_width() + 2 * border_offset, text_surface.get_height() + 2 * border_offset),
        pygame.SRCALPHA
    )
    for dx, dy in [(-border_offset, 0), (border_offset, 0), (0, -border_offset), (0, border_offset),
                   (-border_offset, -border_offset), (-border_offset, border_offset),
                   (border_offset, -border_offset), (border_offset, border_offset)]:
        border_text = font.render(text, True, border_color)
        border_surface.blit(border_text, (dx + border_offset, dy + border_offset))
    border_surface.blit(text_surface, (border_offset, border_offset))
    text_rect = border_surface.get_rect(center=center)
    window.blit(border_surface, text_rect)

def loadFont(font_path, size):
    try:
        font = pygame.font.Font(font_path, size)
        return font
    except FileNotFoundError:
        print(f"Error: No se pudo cargar la fuente '{font_path}'.")
        return None

def loadImage(image_path):
    try:
        image = pygame.image.load(image_path).convert_alpha()
        return image
    except FileNotFoundError:
        print(f"Error: No se pudo cargar la imagen '{image_path}'.")
        return None
    
def loadSound(sound_path):
    try:
        sound = pygame.mixer.Sound(sound_path)
        return sound
    except FileNotFoundError:
        print(f"Error: No se pudo cargar el sonido '{sound_path}'.")
        return None

def IsMouseHovering(button):
    mouse_pos = pygame.mouse.get_pos()
    rect = pygame.Rect(button.x, button.y, button.width, button.height)
    return rect.collidepoint(mouse_pos)

def GetButtonDimensions(button, is_hovered):
    scale_factor = 1.05 if is_hovered else 1.0
    set_width = int(button.width * scale_factor)
    set_height = int(button.height * scale_factor)
    set_x = button.x - (set_width - button.width) // 2
    set_y = button.y - (set_height - button.height) // 2
    return set_x, set_y, set_width, set_height

def PressButton(button, events):
    rect = pygame.Rect(button.x, button.y, button.width, button.height)
    for event in events:
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(f"> Evento de clic detectado en posición: {mouse_pos}")
            print(f"> ¿Colisión con el botón? {rect.collidepoint(mouse_pos)}")
            if rect.collidepoint(event.pos):
                print(f"> Botón '{button.text}' presionado")
                return True
    return False

#FUNCIONES:

def MainWindow(background):
    window.blit(background.image,(background.position,0))

def MainTitle(text):
    tipeletter = loadFont('./fonts/' + text["letter"], text["size"])
    y_offset = 0
    for line in text["text"]:
        text_center = (text["x"], text["y"] + y_offset)
        DrawTextWithBorder(line, tipeletter, text["color"], BLACK, 2, text_center)
        y_offset += tipeletter.get_height() + 5

def StartWindow(background):
    window.blit(background.image,(background.position,0))

def CreditsWindow(background, text):
    window.blit(background.image, (background.position, 0))
    tipeletter = loadFont('./fonts/' + text.letter, text.size)
    y_offset = 0
    for line in text.text:
        text_center = (text.x, text.y + y_offset)
        DrawTextWithBorder(line, tipeletter, text.color, BLACK, 1.5, text_center)
        y_offset += tipeletter.get_height() + 5

def LoadButtonImage(button):
    return loadImage(button.image)

def drawButton(button):
    button_image = loadImage(button.image)
    is_hovered = IsMouseHovering(button)
    set_x, set_y, set_width, set_height = GetButtonDimensions(button, is_hovered)
    button_image = pygame.transform.scale(button_image, (set_width, set_height))
    window.blit(button_image, (set_x, set_y))
    drawButtonText(button, set_x, set_y, set_width, set_height)

def drawButtonText(button, set_x, set_y, set_width, set_height):
    tipeletter = loadFont('./fonts/' + button.font, button.size)
    text_center = (set_x + set_width // 2, set_y + set_height // 2)
    DrawTextWithBorder(button.text, tipeletter, button.text_color, button.border_color, 1.5, text_center)

def MainButtonCore(button):
    button_image = LoadButtonImage(button)
    is_hovered = IsMouseHovering(button)
    set_x, set_y, set_width, set_height = GetButtonDimensions(button, is_hovered)
    drawButton(button_image, set_x, set_y, set_width, set_height)
    drawButtonText(button, set_x, set_y, set_width, set_height)