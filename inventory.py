from resources import *
import time

class Item:
    def __init__(self, name, item_type, description, color=WHITE):
        self.name = name
        self.item_type = item_type
        self.description = description
        self.color = color

class Inventory:
    def __init__(self):
        self.items = {
            "hierba": 5,
            "maíz": 3,
            "semillas": 8,
            "zanahorias": 2
        }
        self.max_items = 99
        self.show_inventory = False
        self.notification_message = ""
        self.notification_timer = 0
        
        # Definir tipos de items
        self.item_definitions = {
            "hierba": Item("Hierba", "comida", "Alimento favorito de vacas y ovejas", GREEN),
            "maíz": Item("Maíz", "comida", "Perfecto para alimentar cerdos", YELLOW),
            "semillas": Item("Semillas", "comida", "Ideales para los pollos", BROWN),
            "zanahorias": Item("Zanahorias", "comida", "Snack saludable para todos", ORANGE)
        }
    
    def add_item(self, item_name, quantity=1):
        """Añade items al inventario"""
        if item_name in self.items:
            new_quantity = min(self.items[item_name] + quantity, self.max_items)
            added = new_quantity - self.items[item_name]
            self.items[item_name] = new_quantity
            
            if added > 0:
                self.show_notification(f"+{added} {item_name}")
                return True
            else:
                self.show_notification(f"Inventario de {item_name} lleno!")
                return False
        return False
    
    def remove_item(self, item_name, quantity=1):
        """Remueve items del inventario"""
        if item_name in self.items and self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
            return True
        return False
    
    def has_item(self, item_name, quantity=1):
        """Verifica si tiene suficientes items"""
        return item_name in self.items and self.items[item_name] >= quantity
    
    def show_notification(self, message):
        """Muestra una notificación temporal"""
        self.notification_message = message
        self.notification_timer = 120  # 2 segundos a 60 FPS
    
    def update(self):
        """Actualiza el inventario"""
        if self.notification_timer > 0:
            self.notification_timer -= 1
            if self.notification_timer <= 0:
                self.notification_message = ""
    
    def toggle_inventory(self):
        """Alterna la visibilidad del inventario"""
        self.show_inventory = not self.show_inventory
    
    def draw_notification(self, surface):
        """Dibuja notificaciones"""
        if self.notification_message and self.notification_timer > 0:
            font = loadFont('./fonts/' + FONT9, 14)
            if font:
                text_surface = font.render(self.notification_message, True, WHITE)
                text_rect = text_surface.get_rect()
                text_rect.center = (WINDOW_WIDTH // 2, 100)
                
                # Fondo para la notificación
                bg_rect = text_rect.inflate(20, 10)
                pygame.draw.rect(surface, GREEN, bg_rect)
                pygame.draw.rect(surface, WHITE, bg_rect, 2)
                surface.blit(text_surface, text_rect)
    
    def draw_inventory(self, surface):
        """Dibuja el inventario cuando está visible"""
        if not self.show_inventory:
            return
        
        # Dimensiones del panel de inventario
        panel_width = 400
        panel_height = 300
        panel_x = (WINDOW_WIDTH - panel_width) // 2
        panel_y = (WINDOW_HIGH - panel_height) // 2
        
        # Fondo del inventario
        panel_rect = pygame.Rect(panel_x, panel_y, panel_width, panel_height)
        pygame.draw.rect(surface, (50, 50, 50, 200))  # Fondo semi-transparente
        pygame.draw.rect(surface, WHITE, panel_rect, 3)
        
        # Título del inventario
        font_title = loadFont('./fonts/' + FONT9, 18)
        font_items = loadFont('./fonts/' + FONT9, 14)
        
        if font_title:
            title_text = font_title.render("INVENTARIO", True, WHITE)
            title_rect = title_text.get_rect()
            title_rect.centerx = panel_x + panel_width // 2
            title_rect.y = panel_y + 10
            surface.blit(title_text, title_rect)
        
        # Dibujar items
        if font_items:
            y_offset = 50
            for item_name, quantity in self.items.items():
                if quantity > 0:
                    item_def = self.item_definitions.get(item_name)
                    color = item_def.color if item_def else WHITE
                    
                    # Nombre y cantidad del item
                    item_text = f"{item_name.capitalize()}: {quantity}"
                    text_surface = font_items.render(item_text, True, color)
                    surface.blit(text_surface, (panel_x + 20, panel_y + y_offset))
                    
                    # Descripción del item
                    if item_def:
                        desc_surface = font_items.render(item_def.description, True, LIGHT_GRAY)
                        surface.blit(desc_surface, (panel_x + 30, panel_y + y_offset + 20))
                    
                    y_offset += 45
        
        # Instrucciones para cerrar
        if font_items:
            close_text = font_items.render("Presiona I para cerrar", True, YELLOW)
            close_rect = close_text.get_rect()
            close_rect.centerx = panel_x + panel_width // 2
            close_rect.y = panel_y + panel_height - 30
            surface.blit(close_text, close_rect)

class ResourceManager:
    def __init__(self):
        self.spawn_points = [
            {"type": "hierba", "x": 100, "y": 200, "respawn_time": 10},
            {"type": "hierba", "x": 600, "y": 150, "respawn_time": 10},
            {"type": "maíz", "x": 300, "y": 400, "respawn_time": 15},
            {"type": "semillas", "x": 450, "y": 250, "respawn_time": 8},
            {"type": "zanahorias", "x": 200, "y": 500, "respawn_time": 20}
        ]
        
        for point in self.spawn_points:
            point["last_spawn"] = 0
            point["available"] = True
    
    def update(self):
        """Actualiza los puntos de recursos"""
        current_time = time.time()
        for point in self.spawn_points:
            if not point["available"] and current_time - point["last_spawn"] > point["respawn_time"]:
                point["available"] = True
    
    def collect_resource(self, player_pos, player_size, inventory):
        """Permite al jugador recolectar recursos"""
        player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size[0], player_size[1])
        
        for point in self.spawn_points:
            if point["available"]:
                resource_rect = pygame.Rect(point["x"] - 15, point["y"] - 15, 30, 30)
                if player_rect.colliderect(resource_rect):
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_e]:  # Tecla E para recolectar
                        if inventory.add_item(point["type"], 1):
                            point["available"] = False
                            point["last_spawn"] = time.time()
                            return True
        return False
    
    def draw(self, surface):
        """Dibuja los recursos disponibles"""
        for point in self.spawn_points:
            if point["available"]:
                resource_rect = pygame.Rect(point["x"] - 15, point["y"] - 15, 30, 30)
                
                # Color basado en el tipo de recurso
                colors = {
                    "hierba": GREEN,
                    "maíz": YELLOW,
                    "semillas": BROWN,
                    "zanahorias": ORANGE
                }
                color = colors.get(point["type"], WHITE)
                
                # Dibujar el recurso
                pygame.draw.rect(surface, color, resource_rect)
                pygame.draw.rect(surface, BLACK, resource_rect, 2)
                
                # Efecto de brillo
                if int(time.time() * 3) % 2:  # Parpadeo
                    pygame.draw.rect(surface, WHITE, resource_rect, 1)
                
                # Etiqueta del recurso
                font = loadFont('./fonts/' + FONT9, 10)
                if font:
                    text_surface = font.render(point["type"], True, BLACK)
                    text_rect = text_surface.get_rect()
                    text_rect.centerx = point["x"]
                    text_rect.y = point["y"] + 20
                    surface.blit(text_surface, text_rect)

# Instancias globales
player_inventory = Inventory()
resource_manager = ResourceManager()