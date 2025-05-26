from resources import *
from level import *
from animals_system import animal_manager
# Nota: inventory se importa en init.py para evitar dependencias circulares

# Jugador
player_pos = [WINDOW_WIDTH // 2, WINDOW_HIGH // 2]
high_player = 35
width_player = 45
velocidad = 5

def MotionPlayer():
    global player_pos
    # Actualizar la posición del jugador según las teclas presionadas
    newplayer_pos = player_pos[:]
    teclas = pygame.key.get_pressed()
    
    # Movimiento con flechas
    if teclas[pygame.K_LEFT]:
        newplayer_pos[0] -= velocidad
        if DEBUG_MODE == True:
            print("Izquierda")
    if teclas[pygame.K_RIGHT]:
        newplayer_pos[0] += velocidad
        if DEBUG_MODE == True:
            print("Derecha")
    if teclas[pygame.K_UP]:
        newplayer_pos[1] -= velocidad
        if DEBUG_MODE == True:
            print("Arriba")
    if teclas[pygame.K_DOWN]:
        newplayer_pos[1] += velocidad
        if DEBUG_MODE == True:
            print("Abajo")
    
    # Movimiento con WASD
    if teclas[pygame.K_a]:
        newplayer_pos[0] -= velocidad
        if DEBUG_MODE == True:
            print("Izquierda (A)")
    if teclas[pygame.K_d]:
        newplayer_pos[0] += velocidad
        if DEBUG_MODE == True:
            print("Derecha (D)")
    if teclas[pygame.K_w]:
        newplayer_pos[1] -= velocidad
        if DEBUG_MODE == True:
            print("Arriba (W)")
    if teclas[pygame.K_s]:
        newplayer_pos[1] += velocidad
        if DEBUG_MODE == True:
            print("Abajo (S)")
    
    # Prevenir movimiento diagonal contradictorio
    if teclas[pygame.K_LEFT] and teclas[pygame.K_RIGHT]:
        newplayer_pos[0] = player_pos[0]
    if teclas[pygame.K_UP] and teclas[pygame.K_DOWN]:
        newplayer_pos[1] = player_pos[1]
    if teclas[pygame.K_a] and teclas[pygame.K_d]:
        newplayer_pos[0] = player_pos[0]
    if teclas[pygame.K_w] and teclas[pygame.K_s]:
        newplayer_pos[1] = player_pos[1]
    
    # Limitar el movimiento del jugador a la ventana
    newplayer_pos[0] = max(0, min(newplayer_pos[0], WINDOW_WIDTH - width_player))
    newplayer_pos[1] = max(0, min(newplayer_pos[1], WINDOW_HIGH - high_player))

    # Crear un rectángulo con la nueva posición del jugador
    newplayer_rect = pygame.Rect(*newplayer_pos, width_player, high_player)

    # Verificar colisión con objetos del escenario
    colision = False
    for obj in OBJECTS_SCENERY:
        if newplayer_rect.colliderect(obj):
            colision = True
            break

    # Solo mover si no hay colisión
    if not colision:
        player_pos[:] = newplayer_pos

    # Manejar interacciones con animales
    animal_manager.handle_interaction(player_pos, (width_player, high_player))

    # Dibujar el jugador
    DrawPlayer()

def DrawPlayer():
    """Dibuja el jugador con un diseño más detallado"""
    # Cuerpo principal (rectángulo redondeado simulado)
    player_rect = pygame.Rect(*player_pos, width_player, high_player)
    pygame.draw.rect(window, BLUE, player_rect)
    pygame.draw.rect(window, DARK_GRAY, player_rect, 3)
    
    # Cabeza (círculo)
    head_center = (player_pos[0] + width_player // 2, player_pos[1] + 8)
    pygame.draw.circle(window, LIGHT_BLUE, head_center, 8)
    pygame.draw.circle(window, DARK_GRAY, head_center, 8, 2)
    
    # Ojos
    left_eye = (head_center[0] - 3, head_center[1] - 2)
    right_eye = (head_center[0] + 3, head_center[1] - 2)
    pygame.draw.circle(window, BLACK, left_eye, 2)
    pygame.draw.circle(window, BLACK, right_eye, 2)
    
    # Brazos (pequeños rectángulos)
    left_arm = pygame.Rect(player_pos[0] - 5, player_pos[1] + 12, 8, 4)
    right_arm = pygame.Rect(player_pos[0] + width_player - 3, player_pos[1] + 12, 8, 4)
    pygame.draw.rect(window, LIGHT_BLUE, left_arm)
    pygame.draw.rect(window, LIGHT_BLUE, right_arm)
    
    # Piernas (pequeños rectángulos)
    left_leg = pygame.Rect(player_pos[0] + 8, player_pos[1] + high_player - 8, 6, 8)
    right_leg = pygame.Rect(player_pos[0] + width_player - 14, player_pos[1] + high_player - 8, 6, 8)
    pygame.draw.rect(window, DARK_GRAY, left_leg)
    pygame.draw.rect(window, DARK_GRAY, right_leg)

def GetPlayerPosition():
    """Devuelve la posición actual del jugador"""
    return player_pos

def GetPlayerRect():
    """Devuelve el rectángulo del jugador"""
    return pygame.Rect(*player_pos, width_player, high_player)