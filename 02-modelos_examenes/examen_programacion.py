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

De 20 contenedores que llegan al puerto de Rosario, se deben pedir y validar los siguientes datos

Marca (no validar)
Categoría (peligroso, comestible, indumentaria)
Peso ( entre 100 y 800)
Tipo de material ( aluminio, hierro , madera)
Costo en $ (mayor a 0)
Pedir datos por prompt y mostrar por print, se debe informar:

Informe A- Cuál fue tipo de material más usado ( aluminio, hierro , madera)
Informe B- El porcentaje de contenedores de Categoría peligroso
Informe C- La marca y tipo del contenedor más pesado
Informe D- La marca del contenedor de comestible con menor costo
Informe E- El promedio de costo de todos los contenedores de HIerro

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        contador_aluminio = 0
        contador_hierro = 0
        contador_madera = 0

        contador_peligroso = 0
        contador_comestible = 0
        contador_indumentaria = 0

        acumulador_hierro = 0

        for i in range(20):
            marca = prompt("Puerto de Rosario","Ingrese la marca:")

            categoria = prompt("Puerto de Rosario","Ingrese la categoria:")
            while categoria != "peligroso" and categoria != "comestible" and categoria != "indumentaria":
                categoria = prompt("Puerto de Rosario","Reingrese la categoria:")

            peso = prompt("Puerto de Rosario","Ingrese el peso del contenedor:")
            while peso == None or peso == "" or not peso.isdigit() or int(peso) < 100 or int(peso) > 800:
                peso = prompt("Puerto de Rosario","Reingrese el peso del contenedor:")

            tipo_de_material = prompt("Puerto de Rosario","Ingrese el tipo de material:")
            while tipo_de_material != "aluminio" and tipo_de_material != "hierro" and tipo_de_material != "madera":
                tipo_de_material = prompt("Puerto de Rosario","reingrese el tipo de material:")

            costo = prompt("Puerto de Rosario","Ingrese el costo:")
            while costo == None or costo == "" or int(costo) < 0:
                costo = prompt("Puerto de Rosario","Reingrese el costo:")

            peso = int(peso)
            costo = int(costo)

            match tipo_de_material:
                case "aluminio":
                    contador_aluminio += 1
                case "hierro":
                    contador_hierro += 1
                    #Informe E- El promedio de costo de todos los contenedores de HIerro
                    acumulador_hierro += costo
                case "madera":
                    contador_madera += 1

            match categoria:
                case "peligroso":
                    contador_peligroso += 1
                case "comestible":
                    contador_comestible += 1
                    #Informe D- La marca del contenedor de comestible con menor costo
                    if contador_comestible == 1 or costo < minimo_costo:
                        minimo_costo = costo
                        minimo_marca = marca
                case "indumentaria":
                    contador_indumentaria += 1

            #Informe C- La marca y tipo del contenedor más pesado
            if i == 0 or peso > maximo_peso:
                maximo_peso = peso
                maximo_marca = marca
                maximo_tipo = tipo_de_material

        #Informe A- Cuál fue tipo de material más usado ( aluminio, hierro , madera)
        if contador_aluminio > contador_hierro and contador_aluminio > contador_madera:
            material_mas_usado = "Aluminio"
        elif contador_hierro > contador_madera:
            material_mas_usado = "Hierro"
        else:
            material_mas_usado = "Madera"

        #Informe B- El porcentaje de contenedores de Categoría peligroso
        porcentaje_peligroso = contador_peligroso * 100 / 20

        #Informe E- El promedio de costo de todos los contenedores de HIerro
        if contador_hierro > 0:
            promedio_costo_hierro = acumulador_hierro / contador_hierro
            mensaje = (f"El promedio de costo de los contenedores de Hierro es de: {promedio_costo_hierro}")
        else:
            mensaje = (f"No se ingresaron contenedores de Hierro")

        print(f"El material mas usado es: {material_mas_usado}")
        print(f"El porcentaje de contenedores peligrosos es: {porcentaje_peligroso}%")
        print(f"El contenedor mas pesado es de:\n\tMarca: {maximo_marca}\n\tTipo de material: {maximo_tipo}")
        if contador_comestible > 0:
            print(f"La marca del contenedor de comestible con menor costo es: {minimo_marca}")
        else:
            print(f"No se ingresaron contenedores de comestible")
        print(mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()