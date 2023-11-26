import pygame
import pygame.mixer
import random
from settings import *
from levels import *
import sys

pygame.init()
pantalla = pygame.display.set_mode((ANCHO, ALTO))
clock = pygame.time.Clock()
fuente = pygame.font.Font(None, 48)
x_jugador, y_jugador = 150, 150
angulo_jugador = 0
mouse_pos_anterior = pygame.mouse.get_pos()

pygame.display.set_caption("Ray Caster Backrooms")


# Asegúrate de tener esta canción

# Crear una superficie para el minilevel
minilevel_surface = pygame.Surface(TAM_MINIMAPA)

# Cargar el sonido de pasos
archivos_sonidos = ["assets\sounds\step\step1.mp3", "assets\sounds\step\step2.mp3", "assets\sounds\step\step3.mp3", "assets\sounds\step\step4.mp3", "assets\sounds\step\step5.mp3", "assets\sounds\step\step6.mp3", "assets\sounds\step\step7.mp3"]

# Cargar todos los sonidos
sonidos_pasos = [pygame.mixer.Sound(archivo) for archivo in archivos_sonidos]


# Intervalo mínimo en milisegundos entre reproducciones de sonido
intervalo_minimo = 500  # 0.5 segundos
tiempo_ultima_reproduccion = 0  # Iniciar el tiempo de la última reproducción

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
        if level[int(y // TAM_BLOQUE)][int(x // TAM_BLOQUE)] == '#':
            return i
    return MAX_DIST

def dibujar(color_fondo, color_pared):

    pantalla.fill(color_fondo)
    for rayo in range(0, NUM_RAYS):
        angulo_rayo = angulo_jugador - (FOV / 2) + (FOV * rayo / NUM_RAYS)
        distancia = calcular_distancia_rayo(x_jugador, y_jugador, angulo_rayo)

        # Comprobar si la distancia es cero o muy pequeña para evitar divisiones por cero
        if distancia <= 0.01:
            continue
        color_pared = (color_pared)  # Por ejemplo, un gris
        color_atenuado = [color / (1 + distancia * distancia * 0.0001) for color in color_pared]

        altura_pared = (TAM_BLOQUE / distancia) * 277  # Proyección en pantalla
        #color = 255 / (1 + distancia * distancia * 0.0001)  # Atenuación de color
        #pygame.draw.rect(pantalla, (color, color, color), (rayo * RESOLUCION, (ALTO / 2) - (altura_pared / 2), RESOLUCION, altura_pared))
        pygame.draw.rect(pantalla, color_atenuado, (rayo * RESOLUCION, (ALTO / 2) - (altura_pared / 2), RESOLUCION, altura_pared))
        # Dibujar el minilevel
        dibujar_minilevel(pantalla, x_jugador, y_jugador, level)

        # Dibujar los FPS en la esquina derecha superior
        fps = clock.get_fps()
        dibujar_fps(pantalla, fps)

    pygame.display.flip()

def dibujar_minilevel(pantalla, x_jugador, y_jugador, level):
    minilevel_surface.fill((0, 0, 0))  # Limpiar la superficie del minilevel
    tam_bloque_minilevel = 11  # Tamaño de cada bloque en el minilevel

    # Dibujar el level en el minilevel
    for y in range(len(level)):
        for x in range(len(level[y])):
            bloque = level[y][x]
            if bloque == '#':
                pygame.draw.rect(minilevel_surface, (255, 255, 255), (x * tam_bloque_minilevel, y * tam_bloque_minilevel, tam_bloque_minilevel, tam_bloque_minilevel))

    # Dibujar la posición del jugador en el minilevel
    pygame.draw.circle(minilevel_surface, (255, 0, 0), (int(x_jugador / TAM_BLOQUE * tam_bloque_minilevel), int(y_jugador / TAM_BLOQUE * tam_bloque_minilevel)), 4)

    # Dibujar el minilevel en la pantalla principal
    pantalla.blit(minilevel_surface, POS_MINIMAPA)

def dibujar_fps(pantalla, fps):
    texto_fps = fuente.render(f"FPS: {int(fps)}", True, COLOR_TEXTO)
    pantalla.blit(texto_fps, (ANCHO - texto_fps.get_width() - 10, 10))




def mostrar_menu_bienvenida(pantalla):
    opciones = ["L3V31 0", "1ev3l 1", "L3ve1 2"]
    seleccion_actual = 0
    corriendo = True
    titulo = "Welcome to the B4ckr00ms"

    pygame.mixer.music.load('assets/sounds/menu.mp3')
    pygame.mixer.music.play(-1)  # Reproduce la música de fondo en bucle

    while corriendo:
        # Renderizar el título
        texto_titulo = fuente.render(titulo, True, COLOR_TITULO)
        pantalla.blit(texto_titulo, (ANCHO // 2 - texto_titulo.get_width() // 2, 100))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.mixer.music.stop()  # Detén la música antes de salir
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    corriendo = False
                if evento.key == pygame.K_w:
                    seleccion_actual = (seleccion_actual - 1) % len(opciones)
                if evento.key == pygame.K_s:
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
    pygame.image.load('assets\sprites\coin1.png').convert_alpha(),
    pygame.image.load('assets\sprites\coin2.png').convert_alpha(),
    pygame.image.load('assets\sprites\coin3.png').convert_alpha(),
    pygame.image.load('assets\sprites\coin4.png').convert_alpha(),
    pygame.image.load('assets\sprites\coin5.png').convert_alpha(),
    pygame.image.load('assets\sprites\coin6.png').convert_alpha(),
    pygame.image.load('assets\sprites\coin7.png').convert_alpha(),
]


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
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
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
    pygame.time.wait(2000)
    pantalla.fill((0, 0, 0))
    pygame.display.flip()  # Esperar 2 segundos





def bucle_juego(nivel):



    global level, x_jugador, y_jugador, angulo_jugador, mouse_pos_anterior
    if nivel == 1:
        level = levels["level1"]
    elif nivel == 2:
        level = levels["level2"]
    elif nivel == 3:
        level = levels["level3"]
    pygame.mixer.music.load('assets/sounds/buzzz.mp3')
    pygame.mixer.music.play(-1)  # Reproduce la música de fondo en bucle
    item = generar_item_aleatorio()
    if item is None:
        print("No se pudo generar un item. Terminando el juego.")
        return


    juego_en_ejecucion = True
    while juego_en_ejecucion:



        if verificar_colision_item(x_jugador, y_jugador, item):
            pygame.mixer.music.stop()
            item.recogido = True
            pygame.mixer.music.load('assets/sounds/colected.mp3')
            pygame.mixer.music.play(-1)
            pantalla_carga(pantalla, "¡Maybe win!")
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

        if level[bloque_y][bloque_x] != '#':
            x_jugador = nueva_x_jugador
            y_jugador = nueva_y_jugador

        dibujar(color_fondo=colores_fondo[f"level{nivel}"],color_pared=colores_pared[f"level{nivel}"])

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
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    while True:  # Bucle principal para reiniciar el juego
        nivel = mostrar_menu_bienvenida(pantalla)

        if nivel == 0:
            break  # Salir del juego si se selecciona la opción para salir
        bucle_juego(nivel)  # Ejecutar el juego con el nivel seleccionado
