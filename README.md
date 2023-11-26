# Proyecto-2-Raycasting

## Descripción
Este proyecto es una implementación de un Ray Caster simple usando PyGame, inspirado en los backrooms. Consiste en un juego donde el jugador navega a través de niveles renderizados en 3D, evitando paredes y cumpliendo objetivos.

### Demostración
[![Vista previa del video](https://i9.ytimg.com/vi/AcjAaBYKXDg/mqdefault.jpg?sqp=CMynj6sG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGH8gEygTMA8=&rs=AOn4CLCyOjN2pKbvNb_U3SHQSI8r4OBJ4A)](https://youtu.be/AcjAaBYKXDg)

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
| Criterio                                        | Puntos Posibles | Puntos Completados|
|-------------------------------------------------|-----------------|-------------------|
| Estética del nivel                              | 0-30            | ?                 |
| Mantener alrededor de 15 fps                    | 15              | 15                |
| Cámara con movimiento y rotación                | 20              | 20                |
| Rotación con el mouse (solo horizontal)         | 10              | 10                | 
| Minimapa en una esquina                         | 10              | 10                |
| Música de fondo                                 | 5               | 5                 |
| Efectos de sonido                               | 10              | 10                |
| Al menos 1 animación en sprite                  | 20              | 20                |
| Pantalla de bienvenida                          | 5               | 5                 |
| Selección entre múltiples niveles               | 10              | 10                |
| Pantalla de éxito al cumplir una condición      | 10              | 10                |

## Autor
- [Javier Ramírez]
