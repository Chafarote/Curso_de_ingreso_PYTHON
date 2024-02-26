import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Gabriel
apellido: Gomez
tutor: Natalí
---
Ejercicio: for_08
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Mostrar cada número primo entre 1 y el número ingresado, e informar la cantidad de números primos encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador_numeros_primos = 0

        numero = prompt("UTN","Ingrese un numero:")
        numero = int(numero)

        for i in range(1,numero+1):
            contador_divisores = 0

            for j in range(1,i+1):
                if i % j == 0:
                    contador_divisores += 1

            if contador_divisores == 2:
                contador_numeros_primos += 1

        print(f"La cantidad de numeros primos es: {contador_numeros_primos}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()