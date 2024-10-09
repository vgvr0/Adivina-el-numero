import random
import pandas as pd
import getpass
import os
import matplotlib.pyplot as plt

# Ruta del archivo de estadísticas. Si solo pone nombre, guarda en la misma carpeta 
# donde está el script 
excel_estadisticas = 'estadisticas_partidas.xlsx'

# Función para guardar las estadísticas
def guarda_estadisticas(jugador, resultado, intentos, dificultad):
    if os.path.exists(excel_estadisticas):
        df = pd.read_excel(excel_estadisticas)
    else:
        df = pd.DataFrame(columns=['Jugador', 'Resultado', 'Intentos', 'Dificultad'])

    nueva_fila = pd.DataFrame({'Jugador': [jugador], 'Resultado': [resultado], 'Intentos': [intentos], 'Dificultad': [dificultad]})
    df = pd.concat([df, nueva_fila], ignore_index=True)
    df.to_excel(excel_estadisticas, index=False)
    print("Estadísticas guardadas.")

# Función para elegir la dificultad y definir el número de intentos
def elige_dificultad():
    while True:
        print("Elija la dificultad:")
        print("1. Fácil (20 intentos)")
        print("2. Medio (12 intentos)")
        print("3. Difícil (5 intentos)")
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                return 20, 'Fácil'
            elif opcion == 2:
                return 12, 'Medio'
            elif opcion == 3:
                return 5, 'Difícil'
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")

# Función para el modo solitario
def modo_solitario():
    print("\nModo Solitario: Adivina el número generado por el ordenador.")
    intentos, dificultad = elige_dificultad()
    numero_adivinar = random.randint(1, 1000)
    nombre_jugador = input("Ingrese su nombre: ")

    for intento in range(1, intentos + 1):
        try:
            guess = int(input(f"Intento {intento}/{intentos}. Adivina el número: "))
            if guess == numero_adivinar:
                print(f"¡Felicidades {nombre_jugador}, adivinaste el número {numero_adivinar} en {intento} intentos!")
                guarda_estadisticas(nombre_jugador, 'Ganó', intento, dificultad)
                return
            elif guess < numero_adivinar:
                print("El número es mayor.")
            else:
                print("El número es menor.")
        except ValueError:
            print("Entrada no válida. Debes ingresar un número.")
    
    print(f"Lo siento {nombre_jugador}, has perdido. El número era {numero_adivinar}.")
    guarda_estadisticas(nombre_jugador, 'Perdió', intentos, dificultad)

# Función para el modo 2 jugadores
def modo_dos_jugadores():
    print("\nModo 2 Jugadores: Un jugador elige el número, el otro intenta adivinarlo.")
    intentos, dificultad = elige_dificultad()
    nombre_jugador1 = input("Jugador 1, ingrese su nombre: ")
    nombre_jugador2 = input("Jugador 2, ingrese su nombre: ")

    while True:
        try:
            # Usamos getpass para ocultar la entrada del número del jugador 1
            numero_adivinar = int(getpass.getpass(f"{nombre_jugador1}, ingrese un número entre 1 y 1000 (oculto): "))
            if 1 <= numero_adivinar <= 1000:
                break
            else:
                print("El número debe estar entre 1 y 1000.")
        except ValueError:
            print("Entrada no válida. Debe ingresar un número entre 1 y 1000.")

    for intento in range(1, intentos + 1):
        try:
            guess = int(input(f"{nombre_jugador2}, intento {intento}/{intentos}. Adivina el número: "))
            if guess == numero_adivinar:
                print(f"¡Felicidades {nombre_jugador2}, adivinaste el número {numero_adivinar} en {intento} intentos!")
                guarda_estadisticas(nombre_jugador2, 'Ganó', intento, dificultad)
                return
            elif guess < numero_adivinar:
                print("El número es mayor.")
            else:
                print("El número es menor.")
        except ValueError:
            print("Entrada no válida. Debes ingresar un número.")

    print(f"Lo siento {nombre_jugador2}, has perdido. El número era {numero_adivinar}.")
    guarda_estadisticas(nombre_jugador2, 'Perdió', intentos, dificultad)

# Función para mostrar las estadísticas
def muestra_estadisticas():
    if os.path.exists(excel_estadisticas):
        df = pd.read_excel(excel_estadisticas)
        print("\nEstadísticas de las partidas:")
        print(df)

        # Graficar las estadísticas
        grafica_estadisticas(df)
    else:
        print("No hay estadísticas registradas aún.")

# Función para graficar las estadísticas
def grafica_estadisticas(df):
    resultados = df.groupby(['Jugador', 'Resultado']).size().unstack(fill_value=0)
    resultados.plot(kind='bar', stacked=True)
    plt.title('Resultados de las partidas')
    plt.xlabel('Jugador')
    plt.ylabel('Número de Partidas')
    plt.legend(title='Resultado')
    plt.tight_layout()
    plt.show()

