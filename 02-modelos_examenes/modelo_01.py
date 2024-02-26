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
Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar en la bolsa de 
valores:

Para ello deberás programar el botón  para poder cargar 10 operaciones de compra con los siguientes datos:
    * Nombre
    * Monto en pesos de la operación (no menor a $10000)
    * Tipo de instrumento(CEDEAR, BONOS, MEP) 
    * Cantidad de instrumentos  (no menos de cero) 
    
Realizar los siguientes informes:

    #! 1) - Tipo de instrumento que menos se operó en total.
    #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
    #! 3) - Cantidad de usuarios que no compraron CEDEAR 
    #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    #! 5) - Nombre y posicion del usuario que invirtio menos dinero
    #! 6) - Promedio de dinero en CEDEAR  ingresado en total.  
    #! 7) - Promedio de cantidad de instrumentos  MEP vendidos en total
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        flag_BONOS_CEDEAR = True
        flag_monto = True
        contador_CEDEAR = 0
        contador_BONOS = 0
        contador_MEP = 0
        contador_usuarios_MEP = 0
        acumulador_dinero_CEDEAR = 0
        acumulador_cantidad_MEP = 0

        for i in range(1,3+1):
            nombre = prompt("Bolsa de valores","Ingrese su nombre:")
            while nombre == None or nombre == "" or nombre.isdigit():
                nombre = prompt("Bolsa de valores","Reingrese su nombre:")

            monto_pesos = prompt("Bolsa de valores","Ingrese un monto en pesos:")
            while monto_pesos == None or monto_pesos == "" or not monto_pesos.isdigit() or int(monto_pesos) < 10000:
                monto_pesos = prompt("Bolsa de valores","reingrese un monto en pesos:")

            tipo_instrumento = prompt("Bolsa de valores","Ingrese el tipo de instrumento:") 
            while tipo_instrumento != "CEDEAR" and tipo_instrumento != "BONOS" and tipo_instrumento != "MEP":
                tipo_instrumento = prompt("Bolsa de valores","Ingrese el tipo de instrumento:")

            cantidad_instrumentos = prompt("Bolsa de valores","Ingrese la cantidad de instrumentos:")
            while cantidad_instrumentos == None or cantidad_instrumentos == "" or not cantidad_instrumentos.isdigit() or int(cantidad_instrumentos) < 0:
                cantidad_instrumentos = prompt("Bolsa de valores","Reingrese la cantidad de instrumentos:")

            cantidad_instrumentos = int(cantidad_instrumentos)

            match tipo_instrumento:
                case "CEDEAR":
                    contador_CEDEAR += 1
                    acumulador_dinero_CEDEAR += monto_pesos
                    if flag_BONOS_CEDEAR == True: #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
                        nombre_primer_CEDEAR_BONOS = nombre
                        monto_primer_CEDEAR_BONOS = monto_pesos
                        flag_BONOS_CEDEAR = False
                case "BONOS":
                    contador_BONOS += 1
                    if flag_BONOS_CEDEAR == True: #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
                        nombre_primer_CEDEAR_BONOS = nombre
                        monto_primer_CEDEAR_BONOS = monto_pesos
                        flag_BONOS_CEDEAR = False
                case "MEP":
                    contador_MEP += 1
                    acumulador_cantidad_MEP += cantidad_instrumentos
                    #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP
                    if cantidad_instrumentos >= 50 and cantidad_instrumentos <= 200:
                        contador_usuarios_MEP += 1

            #! 5) - Nombre y posicion del usuario que invirtio menos dinero
            if flag_monto == True or monto_pesos < monto_minimo:
                monto_minimo = monto_pesos
                nombre_monto_minimo = nombre
                posicion_monto_minimo = i
                flag_monto = False

        #! 1) - Tipo de instrumento que menos se operó en total.
        if contador_CEDEAR < contador_BONOS and contador_CEDEAR < contador_MEP:
            instrumento_menos_operado = "CEDEAR"
        elif contador_BONOS < contador_MEP:
            instrumento_menos_operado = "BONOS"
        else:
            instrumento_menos_operado = "MEP"

        #! 3) - Cantidad de usuarios que no compraron CEDEAR
        usuarios_no_CEDEAR = contador_BONOS + contador_MEP

        #! 6) - Promedio de dinero en CEDEAR  ingresado en total. 
        if contador_CEDEAR > 0:
            promedio_CEDEAR = acumulador_dinero_CEDEAR / contador_CEDEAR
        else:
            promedio_CEDEAR = 0

        #! 7) - Promedio de cantidad de instrumentos  MEP vendidos en total
        if contador_MEP > 0:
            promedio_cantidad_MEP = acumulador_cantidad_MEP / contador_MEP
        else:
            promedio_cantidad_MEP = 0

        print(f"1. Tipo de instrumento que menos se opero: {instrumento_menos_operado}")
        print(f"2. Cantidad de usuarios que comrparon entre 50 y 200 MEP: {contador_usuarios_MEP}")
        print(f"3. Cantidad de usuarios que no compraron CEDEAR: {usuarios_no_CEDEAR}")
        print(f"4. Primer usuario que compro CEDEAR o MEP:\n\t{nombre_primer_CEDEAR_BONOS}\n\t{monto_primer_CEDEAR_BONOS}")
        print(f"5. Usuario que invirtio menos dinero:\n\t{nombre_monto_minimo}\n\tFue el ingreso numero: {posicion_monto_minimo}")
        print(f"6. Promedio de dinero en CEDEAR en total: {promedio_CEDEAR}")
        print(f"7. Promedio de cantidad de instrumentos MEP en total: {promedio_cantidad_MEP}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()