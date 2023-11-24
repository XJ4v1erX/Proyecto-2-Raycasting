# controller.py
import pygame
import settings

class Controller:
    def __init__(self, player):
        self.player = player
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
        pygame.mouse.set_pos(settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT // 2)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move_forward()
        if keys[pygame.K_s]:
            self.player.move_backward()
        if keys[pygame.K_a]:
            self.player.turn_left()
        if keys[pygame.K_d]:
            self.player.turn_right()

        # PS4 controller support
        for event in pygame.event.get(pygame.JOYAXISMOTION):
            if event.axis == settings.PS4_AXIS_HORIZONTAL:
                if event.value > 0:
                    self.player.turn_right()
                elif event.value < 0:
                    self.player.turn_left()

        # Mouse movement for rotation
        new_mouse_x, _ = pygame.mouse.get_pos()
        delta_x = new_mouse_x - self.mouse_x
        self.mouse_x = new_mouse_x
        self.player.angle += delta_x * settings.MOUSE_SENSITIVITY
