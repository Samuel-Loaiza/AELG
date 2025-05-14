import pygame, sys
from resources import *
from window import *
from button import *

# Variable global para controlar la pantalla actual
Current_Screen = "main"
print(f"Inicializando con Current_Screen = '{Current_Screen}'")

# Inicialización de ventanas
main_menu_window = MainMenuWindow()
start_game_window = StartGameWindow()
credits_window = CreditsGameWindow()

def GameLoop():
    global Current_Screen

    # Verificamos eventos de botones para la pantalla principal
    if Current_Screen == "main":
        main_menu_window.render()
        

        # Comprobamos si se ha pulsado algún botón
        start_pressed = PressButton(StartButton, GameResources.EVENTS)
        credits_pressed = PressButton(Creditsbutton, GameResources.EVENTS)
        exit_pressed = PressButton(ExitButton, GameResources.EVENTS)
        
        if start_pressed:
            print(f"Current_Screen antes del cambio: {Current_Screen}")
            Current_Screen = "start_game"
            print(f"Cambiando de 'main' a {Current_Screen}")
        elif credits_pressed:
            print(f"Current_Screen antes del cambio: {Current_Screen}")
            Current_Screen = "window_credit"
            print(f"Cambiando de 'main' a {Current_Screen}")
        elif exit_pressed:
            print("Saliendo del juego")
            pygame.quit()
            sys.exit()
            
    # Manejamos la pantalla de inicio del juego
    elif Current_Screen == "start_game":
        start_game_window.render()
        if PressButton(BackButton, GameResources.EVENTS):
            print("Regresando a 'main'")
            Current_Screen = "main"
        
    # Manejamos la pantalla de créditos
    elif Current_Screen == "window_credit":
        credits_window.render()
        if PressButton(BackButton, GameResources.EVENTS):
            print("Regresando a 'main'")
            Current_Screen = "main"