import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Gabriel
apellido: Gomez
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos
    G. El máximo valor. 
    H. El mínimo valor (incluyendo en que iteracion se encontro, solo la primera)

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        contador_iteracion = 1
        contador_positivo = 0
        contador_negativo = 0
        contador_de_ceros = 0
        acumulador_positivo = 0
        acumulador_negativo = 0

        while True:
            numero = prompt("UTN","Ingrese un numero:")

            if numero == None or numero == "":
                break

            numero = int(numero)

            if contador_iteracion == 1 or numero > numero_maximo:
                numero_maximo = numero
            if contador_iteracion == 1 or numero < numero_minimo:
                numero_minimo = numero
                iteracion_negativa = contador_iteracion

            contador_iteracion += 1

            if numero > 0:
                acumulador_positivo += numero
                contador_positivo += 1
            elif numero < 0:
                acumulador_negativo += numero
                contador_negativo += 1
            else:
                contador_de_ceros += 1

        diferencia = contador_negativo - contador_positivo
        if diferencia < 0:
            diferencia *= -1

        if contador_iteracion == 1:
            alert("Resultado","No se ingresaron datos")
        else:
            mensaje = f"La suma acumulada de los negativos es: {acumulador_negativo} \nLa suma acumulada de los positivos es: {acumulador_positivo} \nLa cantidad de numeros positivos ingresados es: {contador_positivo} \nLa cantidad de numeros negatos es: {contador_negativo} \nLa cantidad de ceros es: {contador_de_ceros} \nLa diferencia entre la cantidad de numeros negativos y positivos ingresados es de: {diferencia} \nEl maximo valor es: {numero_maximo} \nEl valor minimo es: {numero_minimo} y fue ingresado en la iteracion: {iteracion_negativa}"
            alert("Resultado",mensaje)

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
