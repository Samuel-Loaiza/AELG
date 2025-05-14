import pygame, sys, psutil
from resources import *
from init import *

# Modo de depuración

def Debuglog():
    global Current_Screen
    if DEBUG_MODE:
        print("Modo de depuración activado")
        print("\n--- NUEVO FRAME ---")

        # Mostrar información sobre los eventos
        print(f"Eventos capturados: {len(GameResources.EVENTS)}")
        for event in GameResources.EVENTS:
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(f"Clic en posición: {event.pos}")
            elif event.type == QUIT:
                print("Evento QUIT detectado")
            elif event.type == KEYDOWN:
                print(f"Tecla presionada: {event.key}")

        # Mostrar FPS actual
        fps_actual = round(CLOCK.get_fps(), 1)
        print(f"FPS: {fps_actual}")
                        
        # Informar sobre la memoria utilizada (esto requiere el módulo psutil)
        try:
            process = psutil.Process()
            memory_info = process.memory_info()
            print(f"Memoria utilizada: {memory_info.rss / 1024 / 1024:.2f} MB")
        except ImportError:
            pass  # No hacer nada si psutil no está instalado

        # Mostrar información sobre la pantalla actual
        print("\n--- Loop de juego: Current_Screen = '{}' ---".format(Current_Screen))
        if Current_Screen == "main":
            print("Renderizando pantalla principal (main)")
        elif Current_Screen == "start_game":
            print("Renderizando pantalla de inicio del juego (start_game)")
        elif Current_Screen == "window_credit":
            print("Renderizando pantalla de créditos (window_credit)")
        else:
            print(f"ERROR: Pantalla no reconocida: '{Current_Screen}'")
            Current_Screen = "main"
    else:
        print("Modo de depuración desactivado")