from resources import *

button_image_path = './images/button.png'
print(f"Ruta de la imagen del botón: {button_image_path}")

class Button:
    def __init__(self, text, x, y, width, height, image, font, size, text_color, border_color=BLACK):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = image
        self.font = font
        self.size = size
        self.text_color = text_color
        self.border_color = border_color
        print(f"Creando botón: '{text}' en posición ({x}, {y}) con tamaño ({width}, {height})")

# Creación de los botones del juego
print("Inicializando botones...")
StartButton = Button("JUGAR!", 650, 125, 315, 100, button_image_path, FONT9, 15, BROWN)
Creditsbutton = Button("Creditos", 650, 199, 315, 100, button_image_path, FONT9, 15, BROWN)
ExitButton = Button("Salir", 650, 275, 315, 100, button_image_path, FONT9, 15, BROWN)
BackButton = Button("←", 10, 10, 150, 75, button_image_path, FONT9, 20, BROWN)

def viewButtons():
    if DEBUG_MODE:
        print("> Mostrando botones principales")
    drawButton(StartButton)
    drawButton(Creditsbutton)
    drawButton(ExitButton)

def viewBackButton():
    if DEBUG_MODE:
        print("> Mostrando botón de regreso")
    drawButton(BackButton)