import pygame, sys
from resources import *
from window import *
from button import *
from player import *
from level import *
from animals_system import animal_manager
from inventory import player_inventory, resource_manager

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
        
        # Manejar eventos especiales del juego
        HandleGameEvents()
        
        # Actualizar sistemas del juego
        animal_manager.update()
        player_inventory.update()
        resource_manager.update()
        
        # Movimiento del jugador y elementos del nivel
        MotionPlayer()
        DrawElements()
        
        # Recolección de recursos
        resource_manager.collect_resource(GetPlayerPosition(), (width_player, high_player), player_inventory)
        
        # Dibujar recursos
        resource_manager.draw(window)
        
        # Dibujar animales
        animal_manager.draw(window)
        
        # Dibujar inventario y notificaciones
        player_inventory.draw_inventory(window)
        player_inventory.draw_notification(window)
        
        # Dibujar panel de estado de animales
        animal_manager.draw_status_panel(window)
        
        # Manejar botón de regreso
        if PressButton(BackButton, GameResources.EVENTS):
            print("Regresando a 'main'")
            Current_Screen = "main"
        
        # Mostrar instrucciones del juego
        ShowGameInstructions()
        
    # Manejamos la pantalla de créditos
    elif Current_Screen == "window_credit":
        credits_window.render()
        if PressButton(BackButton, GameResources.EVENTS):
            print("Regresando a 'main'")
            Current_Screen = "main"

def HandleGameEvents():
    """Maneja eventos específicos del juego"""
    for event in GameResources.EVENTS:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_i:  # Alternar inventario
                player_inventory.toggle_inventory()
            elif event.key == pygame.K_h:  # Mostrar/ocultar panel de ayuda
                pass  # Implementar más tarde si es necesario

def ShowGameInstructions():
    """Muestra las instrucciones del juego en la pantalla"""
    font = loadFont('./fonts/' + FONT9, 12)
    if not font:
        return
    
    instructions = [
        "=== CONTROLES ===",
        "Flechas/WASD - Mover",
        "E - Recolectar recursos",
        "ESPACIO - Acariciar animal",
        "F - Alimentar animal",
        "I - Abrir/Cerrar inventario",
        "ESC - Salir del juego",
        "",
        "=== OBJETIVO ===",
        "Recolecta recursos de la granja",
        "Cuida a los animales",
        "Mantenlos felices y alimentados"
    ]
    
    # Fondo para las instrucciones
    panel_width = 300
    panel_height = len(instructions) * 20 + 20
    panel_x = 10
    panel_y = 10

    panel_rect = pygame.Rect(panel_x, panel_y, panel_width, panel_height)
    
    panel_surface = pygame.Surface((panel_width, panel_height), pygame.SRCALPHA)
    panel_surface.fill((0, 0, 0, 180))  # Negro con alfa 180
    window.blit(panel_surface, (panel_x, panel_y))
    pygame.draw.rect(window, WHITE, panel_rect, 2)
    
    # Dibujar instrucciones
    y_offset = 20
    for instruction in instructions:
        if instruction:  # Solo dibujar si no está vacío
            color = YELLOW if instruction.startswith("===") else WHITE
            text_surface = font.render(instruction, True, color)
            window.blit(text_surface, (panel_x + 10, panel_y + y_offset))
        y_offset += 20