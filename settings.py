import math

# Configuración inicial
ANCHO, ALTO = 800, 600
FOV = math.pi / 3  # Campo de visión
NUM_RAYS = 120  # Número de rayos
MAX_DIST = 800  # Distancia máxima de renderizado
RESOLUCION = ANCHO // NUM_RAYS
# Tamaño del minimapa y su posición en la pantalla
TAM_MINIMAPA = (99, 99)
POS_MINIMAPA = (10, 10)
# Colores
COLOR_TEXTO = (255, 255, 255)
COLOR_SELECCION = (128, 129, 128)  # Dorado

# Tamaño del bloque en el mapa
TAM_BLOQUE = 100

# Escala las imágenes al tamaño deseado
TAM_BLOQUE = 50  # O el tamaño que necesites
COLOR_TITULO = (63, 66, 68)
