# main.py
"""
Este programa contiene la tarea "Adivina el número" (Entrega 1). El menú principal consta de:

1. Modo Solitario: el jugador intenta adivinar un número generado por el ordenador.
2. Modo 2 Jugadores: un jugador elige un número y el otro intenta adivinarlo.
3. Estadísticas: muestra las estadísticas de las partidas anteriores.
4. Salir: cierra el programa.

Las estadísticas se guardan en un archivo Excel y se pueden visualizar con un gráfico.

Módulos y librerías utilizadas:

1. random: genera números aleatorios en el modo solitario.
2. pandas: gestiona los datos de las partidas y los guarda en un Excel.
3. os: verifica si el archivo de estadísticas ya existe.
4. matplotlib.pyplot: genera gráficos de las estadísticas.
5. adivinanzaAux (módulo creado para este juego): contiene todas, incluyendo el modo solitario, 
    el modo 2 jugadores, la gestión de estadísticas y la visualización de gráficos.

"""

from adivinanzaAux import modo_solitario, modo_dos_jugadores, muestra_estadisticas

# Función principal del menú
def menu():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Partida modo solitario")
        print("2. Partida 2 Jugadores")
        print("3. Estadística")
        print("4. Salir")
        try:
            opcion = int(input("Seleccione una opción (1-4): "))
            if opcion == 1:
                modo_solitario()
            elif opcion == 2:
                modo_dos_jugadores()
            elif opcion == 3:
                muestra_estadisticas()
            elif opcion == 4:
                print("Gracias por jugar. ¡Hasta pronto!")
                break
            else:
                print("Opción no válida. Por favor seleccione una opción entre 1 y 4.")
        except ValueError:
            print("Opción no válida. Por favor seleccione una opción entre 1 y 4.")

# Ejecuta el menú principal
if __name__ == "__main__":
    menu()
