# renderer.py
import pygame
import math

class Renderer:
    def __init__(self, screen, level_map, tile_size, fov):
        self.screen = screen
        self.level_map = level_map
        self.tile_size = tile_size
        self.fov = fov
        self.width, self.height = screen.get_size()
        self.dist_to_proj_plane = (self.width / 2) / math.tan(math.radians(self.fov / 2))

    def render(self, player):
        for x in range(0, self.width, 1):
            ray_angle = (player.angle - self.fov / 2) + (x / self.width) * self.fov
            distance, offset = self.cast_ray(player.x, player.y, math.radians(ray_angle))

            if distance == 0:
                distance = 0.0001  # Evitar la división por cero asignando un valor pequeño

            wall_height = (self.tile_size / distance) * self.dist_to_proj_plane

            start = int((self.height / 2) - (wall_height / 2))
            end = int((self.height / 2) + (wall_height / 2))
            pygame.draw.line(self.screen, (255, 255, 255), (x, start), (x, end))


    def cast_ray(self, x, y, angle):
        sin_a = math.sin(angle)
        cos_a = math.cos(angle)

        # Evitar división por cero
        if cos_a == 0:
            cos_a = 0.0001

        # Raycasting algorithm
        for depth in range(0, 1000, 1):
            target_x = x + cos_a * depth
            target_y = y + sin_a * depth

            # Check if the ray has hit a wall
            col = int(target_x / self.tile_size)
            row = int(target_y / self.tile_size)

            if 0 <= row < len(self.level_map) and 0 <= col < len(self.level_map[row]):
                if self.level_map[row][col] == 1:  # Assuming 1 is a wall in the level map
                    # Calculate distance to the wall
                    distance = math.sqrt((target_x - x) ** 2 + (target_y - y) ** 2)
                    return distance, 0  # Offset is zero for simplicity

            # Si se sale del mapa, asumir que no hay muro
            if not (0 <= row < len(self.level_map) and 0 <= col < len(self.level_map[row])):
                return 0, 0

        return 0, 0  # Return default value if no wall is hit
