import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter
import random

'''
nombre: Gabriel
apellido: Gomez
tutor: Natalí
----------
Simulacro Turno Noche

Un famoso casino de mar del plata,  requiere una app para controlar el egreso de dinero durante una jornada. Para ello se ingresa por cada ganador:

Nombre

Importe ganado (mayor o igual $1000)

Género (“Femenino”, “Masculino”, “Otro”)

Juego (Ruleta, Poker, Tragamonedas)

Necesitamos saber:

Nombre y género de la persona que más ganó.

Promedio de dinero ganado en Ruleta.

Porcentaje de personas que jugaron en el Tragamonedas.

Cuál es el juego menos elegido por los ganadores.

El nombre del jugador que ganó más dinero jugando Poker
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        flag_maximo = True
        flag_maximo_poker = True
        continuar = True

        contador_ruleta = 0
        contador_tragamonedas = 0
        contador_poker = 0
        acumulador_dinero_ruleta = 0

        while continuar == True:
            nombre = prompt("Ganadores","Ingrese el nombre:")
            while nombre == None or nombre == "" or nombre.isdigit():
                nombre = prompt("Ganadores","reingrese el nombre:")

            importe_ganado = prompt("Ganadores","Ingrese el importe ganado:")
            while importe_ganado == None or importe_ganado == "" or not importe_ganado.isdigit() or int(importe_ganado) < 1000:
                importe_ganado = prompt("Ganadores","Reingrese el importe ganado:")

            genero = prompt("Ganadores","Ingrese el genero del ganador:")
            while genero != "Femenino" and genero != "Masculino" and genero != "Otro":
                genero = prompt("Ganadores","reingrese el genero del ganador:")

            juego = prompt("Ganadores","Ingrese el juego:")
            while juego != "Ruleta" and juego != "Poker" and juego != "Tragamonedas":
                juego = prompt("Ganadores","Reingrese el juego:")

            importe_ganado = int(importe_ganado)

            match juego:
                case "Ruleta":
                    contador_ruleta += 1
                    acumulador_dinero_ruleta += importe_ganado
                case "Poker":
                    contador_poker += 1
                    if flag_maximo_poker == True or importe_ganado > maximo_poker:
                        maximo_poker = importe_ganado
                        maximo_ganador_poker = nombre
                        flag_maximo_poker = False
                case "Tragamonedas":
                    contador_tragamonedas += 1

            if flag_maximo == True or importe_ganado > maximo_ganador:
                maximo_ganador = importe_ganado
                nombre_maximo_ganador = nombre
                genero_maximo_ganador = genero
                flag_maximo = False

            continuar = question("Desea continuar?")

        if contador_ruleta > 0:
            promedio_ruleta = acumulador_dinero_ruleta / contador_ruleta
        else:
            promedio_ruleta = "No hubo ingresos de ruleta"

        if contador_ruleta < contador_poker and contador_ruleta < contador_tragamonedas:
            juego_menos_elegido = "Ruleta"
        elif contador_poker < contador_tragamonedas:
            juego_menos_elegido = "Poker"
        else:
            juego_menos_elegido = "Tragamonedas"

        total_personas = contador_poker + contador_ruleta + contador_tragamonedas

        porcentaje_tragamonedas = contador_tragamonedas * 100 / total_personas

        print(f"1. Nombre y genero de la persona que mas gano:\n\t{nombre_maximo_ganador}\n\t{genero_maximo_ganador}")
        print(f"2. Promedio de dinero ganado en Ruleta: {promedio_ruleta}")
        print(f"3. Porcentaje de personas que jugaron en el Tragamonedas: {porcentaje_tragamonedas}%")
        print(f"4. Juego menos elegido por los ganadores: {juego_menos_elegido}")
        if flag_maximo_poker == False:
            print(f"5. Persona que gano mas dinero jugando Poker: {maximo_ganador_poker}")
        else:
            print(f"5. No se ingreso ningun ganador de Poker")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()