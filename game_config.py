# Configuración del juego "Aprendizaje en la Granja"

# Configuración del jugador
PLAYER_CONFIG = {
    "width": 45,
    "height": 35,
    "speed": 5,
    "color": (0, 100, 255),  # Azul
    "starting_x": None,  # Se calculará como WINDOW_WIDTH // 2
    "starting_y": None   # Se calculará como WINDOW_HIGH // 2
}

# Configuración de animales
ANIMAL_CONFIG = {
    "interaction_cooldown": 3,  # Segundos entre interacciones
    "happiness_decay_rate": 1,  # Puntos de felicidad perdidos cada 10 segundos
    "hunger_increase_rate": 1,  # Puntos de hambre ganados cada 10 segundos
    "movement_probability": 0.3,  # Probabilidad de movimiento por frame
    "direction_change_frames": 60  # Frames antes de cambiar dirección
}

# Configuración de recursos
RESOURCE_CONFIG = {
    "respawn_times": {
        "hierba": 10,
        "maíz": 15,
        "semillas": 8,
        "zanahorias": 20
    },
    "spawn_locations": [
        {"type": "hierba", "x": 100, "y": 200},
        {"type": "hierba", "x": 600, "y": 150},
        {"type": "maíz", "x": 300, "y": 400},
        {"type": "semillas", "x": 450, "y": 250},
        {"type": "zanahorias", "x": 200, "y": 500}
    ]
}

# Configuración del inventario
INVENTORY_CONFIG = {
    "max_items_per_type": 99,
    "starting_items": {
        "hierba": 5,
        "maíz": 3,
        "semillas": 8,
        "zanahorias": 2
    }
}

# Configuración de la interfaz
UI_CONFIG = {
    "notification_duration": 120,  # Frames (2 segundos a 60 FPS)
    "panel_transparency": 128,
    "instruction_panel_width": 300,
    "status_panel_width": 250
}

# Configuración de los elementos del escenario
SCENERY_CONFIG = {
    "objects": [
        {"x": 200, "y": 150, "width": 60, "height": 60, "type": "rock"},
        {"x": 500, "y": 400, "width": 50, "height": 80, "type": "tree"}
    ]
}

# Mensajes del juego
GAME_MESSAGES = {
    "welcome": "¡Bienvenido a la Granja!",
    "inventory_full": "Inventario lleno!",
    "no_food": "No tienes comida para este animal",
    "animal_happy": "¡El animal está feliz!",
    "resource_collected": "Recurso recolectado",
    "interaction_cooldown": "Espera un momento antes de interactuar de nuevo"
}

# Configuración de efectos visuales
VISUAL_EFFECTS = {
    "hover_scale": 1.05,
    "button_border_width": 3,
    "resource_blink_speed": 3,  # Velocidad del parpadeo de recursos
    "status_bar_height": 10
}

# Teclas de control (para facilitar personalización futura)
CONTROLS = {
    "move_left": ["K_LEFT", "K_a"],
    "move_right": ["K_RIGHT", "K_d"],
    "move_up": ["K_UP", "K_w"],
    "move_down": ["K_DOWN", "K_s"],
    "interact": "K_SPACE",
    "feed": "K_f",
    "collect": "K_e",
    "inventory": "K_i",
    "exit": "K_ESCAPE"
}

# Configuración de dificultad (para futuras expansiones)
DIFFICULTY_SETTINGS = {
    "easy": {
        "animal_happiness_decay": 0.5,
        "resource_respawn_multiplier": 0.8,
        "starting_resources_multiplier": 2
    },
    "normal": {
        "animal_happiness_decay": 1.0,
        "resource_respawn_multiplier": 1.0,
        "starting_resources_multiplier": 1
    },
    "hard": {
        "animal_happiness_decay": 1.5,
        "resource_respawn_multiplier": 1.2,
        "starting_resources_multiplier": 0.5
    }
}

# Configuración actual de dificultad
CURRENT_DIFFICULTY = "normal"

def get_difficulty_setting(setting_name):
    """Obtiene una configuración basada en la dificultad actual"""
    return DIFFICULTY_SETTINGS[CURRENT_DIFFICULTY].get(setting_name, 1.0)