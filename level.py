from resources import *

OBJECTS_SCENERY = [
    Elements(200, 150, 60, 60),  # Roca
    Elements(500, 400, 50, 80)   # Árbol
    ]

def DrawElements():
    for obj in OBJECTS_SCENERY:
        pygame.draw.rect(window, (100, 100, 100), obj)  # Color gris para objetos