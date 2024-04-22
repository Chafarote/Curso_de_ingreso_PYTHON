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

UTN Tecnologies, una reconocida software factory se encuentra en la busqueda de ideas para su proximo desarrollo en python, 
que promete revolucionar el mercado. 
Las posibles aplicaciones son las siguientes: 
# Inteligencia artificial (IA),
# Realidad virtual/aumentada (RV/RA), 
# Internet de las cosas (IOT) o 


Para ello, realiza entre sus empleados una encuesta, con el propósito de conocer ciertas métricas:

Los datos a ingresar por cada encuestado son:
    * nombre del empleado
    * edad (no menor a 18)
    * genero (Masculino - Femenino - Otro)
    * tecnologia (IA, RV/RA, IOT)   

En esta opción, se ingresaran empleados hasta que el usuario lo desee.

Una vez finalizado el ingreso, mostrar:

    #!X 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
    #!X 2) - Tecnología que mas se votó.
    #!X 3) - Porcentaje de empleados por cada genero
    #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.  
    #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
    #!X 6) - Nombre y género del empleado que voto por RV/RA con menor edad.

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        continuar = True

        contador_masculino = 0
        contador_femenino = 0
        contador_otro = 0
        contador_masculino_IOT_IA = 0
        contador_IA = 0
        contador_RV_RA = 0
        contador_IOT = 0
        contador_IOT_rango_edad = 0
        contador_femenino_IA = 0
        acumulador_edad_femenino_IA = 0


        while continuar == True:
            nombre = prompt("Encuesta","Ingrese su nombre:")
            while nombre == None or nombre == "" or nombre.isdigit():
                nombre = prompt("Encuesta","Reingrese su nombre:")

            edad = prompt("Encuesta","Ingrese su edad:")
            while edad == None or edad == "" or not edad.isdigit() or int(edad) < 18:
                edad = prompt("Encuesta","Reingrese su edad:")

            genero = prompt("Encuenta","Ingrese su genero:")
            while genero != "Masculino" and genero != "Femenino" and genero != "Otro":
                genero = prompt("Encuenta","Reingrese su genero:")

            tecnologia = prompt("Encuesta","Ingrese su tecnologia:")
            while tecnologia != "IA" and tecnologia != "RV/RA" and tecnologia != "IOT":
                tecnologia = prompt("Encuesta","Reingrese su tecnologia:")

            edad = int(edad)

            match genero:
                case "Masculino":
                    contador_masculino += 1
                    # 1) - Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad este entre 25 y 50 años inclusive.
                    if tecnologia == "IOT" or tecnologia == "IA" and (edad >= 25 and edad <= 50):
                        contador_masculino_IOT_IA += 1
                case "Femenino":
                    contador_femenino += 1
                    if tecnologia == "IA":
                        acumulador_edad_femenino_IA += edad
                        contador_femenino_IA += 1
                case "Otro":
                    contador_otro += 1

            match tecnologia:
                case "IA":
                    contador_IA += 1
                case "RV/RA":
                    contador_RV_RA += 1
                    if contador_RV_RA == 1 or edad_minima > edad:
                        edad_minima = edad
                        nombre_minimo = nombre
                        genero_minimo = genero
                case "IOT":
                    contador_IOT += 1
                    # 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.
                    if (edad >= 18 and edad <= 25) or (edad >= 33 and edad <= 42):
                        contador_IOT_rango_edad += 1

            continuar = question("Encuesta","Desea continuar?")

        # 2) - Tecnología que mas se votó.
        if contador_IA > contador_RV_RA and contador_IA > contador_IOT:
            tecnologia_mas_votada = "IA"
        elif contador_RV_RA > contador_IOT:
            tecnologia_mas_votada = "RV/RA"
        else:
            tecnologia_mas_votada = "IOT"

        #!X 3) - Porcentaje de empleados por cada genero
        total_empleados = contador_masculino + contador_femenino + contador_otro
        porcentaje_mascuilino = contador_masculino * 100 / total_empleados
        porcentaje_femenino = contador_femenino * 100 / total_empleados
        porcentaje_otro = contador_otro * 100 / total_empleados

        #!X 4) - Porcentaje de empleados que votaron por IOT, siempre y cuando su edad se encuentre entre 18 y 25 o entre 33 y 42.
        porcentaje_IOT_rango_edad = contador_IOT_rango_edad * 100 / total_empleados


        print(f"Cantidad de empleados de género masculino que votaron por IOT o IA: {contador_masculino_IOT_IA}")
        print(f"La tecnologia mas votada es: {tecnologia_mas_votada}")
        print(f"Porcentaje de empleados por genero:\n\tMasculino: {porcentaje_mascuilino}%\n\tFemenino: {porcentaje_femenino}%\n\tOtro: {porcentaje_otro}%")
        print(f"El porcentaje de empleados que voto IOT en el rango de edad establecido es: {porcentaje_IOT_rango_edad}%")
        #!X 5) - Promedio de edad de los empleados de genero Femenino que votaron por IA
        if contador_femenino_IA > 0:
            promedio_edad_femenino_IA = acumulador_edad_femenino_IA / contador_femenino_IA
            print(f"Promedio de edad de genero femenino que voto IA: {promedio_edad_femenino_IA}")
        else:
            print(f"No se ingresaron empleados de genero femenino que hayan votado IA")
        if contador_RV_RA > 0:
            print(f"El empleado que voto RV/RA con menor edad es:\n\tNombre: {nombre_minimo}\n\tGenero: {genero_minimo}")
        else:
            print("No se ingresaron empleados que hayan votado RV/RA")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()