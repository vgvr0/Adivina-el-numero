# Adivina el número

Este es un juego de adivinanza en Python, donde los jugadores intentan adivinar un número entre 1 y 1000. El juego ofrece dos modos: solitario y 2 jugadores. Las estadísticas de las partidas se guardan en un archivo Excel.

## Requisitos

- Python 3.12.3
- Librerías necesarias:
  - `random`
  - `pandas`
  - `getpass`
  - `os`
  - `matplotlib`

Puedes instalar las librerías que no tengas ejecutando:
```bash
pip install pandas matplotlib
```

## Cómo ejecutar el juego

Para ejecutar el juego, simplemente ejecuta el script en tu terminal:
```bash
python nombre_del_script.py
```

## Modos de juego

1. **Modo Solitario:** El jugador intenta adivinar un número generado por la computadora en un número limitado de intentos, dependiendo del nivel de dificultad seleccionado.
2. **Modo 2 Jugadores:** Un jugador elige un número, y el otro intenta adivinarlo. El número de intentos está limitado por la dificultad elegida.

## Funcionalidades

### 1. Guardar estadísticas

Las estadísticas de cada partida se almacenan en un archivo Excel (`estadisticas_partidas.xlsx`). Los datos guardados incluyen:

- Nombre del jugador
- Resultado de la partida (Ganó o Perdió)
- Número de intentos utilizados
- Dificultad elegida

### 2. Selección de la dificultad

El jugador puede seleccionar uno de los siguientes niveles de dificultad:

- **Fácil:** 20 intentos
- **Medio:** 12 intentos
- **Difícil:** 5 intentos

### 3. Modo Solitario

En este modo, el jugador intenta adivinar un número generado aleatoriamente por el ordenador entre 1 y 1000. El jugador tiene un número de intentos limitado según la dificultad elegida.

### 4. Modo 2 Jugadores

En el modo para dos jugadores, un jugador introduce un número de forma oculta usando `getpass`, y el otro jugador intenta adivinarlo. Al igual que en el modo solitario, los intentos son limitados según la dificultad seleccionada.

### 5. Mostrar estadísticas

El juego permite visualizar un resumen de las estadísticas almacenadas en el archivo Excel. Si existen datos, se muestra un gráfico de barras con los resultados de las partidas.

### 6. Graficar las estadísticas

Se utiliza la librería `matplotlib` para graficar las estadísticas de las partidas, mostrando el número de partidas ganadas y perdidas por cada jugador.

## Ejemplo de Uso

### Iniciar el juego

Cuando ejecutes el script, se te pedirá que elijas entre los modos de juego disponibles:
- Modo Solitario
- Modo 2 Jugadores
- Ver Estadísticas

Sigue las instrucciones en la pantalla para completar la partida.

### Ver las estadísticas

Selecciona la opción de mostrar estadísticas para visualizar un resumen de los juegos anteriores. Si hay datos registrados, se mostrará un gráfico de barras.

## Personalización

Puedes modificar la ruta del archivo de estadísticas cambiando el valor de la variable `excel_estadisticas` en el script:
```python
excel_estadisticas = 'ruta_personalizada/estadisticas_partidas.xlsx'
```

## Contribuciones

Si deseas contribuir a este proyecto, puedes hacerlo creando un fork del repositorio, haciendo tus cambios y enviando un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Puedes ver el archivo `LICENSE` para más detalles.
```

Este archivo proporciona una descripción general del juego, sus funcionalidades, cómo ejecutarlo y personalizarlo, además de otros detalles importantes.
