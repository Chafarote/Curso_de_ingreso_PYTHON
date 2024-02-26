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
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        flag = True
        contador_genero_NB = 0
        contador_genero_F = 0
        contador_genero_M = 0
        contador_NB_ASP_JS_Ssr = 0
        contador_PHYTON = 0
        contador_JS = 0
        contador_ASP_NET = 0
        acumulador_edad_NB = 0
        acumulador_edad_F = 0
        acumulador_edad_M = 0

        for i in range(10):
            nombre = prompt("UTN Software Factory","Nombre del postulante:")
            while nombre == None or nombre == "" or nombre.isdigit():
                nombre = prompt("UTN Software Factory","Reingrese el nombre del postulante:")

            edad = prompt("UTN Software Factory","Edad del postulante:")
            while edad == None or edad == "" or not edad.isdigit() or int(edad) < 18:
                edad = prompt("UTN Software Factory","Reingrese la edad del postulante:")

            genero = prompt("UTN Software Factory","Genero del postulante:")
            while genero != "F" and genero != "M" and genero != "NB":
                genero = prompt("UTN Software Factory","Reingrese el genero del postulante:")

            tecnologia = prompt("UTN Software Factory","Tecnologia del postulante:")
            while tecnologia != "PHYTON" and tecnologia != "JS" and tecnologia != "ASP.NET":
                tecnologia = prompt("UTN Software Factory","Reingrese la tecnologia del postulante:")

            puesto = prompt("UTN Software Factory","Puesto del postulante:")
            while puesto != "Jr" and puesto != "Ssr" and puesto != "Sr":
                puesto = prompt("UTN Software Factory","reingrese el puesto del postulante:")

            print(f"{nombre}\n{edad}\n{genero}\n{tecnologia}\n{puesto}")

            edad = int(edad)

            match genero:
                case "NB":
                    acumulador_edad_NB += edad
                    contador_genero_NB += 1
                    if (tecnologia == "ASP.NET" or tecnologia == "JS") and (edad >= 25 and edad <= 40) and puesto == "Ssr":
                        contador_NB_ASP_JS_Ssr += 1
                case "F":
                    acumulador_edad_F += edad
                    contador_genero_F += 1
                case "M":
                    acumulador_edad_M += edad
                    contador_genero_M += 1

            match puesto:
                case "Jr":
                    if flag == True or edad < edad_minima_Jr:
                        edad_minima_Jr = edad
                        nombre_minimo_Jr = nombre
                        flag = False

            match tecnologia:
                case "PHYTON":
                    contador_PHYTON += 1
                case "JS":
                    contador_JS += 1
                case "ASP.NET":
                    contador_ASP_NET += 1

        if contador_PHYTON > contador_JS and contador_PHYTON > contador_ASP_NET:
            mayor_tecnologia = "PHYTON"
        elif contador_JS > contador_ASP_NET:
            mayor_tecnologia = "JS"
        else:
            mayor_tecnologia = "ASP.NET"

        if contador_genero_NB > 0:
            promedio_edad_NB = acumulador_edad_NB / contador_genero_NB
        else:
            promedio_edad_NB = 0
        if contador_genero_F > 0:
            promedio_edad_F = acumulador_edad_F / contador_genero_F
        else:
            promedio_edad_F = 0
        if contador_genero_M > 0:
            promedio_edad_M = acumulador_edad_M / contador_genero_M
        else:
            promedio_edad_M = 0
            

        total_postulantes = contador_genero_NB + contador_genero_F + contador_genero_M

        porcentaje_NB = contador_genero_NB * 100 / total_postulantes
        porcentaje_F = contador_genero_F * 100 / total_postulantes
        porcentaje_M = 100 - (porcentaje_NB + porcentaje_F)

        print(f"a. Cantidad de postulantes de genero No Binario que programan en ASP.NEt o JS postulados para Ssr: {contador_NB_ASP_JS_Ssr}")
        if flag == True:
            print(f"b. No se ingreso coincidencia")
        else:
            print(f"b. Nombre del posulante Jr mas joven: {nombre_minimo_Jr}")
        print(f"c. Promedio de edades por genero:\n\tFemenino: {promedio_edad_F}\n\tMasculino: {promedio_edad_M}\n\tNo Binario: {promedio_edad_NB}")
        print(f"d. Tecnologia con mas postulantes: {mayor_tecnologia}")
        print(f"e. Porcentaje de postulantes de cada genero:\n\tFemenino: {porcentaje_F}%\n\tMasculino: {porcentaje_M}%\n\tNo Binario: {porcentaje_NB}%")

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
