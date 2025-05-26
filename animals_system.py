from resources import *
import random
import time

class Animal:
    def __init__(self, name, x, y, width, height, color, sound, interaction_text, food_type):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.sound = sound
        self.interaction_text = interaction_text
        self.food_type = food_type
        self.rect = pygame.Rect(x, y, width, height)
        self.happiness = 50  # Nivel de felicidad (0-100)
        self.hunger = 50     # Nivel de hambre (0-100)
        self.last_interaction = 0
        self.is_moving = False
        self.move_direction = [random.choice([-1, 0, 1]), random.choice([-1, 0, 1])]
        self.move_timer = 0
        self.interaction_cooldown = 3  # Segundos entre interacciones
        
    def update(self):
        """Actualiza el estado del animal"""
        current_time = time.time()
        
        # Movimiento aleatorio
        self.move_timer += 1
        if self.move_timer > 60:  # Cambiar dirección cada 60 frames
            self.move_direction = [random.choice([-1, 0, 1]), random.choice([-1, 0, 1])]
            self.move_timer = 0
            
        # Mover el animal lentamente
        if random.random() < 0.3:  # 30% de probabilidad de moverse
            new_x = self.x + self.move_direction[0]
            new_y = self.y + self.move_direction[1]
            
            # Mantener dentro de los límites
            if 50 < new_x < WINDOW_WIDTH - 50 - self.width:
                self.x = new_x
            if 50 < new_y < WINDOW_HIGH - 50 - self.height:
                self.y = new_y
                
            self.rect.x = self.x
            self.rect.y = self.y
        
        # Decrementar felicidad y aumentar hambre con el tiempo
        if current_time - self.last_interaction > 10:  # Cada 10 segundos
            self.happiness = max(0, self.happiness - 1)
            self.hunger = min(100, self.hunger + 1)
            self.last_interaction = current_time
    
    def can_interact(self):
        """Verifica si el animal puede interactuar"""
        return time.time() - self.last_interaction > self.interaction_cooldown
    
    def interact(self, interaction_type="pet"):
        """Interactúa con el animal"""
        if not self.can_interact():
            return False
            
        self.last_interaction = time.time()
        
        if interaction_type == "pet":
            self.happiness = min(100, self.happiness + 15)
            return f"Has acariciado a {self.name}! Felicidad +15"
        elif interaction_type == "feed":
            self.hunger = max(0, self.hunger - 30)
            self.happiness = min(100, self.happiness + 10)
            return f"Has alimentado a {self.name}! Hambre -30, Felicidad +10"
        
        return "Interacción exitosa"
    
    def get_status_color(self):
        """Devuelve el color del animal basado en su estado"""
        if self.happiness > 70:
            return self.color  # Color normal cuando está feliz
        elif self.happiness > 30:
            return tuple(max(0, c - 50) for c in self.color)  # Un poco más oscuro
        else:
            return tuple(max(0, c - 100) for c in self.color)  # Más oscuro cuando está triste
    
    def draw(self, surface):
        """Dibuja el animal en la superficie"""
        # Dibujar el cuerpo del animal
        current_color = self.get_status_color()
        pygame.draw.ellipse(surface, current_color, self.rect)
        
        # Dibujar borde
        pygame.draw.ellipse(surface, BLACK, self.rect, 2)
        
        # Dibujar ojos simples
        eye_size = 4
        left_eye_pos = (self.x + self.width // 3, self.y + self.height // 3)
        right_eye_pos = (self.x + 2 * self.width // 3, self.y + self.height // 3)
        pygame.draw.circle(surface, BLACK, left_eye_pos, eye_size)
        pygame.draw.circle(surface, BLACK, right_eye_pos, eye_size)
        
        # Mostrar nombre del animal
        font = loadFont('./fonts/' + FONT9, 12)
        if font:
            text_surface = font.render(self.name, True, BLACK)
            text_rect = text_surface.get_rect()
            text_rect.centerx = self.rect.centerx
            text_rect.y = self.rect.y - 20
            surface.blit(text_surface, text_rect)
    
    def draw_status_bar(self, surface, x, y):
        """Dibuja las barras de estado del animal"""
        font = loadFont('./fonts/' + FONT9, 12)
        if not font:
            return
            
        # Información del animal
        name_text = font.render(f"{self.name}:", True, BLACK)
        surface.blit(name_text, (x, y))
        
        # Barra de felicidad
        happiness_text = font.render("Felicidad:", True, BLACK)
        surface.blit(happiness_text, (x, y + 25))
        
        happiness_bar_rect = pygame.Rect(x + 100, y + 25, 100, 10)
        pygame.draw.rect(surface, RED, happiness_bar_rect)
        happiness_fill = pygame.Rect(x + 100, y + 25, self.happiness, 10)
        pygame.draw.rect(surface, GREEN, happiness_fill)
        pygame.draw.rect(surface, BLACK, happiness_bar_rect, 2)
        
        # Barra de hambre
        hunger_text = font.render("Hambre:", True, BLACK)
        surface.blit(hunger_text, (x, y + 45))
        
        hunger_bar_rect = pygame.Rect(x + 100, y + 45, 100, 10)
        pygame.draw.rect(surface, GREEN, hunger_bar_rect)
        hunger_fill = pygame.Rect(x + 100, y + 45, self.hunger, 10)
        pygame.draw.rect(surface, RED, hunger_fill)
        pygame.draw.rect(surface, BLACK, hunger_bar_rect, 2)

class AnimalManager:
    def __init__(self):
        self.animals = []
        self.interaction_message = ""
        self.message_timer = 0
        self.selected_animal = None
        self.create_animals()
    
    def create_animals(self):
        """Crea los animales iniciales"""
        # Vaca
        cow = Animal("Vaca", 300, 200, 60, 40, BROWN, "moo", 
                    "La vaca dice: ¡Muuu!", "hierba")
        
        # Cerdo
        pig = Animal("Cerdo", 500, 300, 50, 35, PINK, "oink", 
                    "El cerdo dice: ¡Oink oink!", "maíz")
        
        # Pollo
        chicken = Animal("Pollo", 150, 350, 30, 25, WHITE, "cluck", 
                        "El pollo dice: ¡Clo clo clo!", "semillas")
        
        # Oveja
        sheep = Animal("Oveja", 400, 450, 45, 35, WHITE, "baa", 
                      "La oveja dice: ¡Beee!", "hierba")
        
        self.animals = [cow, pig, chicken, sheep]
    
    def update(self):
        """Actualiza todos los animales"""
        for animal in self.animals:
            animal.update()
        
        # Decrementar timer del mensaje
        if self.message_timer > 0:
            self.message_timer -= 1
            if self.message_timer <= 0:
                self.interaction_message = ""
    
    def handle_interaction(self, player_pos, player_size):
        """Maneja las interacciones entre el jugador y los animales"""
        player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size[0], player_size[1])
        
        keys = pygame.key.get_pressed()
        
        for animal in self.animals:
            # Verificar si el jugador está cerca del animal
            if player_rect.colliderect(animal.rect):
                self.selected_animal = animal
                
                # Interacciones con teclas
                if keys[pygame.K_SPACE] and animal.can_interact():
                    message = animal.interact("pet")
                    self.show_message(message)
                elif keys[pygame.K_f] and animal.can_interact():
                    message = animal.interact("feed")
                    self.show_message(message)
                
                break
        else:
            self.selected_animal = None
    
    def show_message(self, message):
        """Muestra un mensaje de interacción"""
        self.interaction_message = message
        self.message_timer = 120  # Mostrar por 2 segundos a 60 FPS
    
    def draw(self, surface):
        """Dibuja todos los animales"""
        for animal in self.animals:
            animal.draw(surface)
        
        # Dibujar mensaje de interacción
        if self.interaction_message and self.message_timer > 0:
            font = loadFont('./fonts/' + FONT9, 14)
            if font:
                text_surface = font.render(self.interaction_message, True, WHITE)
                text_rect = text_surface.get_rect()
                text_rect.center = (WINDOW_WIDTH // 2, 50)
                
                # Fondo para el mensaje
                bg_rect = text_rect.inflate(20, 10)
                pygame.draw.rect(surface, BLACK, bg_rect)
                pygame.draw.rect(surface, WHITE, bg_rect, 2)
                surface.blit(text_surface, text_rect)
        
        # Mostrar instrucciones si hay un animal seleccionado
        if self.selected_animal:
            font = loadFont('./fonts/' + FONT9, 12)
            if font:
                instructions = [
                    "ESPACIO - Acariciar",
                    "F - Alimentar"
                ]
                
                y_offset = WINDOW_HIGH - 100
                for instruction in instructions:
                    text_surface = font.render(instruction, True, WHITE)
                    text_rect = text_surface.get_rect()
                    text_rect.x = 10
                    text_rect.y = y_offset
                    
                    # Fondo para las instrucciones
                    bg_rect = text_rect.inflate(10, 5)
                    pygame.draw.rect(surface, BLACK, bg_rect)
                    pygame.draw.rect(surface, WHITE, bg_rect, 1)
                    surface.blit(text_surface, text_rect)
                    
                    y_offset += 25
    
    def draw_status_panel(self, surface):
        """Dibuja el panel de estado de los animales"""
        panel_x = WINDOW_WIDTH - 250
        panel_y = 10
        panel_width = 240
        panel_height = len(self.animals) * 80 + 20
        
        # Fondo del panel
        panel_rect = pygame.Rect(panel_x, panel_y, panel_width, panel_height)
        pygame.draw.rect(surface, (50, 50, 50), panel_rect)  # Fondo oscuro
        pygame.draw.rect(surface, WHITE, panel_rect, 2)
        
        # Título del panel
        font = loadFont('./fonts/' + FONT9, 14)
        if font:
            title_text = font.render("Estado de Animales", True, WHITE)
            surface.blit(title_text, (panel_x + 10, panel_y + 5))
        
        # Estado de cada animal
        y_offset = 30
        for animal in self.animals:
            animal.draw_status_bar(surface, panel_x + 10, panel_y + y_offset)
            y_offset += 80

# Instancia global del manejador de animales
animal_manager = AnimalManager()