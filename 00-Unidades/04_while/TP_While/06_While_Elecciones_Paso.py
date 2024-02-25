import re
import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Gabriel
apellido: Gomez
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        continuar = True
        contador_iteracion = 0
        acumulador_votos = 0
        acumulador_edades = 0

        while continuar == True:

            nombre = prompt("Elecciones","Nombre del candidato:")

            while nombre == None or nombre == "":
                nombre = prompt("Elecciones","Reingrese nombre del candidato:")

            edad = prompt("Elecciones","Edad del candidato:")
            while edad == None or edad == "" or not edad.isdigit() or int(edad) < 26:
                edad = prompt("Elecciones","Reingrese la edad del candidato:")

            edad = int(edad)
            acumulador_edades += edad

            cantidad_votos = prompt("Elecciones","Cantidad de votos:")
            while cantidad_votos == None or cantidad_votos == "" or not cantidad_votos.isdigit() or int(cantidad_votos) < 0:
                cantidad_votos = prompt("Elecciones","Reingrese la cantidad de votos:")

            contador_iteracion += 1

            cantidad_votos = int(cantidad_votos)
            acumulador_votos += cantidad_votos

            if contador_iteracion == 1 or cantidad_votos > numero_maximo:
                numero_maximo = cantidad_votos
                nombre_maximo = nombre

            if contador_iteracion == 1 or cantidad_votos < numero_minimo:
                numero_minimo = cantidad_votos
                nombre_minimo = nombre
                edad_minimo = edad

            continuar = question("Elecciones","Desea continuar?")

        if contador_iteracion == 0:
            mensaje = f"No se ingresaron datos"
        else:
            promedio_edades = acumulador_edades / contador_iteracion
            mensaje = f"Candidato con mas votos: {nombre_maximo} \nCandidato con menos votos: {nombre_minimo} edad: {edad_minimo} \nPromedio de edades: {promedio_edades} \nTotal de votos emitidos: {acumulador_votos}"

        alert("Elecciones",mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
