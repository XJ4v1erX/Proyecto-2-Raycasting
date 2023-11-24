import pygame
import pygame.mixer
import random
import math
import sys

# Configuración inicial
ANCHO, ALTO = 800, 600
FOV = math.pi / 3  # Campo de visión
NUM_RAYS = 120  # Número de rayos
MAX_DIST = 800  # Distancia máxima de renderizado
RESOLUCION = ANCHO // NUM_RAYS
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ray Caster Game")

clock = pygame.time.Clock()
fuente = pygame.font.Font(None, 48)
fondo_menu = "./menu.png" # Asegúrate de tener esta imagen
x_jugador, y_jugador = 150, 150
angulo_jugador = 0
mouse_pos_anterior = pygame.mouse.get_pos()
# Asegúrate de tener esta canción

# Tamaño del minimapa y su posición en la pantalla
TAM_MINIMAPA = (99, 99)
POS_MINIMAPA = (10, 10)

# Crear una superficie para el minimapa
minimapa_surface = pygame.Surface(TAM_MINIMAPA)

# Cargar el sonido de pasos
archivos_sonidos = ["step1.mp3", "step2.mp3", "step3.mp3", "step4.mp3", "step5.mp3", "step6.mp3", "step7.mp3"]

# Cargar todos los sonidos
sonidos_pasos = [pygame.mixer.Sound(archivo) for archivo in archivos_sonidos]

imagen_de_fondo = pygame.image.load('fondo.png')
imagen_de_fondo = pygame.transform.scale(imagen_de_fondo, (ANCHO, ALTO))


# Intervalo mínimo en milisegundos entre reproducciones de sonido
intervalo_minimo = 500  # 0.5 segundos
tiempo_ultima_reproduccion = 0  # Iniciar el tiempo de la última reproducción
# Colores
COLOR_TEXTO = (255, 255, 255)
COLOR_SELECCION = (255, 215, 0)  # Dorado
# Mapa del nivel (Ejemplo simple)
mapa = [
    "#########",
    "#......##",
    "#.####..#",
    "#.......#",
    "#..###..#",
    "#.##.##.#",
    "#......##",
    "#.####..#",
    "#.......#",
    "###.#####",
    "#.......#",
    "#.#######",
    "#.......#",
    "#########"
]

mapa_templo_desierto = [
    "#########",
    "#......##",
    "#.####..#",
    "#.......#",
    "###.#####",
    "#.......#",
    "#.#######",
    "#.......#",
    "#########"
]
mapa_ciudad_jungla = [
    "#########",
    "#...#...#",
    "#.#.#.#.#",
    "#.#...#.#",
    "###.#.###",
    "#...#...#",
    "#.#.#.#.#",
    "#...#...#",
    "#########"
]


# Tamaño del bloque en el mapa
TAM_BLOQUE = 100

# Iniciar PyGame
pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()

# Posición y orientación del jugador
x_jugador, y_jugador = 150, 150
angulo_jugador = 0

def calcular_distancia_rayo(x_jugador, y_jugador, angulo_rayo):
    for i in range(0, MAX_DIST, 5):
        x = x_jugador + (i * math.cos(angulo_rayo))
        y = y_jugador + (i * math.sin(angulo_rayo))

        # Verificar colisión con pared
        if mapa[int(y // TAM_BLOQUE)][int(x // TAM_BLOQUE)] == '#':
            return i
    return MAX_DIST

def dibujar():
    pantalla.fill((0, 0, 0))
    for rayo in range(0, NUM_RAYS):
        angulo_rayo = angulo_jugador - (FOV / 2) + (FOV * rayo / NUM_RAYS)
        distancia = calcular_distancia_rayo(x_jugador, y_jugador, angulo_rayo)

        # Comprobar si la distancia es cero o muy pequeña para evitar divisiones por cero
        if distancia <= 0.01:
            continue

        altura_pared = (TAM_BLOQUE / distancia) * 277  # Proyección en pantalla
        color = 255 / (1 + distancia * distancia * 0.0001)  # Atenuación de color
        pygame.draw.rect(pantalla, (color, color, color), (rayo * RESOLUCION, (ALTO / 2) - (altura_pared / 2), RESOLUCION, altura_pared))
        # Dibujar el minimapa
        dibujar_minimapa(pantalla, x_jugador, y_jugador, mapa)

        # Dibujar los FPS en la esquina derecha superior
        fps = clock.get_fps()
        dibujar_fps(pantalla, fps)

    pygame.display.flip()

def dibujar_minimapa(pantalla, x_jugador, y_jugador, mapa):
    minimapa_surface.fill((0, 0, 0))  # Limpiar la superficie del minimapa
    tam_bloque_minimapa = 11  # Tamaño de cada bloque en el minimapa

    # Dibujar el mapa en el minimapa
    for y in range(len(mapa)):
        for x in range(len(mapa[y])):
            bloque = mapa[y][x]
            if bloque == '#':
                pygame.draw.rect(minimapa_surface, (255, 255, 255), (x * tam_bloque_minimapa, y * tam_bloque_minimapa, tam_bloque_minimapa, tam_bloque_minimapa))

    # Dibujar la posición del jugador en el minimapa
    pygame.draw.circle(minimapa_surface, (255, 0, 0), (int(x_jugador / TAM_BLOQUE * tam_bloque_minimapa), int(y_jugador / TAM_BLOQUE * tam_bloque_minimapa)), 4)

    # Dibujar el minimapa en la pantalla principal
    pantalla.blit(minimapa_surface, POS_MINIMAPA)

def dibujar_fps(pantalla, fps):
    texto_fps = fuente.render(f"FPS: {int(fps)}", True, COLOR_TEXTO)
    pantalla.blit(texto_fps, (ANCHO - texto_fps.get_width() - 10, 10))


def cargar_y_escalar_imagen(fondo_menu, nueva_anchura, nueva_altura):
    # Cargar la imagen original
    imagen = pygame.image.load(fondo_menu)

    # Obtener dimensiones originales
    anchura_original, altura_original = imagen.get_size()

    # Calcular el factor de escala manteniendo la relación de aspecto
    factor_escala = min(nueva_anchura / anchura_original, nueva_altura / altura_original)

    # Calcular nuevas dimensiones
    nueva_anchura = int(anchura_original * factor_escala)
    nueva_altura = int(altura_original * factor_escala)

    # Escalar la imagen
    imagen_escalada = pygame.transform.scale(imagen, (nueva_anchura, nueva_altura))

    return imagen_escalada

imagen_fondo_escalada = cargar_y_escalar_imagen(fondo_menu, ALTO, ANCHO)

def mostrar_menu_bienvenida(pantalla):
    opciones = ["Templo del Desierto", "Ciudad Perdida en la Jungla", "Templo de la Muerte"]
    seleccion_actual = 0
    corriendo = True

    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play(-1)  # Reproduce la música de fondo en bucle

    while corriendo:
        pantalla.blit(imagen_fondo_escalada, (10, 10))

        # Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.mixer.music.stop()  # Detén la música antes de salir
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    corriendo = False
                if evento.key == pygame.K_UP:
                    seleccion_actual = (seleccion_actual - 1) % len(opciones)
                if evento.key == pygame.K_DOWN:
                    seleccion_actual = (seleccion_actual + 1) % len(opciones)

        # Dibujar opciones de menú
        for i, opcion in enumerate(opciones):
            if i == seleccion_actual:
                texto = fuente.render(opcion, True, COLOR_SELECCION)
            else:
                texto = fuente.render(opcion, True, COLOR_TEXTO)
            pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, 200 + i * 50))

        pygame.display.flip()

    pygame.mixer.music.stop()  # Detén la música antes de entrar al juego

    return seleccion_actual + 1

def reproducir_sonido_aleatorio():
    global tiempo_ultima_reproduccion
    tiempo_actual = pygame.time.get_ticks()

    if tiempo_actual - tiempo_ultima_reproduccion >= intervalo_minimo:
        sonido_aleatorio = random.choice(sonidos_pasos)
        sonido_aleatorio.play()
        tiempo_ultima_reproduccion = tiempo_actual

# Carga todas las imágenes de la animación en una lista
imagenes_rotacion = [
    pygame.image.load('coin1.png').convert_alpha(),
    pygame.image.load('coin2.png').convert_alpha(),
    pygame.image.load('coin3.png').convert_alpha(),
    pygame.image.load('coin4.png').convert_alpha(),
    pygame.image.load('coin5.png').convert_alpha(),
    pygame.image.load('coin6.png').convert_alpha(),
    pygame.image.load('coin7.png').convert_alpha(),

    # ... Carga el resto de las imágenes
]

# Escala las imágenes al tamaño deseado
TAM_BLOQUE = 50  # O el tamaño que necesites
imagenes_rotacion = [pygame.transform.scale(img, (TAM_BLOQUE, TAM_BLOQUE)) for img in imagenes_rotacion]

class Item:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.recogido = False
        self.indice_animacion = 0
        self.contador_animacion = 0

    def actualizar_animacion(self):
        # Actualizar la animación solo cada 5 cuadros
        self.contador_animacion += 1
        if self.contador_animacion >= 5:
            self.contador_animacion = 0
            self.indice_animacion += 1
            if self.indice_animacion >= len(imagenes_rotacion):
                self.indice_animacion = 0

    def dibujar_item_giratorio(self, pantalla, x_jugador, y_jugador, angulo_jugador):
        dx, dy = self.x - x_jugador, self.y - y_jugador
        distancia = math.sqrt(dx * dx + dy * dy)
        if distancia < 20 or distancia > MAX_DIST:
            return

        # Actualiza la animación y obtiene la imagen actual
        self.actualizar_animacion()
        imagen_actual = imagenes_rotacion[self.indice_animacion]

        # Ajusta la escala de la imagen según la distancia
        altura_proyectada = int(TAM_BLOQUE / distancia * 277)
        imagen_escala = pygame.transform.scale(imagen_actual, (altura_proyectada, altura_proyectada))

        # Calcula la posición de la imagen en la pantalla
        angulo_relativo = angulo_jugador - math.atan2(dy, dx)
        angulo_relativo = (angulo_relativo + math.pi) % (2 * math.pi) - math.pi
        if -FOV / 2 < angulo_relativo < FOV / 2:
            item_x_pantalla = (angulo_relativo + FOV / 2) / FOV * ANCHO
            item_y_pantalla = ALTO / 2 + (altura_proyectada / 2)
            distancia_al_muro = calcular_distancia_rayo(x_jugador, y_jugador, math.atan2(dy, dx))

            if distancia < distancia_al_muro:
                rect = imagen_escala.get_rect()
                rect.center = (int(item_x_pantalla), int(item_y_pantalla))
                pantalla.blit(imagen_escala, rect)






def generar_item_aleatorio():
    posiciones_validas = []
    for y in range(len(mapa)):
        for x in range(len(mapa[y])):
            if mapa[y][x] == '.':
                posiciones_validas.append((x, y))

    if posiciones_validas:
        x, y = random.choice(posiciones_validas)
        return Item(x * TAM_BLOQUE + TAM_BLOQUE // 2, y * TAM_BLOQUE + TAM_BLOQUE // 2)
    else:
        return None

def verificar_colision_item(x_jugador, y_jugador, item):
    if abs(x_jugador - item.x) < 20 and abs(y_jugador - item.y) < 20:
        return True
    return False


def pantalla_carga(pantalla, mensaje):
    pantalla.fill((0, 0, 0))  # Fondo negro
    texto = fuente.render(mensaje, True, COLOR_SELECCION)
    pantalla.blit(texto, (ANCHO // 2 - texto.get_width() // 2, ALTO // 2 - texto.get_height() // 2))
    pygame.display.flip()
    pygame.time.wait(2000)  # Esperar 2 segundos


def bucle_juego(nivel):



    global mapa, x_jugador, y_jugador, angulo_jugador, mouse_pos_anterior
    if nivel == 1:
        mapa = mapa_templo_desierto
    elif nivel == 2:
        mapa = mapa_ciudad_jungla
    elif nivel == 3:
        mapa = mapa

    item = generar_item_aleatorio()
    if item is None:
        print("No se pudo generar un item. Terminando el juego.")
        return


    juego_en_ejecucion = True
    while juego_en_ejecucion:

        pantalla.blit(imagen_de_fondo, (0, 0))

        if verificar_colision_item(x_jugador, y_jugador, item):
            item.recogido = True
            pantalla_carga(pantalla, "¡Excelente!")
            return

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                juego_en_ejecucion = False

        # Controles (simple)
        teclas = pygame.key.get_pressed()
        movimiento = False  # Para rastrear si el jugador se ha movido

        nueva_x_jugador = x_jugador
        nueva_y_jugador = y_jugador

        if teclas[pygame.K_w]:
            nueva_x_jugador += 2 * math.cos(angulo_jugador)
            nueva_y_jugador += 2 * math.sin(angulo_jugador)
            movimiento = True
        if teclas[pygame.K_s]:
            nueva_x_jugador -= 2 * math.cos(angulo_jugador)
            nueva_y_jugador -= 2 * math.sin(angulo_jugador)
            movimiento = True
        if teclas[pygame.K_a]:
            angulo_jugador -= 0.02
            movimiento = True
        if teclas[pygame.K_d]:
            angulo_jugador += 0.02
            movimiento = True
        if movimiento:
            reproducir_sonido_aleatorio()
        # Obtener la posición actual del mouse en el eje X
        mouse_pos_actual = pygame.mouse.get_pos()

        # Calcular la diferencia en la posición del mouse en el eje X
        diferencia_x_mouse = mouse_pos_actual[0] - mouse_pos_anterior[0]

        # Actualizar la orientación del jugador (rotación horizontal)
        angulo_jugador += diferencia_x_mouse * 0.005  # Ajusta la velocidad de rotación según tu preferencia

        # Actualizar la posición anterior del mouse
        mouse_pos_anterior = mouse_pos_actual

        # Comprobar colisión con las paredes
        bloque_x = int(nueva_x_jugador // TAM_BLOQUE)
        bloque_y = int(nueva_y_jugador // TAM_BLOQUE)

        if mapa[bloque_y][bloque_x] != '#':
            x_jugador = nueva_x_jugador
            y_jugador = nueva_y_jugador





        dibujar()

        # Obtener los FPS actuales
        fps = clock.get_fps()
        dibujar_fps(pantalla, fps)
        # Luego, en tu función de dibujo:
        if not item.recogido:
            item.dibujar_item_giratorio(pantalla, x_jugador, y_jugador, angulo_jugador)

        pygame.display.flip()

        clock.tick(65)  # Limitar a 30 FPS

    pygame.quit()


if __name__ == "__main__":

    pygame.init()
    pygame.mixer.init()
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    while True:  # Bucle principal para reiniciar el juego
        nivel = mostrar_menu_bienvenida(pantalla)
        if nivel == 0:
            break  # Salir del juego si se selecciona la opción para salir
        bucle_juego(nivel)  # Ejecutar el juego con el nivel seleccionado

    pygame.quit()
    sys.exit()
