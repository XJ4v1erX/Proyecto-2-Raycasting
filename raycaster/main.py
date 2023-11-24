#main.py
import pygame
import settings
from player.player import Player
from engine.render import Renderer
from player.controller import Controller

def load_level(level_file):
    # Esta función carga un nivel desde un archivo y retorna un mapa de nivel
    with open(level_file, 'r') as file:
        level_map = [list(line.strip()) for line in file.readlines()]
    return level_map

def main():
    pygame.init()
    screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    pygame.display.set_caption("Ray Caster Game")

    # Cargar el primer nivel
    level_map = load_level("levels/level1.txt")

    player = Player(settings.SCREEN_WIDTH / 2, settings.SCREEN_HEIGHT / 2, settings.PLAYER_SPEED)
    renderer = Renderer(screen, level_map, settings.TILE_SIZE, settings.FOV)
    controller = Controller(player)

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Actualizar estado del juego
        controller.handle_input()
        player.update()

        # Renderizar frame actual
        screen.fill((0, 0, 0))  # Fondo negro
        renderer.render(player)
        pygame.display.flip()

        clock.tick(settings.FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
