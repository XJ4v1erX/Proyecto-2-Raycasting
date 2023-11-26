# Proyecto-2-Raycasting

## Descripción
Este proyecto es una implementación de un Ray Caster simple usando PyGame, inspirado en los backrooms. Consiste en un juego donde el jugador navega a través de niveles renderizados en 3D, evitando paredes y cumpliendo objetivos.

### Demostración
- [Link al video demostrativo](URL_DEL_VIDEO)

### Técnica del Ray Caster
El Ray Caster es una técnica de renderizado para crear una perspectiva 3D en juegos. Utiliza rayos proyectados desde la posición del jugador para calcular la distancia a las paredes y otros objetos, determinando así cómo deben ser renderizados en la pantalla.

### Inspiración: Los Backrooms
Los backrooms son una leyenda urbana sobre un espacio infinito de habitaciones y pasillos monótonos. Esta idea fue la inspiración para el diseño y la estética de los niveles en este proyecto.

## Estructura del Proyecto
- `main.py`: Script principal del juego.
- `settings.py`: Configuraciones del juego como dimensiones de pantalla, colores, etc.
- `levels.py`: Define los niveles del juego y sus características.
- Carpeta `assets`: Contiene recursos como sonidos, texturas y sprites.

## Uso
1. Instalar Python y PyGame.
2. Clonar el repositorio.
3. Ejecutar `main.py` para iniciar el juego.
4. Navegar por los menús para seleccionar un nivel.
5. Jugar usando el teclado y el mouse para la navegación.

### Controles del Juego
| Tecla | Acción                    |
|-------|---------------------------|
| W     | Mover hacia adelante      |
| A     | Mover hacia la izquierda  |
| S     | Mover hacia atrás         |
| D     | Mover hacia la derecha    |
| Enter | Seleccionar en el menú    |
| Mouse | Rotación horizontal       |

## Puntos Completados
- **Estética del nivel (0-30 puntos)**
- **FPS mantenidos alrededor de 15 (15 puntos)**
- **Cámara con movimiento y rotación (20 puntos)**
- **Rotación con el mouse (10 puntos adicionales)**
- **Minimapa en una esquina (10 puntos)**
- **Música de fondo (5 puntos)**
- **Efectos de sonido (10 puntos)**
- **Al menos 1 animación en sprite (20 puntos)**
- **Pantalla de bienvenida (5 puntos)**
- **Selección entre múltiples niveles (10 puntos adicionales)**
- **Pantalla de éxito al cumplir una condición (10 puntos)**

## Autor
- Javier Ramírez
