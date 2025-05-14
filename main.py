import pygame, sys
from init import *
from debug import *

if __name__ == '__main__':
    print("=== INICIANDO EL JUEGO ===")
    
    # Bucle principal del juego
    while True:
        
        # Capturar todos los eventos de pygame
        GameResources.EVENTS = pygame.event.get()

        # Procesar eventos para salir del juego
        for event in GameResources.EVENTS:
            if event.type == QUIT or (event.type == KEYDOWN and event.key == pygame.K_ESCAPE):
                print("Saliendo del juego...")
                pygame.quit()
                sys.exit()
                    
        # Limpiar la ventana
        window.fill(WHITE)

        # Ejecutar el ciclo principal del juego
        GameLoop()
        Debuglog()

        # Actualizar la pantalla
        pygame.display.update()