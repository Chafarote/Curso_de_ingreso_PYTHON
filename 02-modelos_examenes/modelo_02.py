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
Se nos ha solicitado desarrollar una aplicación para llevar registro de las entradas vendidas en el Estadio River 
Plate, para el concierto de Taylor Swift. Para ello, se solicitará al usuario la siguiente información al momento de 
comprar cada entrada:

Al presionar el boton se debera pedir la carga de los siguientes datos, hasta que el usuario lo desee:

Los datos que deberas pedir para los ventas son:
    * Nombre del comprador
    * Edad (no menor a 16)
    * Género (Masculino, Femenino, Otro)
    * Tipo de entrada (General, Campo delantero, Platea)
    * Medio de pago (Crédito, Efectivo, Débito) 
    * Precio de la entrada (Se debe calcular)

Para cada venta, se calculará el total a pagar en función del tipo de entrada elegida, 
el medio de pago y su precio correspondiente.

 * Lista de precios: 
        * General: $16000
        * Campo:   $25000
        * Platea:  $30000

Las entradas adquiridas con tarjeta de crédito tendrán un 20% de descuento sobre el 
precio de la entrada, mientras que las adquiridas con tarjeta de débito un 15%. 

Al finalizar la carga, el programa debera mostrar los siguientes informes:

    #! 1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
    #! 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta 
    #!          de crédito y su edad promedio.
    #! 3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y 
    #!          pagaron con tarjeta de débito  respecto al total de personas en la lista.
    #! 4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de 
    #!          los aplicados a tarjetas de crédito
    #! 5) - El nombre y la edad de la persona que pagó el precio más alto por una entrada de 
    #!          tipo "General" y pagó con tarjeta de débito (Solo la primera que se encuentre)
    #! 6) - La cantidad de personas que compraron entradas de tipo "Platea" y cuya 
    #!          edad es un número primo.
    #! 7) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y 
    #!          pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        flag = True

        GENERAL = 16000
        CAMPO = 25000
        PLATEA = 30000

        contador_clientes = 0
        contador_femenino = 0
        contador_masculino = 0
        contador_otro = 0
        contador_general_credito = 0
        contador_platea_debito = 0
        contador_edad_primos = 0
        acumulador_edad_general_credito = 0
        acumulador_descuento_credito = 0
        acumulador_platea_mutltiplo_de_6 = 0

        continuar = True

        while continuar == True:
            nombre = prompt("Entradas","Ingrese su nombre:")
            while nombre == None or nombre == "" or nombre.isdigit():
                nombre = prompt("Entradas","Reingrese su nombre:")

            edad = prompt("Entradas","Ingrese su edad:")
            while edad == None or edad == "" or not edad.isdigit() or int(edad) < 16:
                edad = prompt("Entradas","Reingrese su edad:")

            genero = prompt("Entradas","Ingrese su genero:")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = prompt("Entradas","Reingrese su genero:")

            tipo_entrada = prompt("Entrada","Ingrese el tipo de entrada:")
            while tipo_entrada != "General" and tipo_entrada != "Campo Delantero" and tipo_entrada != "Platea":
                tipo_entrada = prompt("Entrada","reingrese el tipo de entrada:")

            medio_de_pago = prompt("Entrada","Ingrese el medio de pago:")
            while medio_de_pago != "Credito" and medio_de_pago != "Efectivo" and medio_de_pago != "Debito":
                medio_de_pago = prompt("Entrada","Reingrese el medio de pago:")

            contador_clientes += 1

            edad = int(edad)

            match tipo_entrada:
                case "General":
                    precio_entrada = GENERAL
                    #! 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta 
                    if medio_de_pago == "Credito":
                        contador_general_credito += 1 
                        acumulador_edad_general_credito += edad
                    #! 5) - El nombre y la edad de la persona que pagó el precio más alto por una entrada de tipo "General" y pagó con tarjeta de débito (Solo la primera que se encuentre)
                    elif flag == True and medio_de_pago == "Debito":
                        nombre_primero_general = nombre
                        edad_primero_general = edad
                        flag = False
                case "Campo Delantero":
                    precio_entrada = CAMPO
                    if genero == "Femenino":
                        contador_femenino += 1
                    elif genero == "Masculino":
                        contador_masculino += 1
                    else:
                        contador_otro += 1
                case "Platea":
                    precio_entrada = PLATEA
                    if medio_de_pago == "Debito":
                        contador_platea_debito += 1

                    #! 6) - La cantidad de personas que compraron entradas de tipo "Platea" y cuya edad es un número primo.
                    contador_divisores = 0
                    for i in range(1,edad+1):
                        if edad % i == 0:
                            contador_divisores +=1

                    if contador_divisores == 2:
                        contador_edad_primos += 1

                    

            match medio_de_pago:
                case "Credito":
                    descuento = precio_entrada * 0.20
                case "Debito":
                    descuento = precio_entrada * 0.15
                case "Efectivo":
                    descuento = 0

            total_entrada = precio_entrada - descuento

            #! 4) - Cuál es el total de descuentos en pesos que aplicó la empresa, pero solo de los aplicados a tarjetas de crédito
            if medio_de_pago == "Credito":
                acumulador_descuento_credito += descuento
            elif medio_de_pago == "Debito" and tipo_entrada == "Platea" and (edad % 6) == 0:
                acumulador_platea_mutltiplo_de_6 += total_entrada
            #! 7) - Calcula el monto total recaudado por la venta de entradas de tipo "Platea" y pagadas con tarjeta de debito por personas cuyas edades son múltiplos de 6.

            print(f"El precio total de su entrada es de ${total_entrada}")

            continuar = question("Entradas","Desea continuar?")

        #! 1) - Determina el género más frecuente entre las personas que compraron entradas de tipo "Campo".
        if contador_femenino > contador_masculino and contador_femenino > contador_otro:
            genero_frecuente_campo = "Femenino"
        elif contador_masculino > contador_otro:
            genero_frecuente_campo = "Masculino"
        else:
            genero_frecuente_campo = "Otro"

        #! 2) - Determina cuántas personas compraron entradas de tipo "General" pagando con tarjeta 
        if contador_general_credito > 0:
            promedio_edad_general_credito = acumulador_edad_general_credito / contador_general_credito
        else:
            promedio_edad_general_credito = "No se ingresaron coincidencias"

        #! 3) - Calcula el porcentaje de personas que compraron entradas de tipo "Platea" y pagaron con tarjeta de débito  respecto al total de personas en la lista.
        if contador_platea_debito > 0:
            porcentaje_platea_debito = contador_platea_debito * 100 / contador_clientes
        else:
            porcentaje_platea_debito = 0

        print(f"1. Genero mas frecuente en campo: {genero_frecuente_campo}")
        print(f"2. Cantidad de personas que compraron entradas de tipo General con tarjeta de credito: {contador_general_credito}\n\tEdad promedio: {promedio_edad_general_credito}")
        print(f"3. Porcentaje de personas con entrada de Platea y abonaron con tarjeta de Debito: {porcentaje_platea_debito}%")
        print(f"4. Total de descuento aplicado a compras con tajeta de credito: {acumulador_descuento_credito}")
        if flag == True:
            print(f"5. Ninguna persona compro una entrada General abonando con debito")
        else:
            print(f"5. Persona que pago el monto mas alto por una entrada General abonando con debito:\n\tNombre: {nombre_primero_general}\n\tEdad: {edad_primero_general}")
        print(f"Cantidad de personas con entrada de Platea cuya edad es un numero primo: {contador_edad_primos}")
        print(f"Monto recaudado con entradas de Platea, abonadas con tarjeta de debito cpor clientes los cuales su edad es multiplo de 6: {acumulador_platea_mutltiplo_de_6}")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()