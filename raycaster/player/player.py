# player/player.py
import math
import settings

class Player:
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.angle = 0  # Dirección en la que mira el jugador
        self.speed = speed

    def move_forward(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed

    def move_backward(self):
        self.x -= math.cos(self.angle) * self.speed
        self.y -= math.sin(self.angle) * self.speed

    def turn_left(self):
        self.angle -= settings.PLAYER_ROTATION_SPEED * math.pi / 180

    def turn_right(self):
        self.angle += settings.PLAYER_ROTATION_SPEED * math.pi / 180

    def update(self):
        # Aquí puedes agregar lógica adicional para actualizar el estado del jugador
        pass
