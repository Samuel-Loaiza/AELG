from resources import *
from level import *

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
    # Otras teclas para el movimiento
    if teclas[pygame.K_a]:
        newplayer_pos[0] -= velocidad
        if DEBUG_MODE == True:
            print("Izquierda")
    if teclas[pygame.K_d]:
        newplayer_pos[0] += velocidad
        if DEBUG_MODE == True:
            print("Derecha")
    if teclas[pygame.K_w]:
        newplayer_pos[1] -= velocidad
        if DEBUG_MODE == True:
            print("Arriba")
    if teclas[pygame.K_s]:
        newplayer_pos[1] += velocidad
        if DEBUG_MODE == True:
            print("Abajo")
    # Quitar el movimiento diagonal con flechas y WASD
    if teclas[pygame.K_LEFT] and teclas[pygame.K_RIGHT] and teclas[pygame.K_UP] and teclas[pygame.K_DOWN]:
        newplayer_pos[0] = player_pos[0]
        newplayer_pos[1] = player_pos[1]
    # Limitar el movimiento del jugador a la ventana
    newplayer_pos[0] = max(0, min(newplayer_pos[0], WINDOW_WIDTH - width_player))
    newplayer_pos[1] = max(0, min(newplayer_pos[1], WINDOW_HIGH - high_player))

    # Crear un rectángulo con la nueva posición del jugador
    newplayer_rect = pygame.Rect(*newplayer_pos, high_player, width_player)

    # Verificar colisión con objetos
    colision = False
    for obj in OBJECTS_SCENERY:
        if newplayer_rect.colliderect(obj):
            colision = True
            break

    # Solo mover si no hay colisión
    if not colision:
        player_pos[:] = newplayer_pos

    # Dibujar el jugador
    pygame.draw.rect(window, WHITE, (*player_pos, high_player, width_player))