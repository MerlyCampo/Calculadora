import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from calculadora import *

import os
import math

#creo el objeto CalculadoraGeometrica
calculadoraGeo=CalculadoraGeometrica()

# Obtenemos la ruta absoluta del archivo actual usando la variable especial __file__
ruta_absoluta = os.path.abspath(__file__)
# Obtenemos el directorio actual usando la función os.path.dirname
directorio_actual = os.path.dirname(ruta_absoluta)

#Desarrollo la interfaz para la calculadora
#Se crean las pestañas de la interfaz, una para el calculo del área y otra para la ecuación
class InterfazCalculadora:
   def __init__(self, root):
        self.root = root
        self.root.title("Calculadora Geométrica")
        self.root.geometry("300x300")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        self.pestana_area = ttk.Frame(self.notebook)
        self.pestana_ecuacion = ttk.Frame(self.notebook)

        self.notebook.add(self.pestana_area, text='Área')
        self.notebook.add(self.pestana_ecuacion, text='Ecuación')

        self.crear_pestana_area()
        self.crear_pestana_ecuacion()
        
        self.imagen_label = ttk.Label(self.pestana_area)
        self.imagen_label.grid(row=4, columnspan=2)

#Creo lista desplegable para seleccionar la figura a la cual le vamos a calcular el área
   def crear_pestana_area(self):
        ttk.Label(self.pestana_area, text="Seleccione una figura:").grid(row=0, column=0)
        
        self.figura_var = tk.StringVar()
        figuras = ["Triángulo Equilátero", "Cuadrado", "Rectángulo", "Círculo", "Triángulo Rectángulo"]
        self.figura_combo = ttk.Combobox(self.pestana_area, textvariable=self.figura_var, values=figuras)
        self.figura_combo.grid(row=0, column=1)
        self.figura_combo.bind("<<ComboboxSelected>>", self.mostrar_campos)
        
        self.datos_frame = ttk.Frame(self.pestana_area)
        self.datos_frame.grid(row=1, columnspan=2)

        self.resultado_label = ttk.Label(self.pestana_area, text="")
        self.resultado_label.grid(row=3, columnspan=2)

        ttk.Button(self.pestana_area, text="Calcular", command=self.calcular_area).grid(row=2, columnspan=2)

#Se define lo que se desea mostrar en la pestaña de área.
   def mostrar_campos(self, event):
        for widget in self.datos_frame.winfo_children():
            widget.destroy()

        figura = self.figura_var.get()
        if figura == "Triángulo Equilátero":
            ttk.Label(self.datos_frame, text="Lado:").grid(row=0, column=0)
            self.lado_entry = ttk.Entry(self.datos_frame)
            self.lado_entry.grid(row=0, column=1)
            self.mostrar_imagen('triangulo.png')
        elif figura == "Cuadrado":
            ttk.Label(self.datos_frame, text="Lado:").grid(row=0, column=0)
            self.lado_entry = ttk.Entry(self.datos_frame)
            self.lado_entry.grid(row=0, column=1)
            self.mostrar_imagen('cuadrado.png')
        elif figura == "Rectángulo":
            ttk.Label(self.datos_frame, text="Base:").grid(row=0, column=0)
            self.base_entry = ttk.Entry(self.datos_frame)
            self.base_entry.grid(row=0, column=1)
            ttk.Label(self.datos_frame, text="Altura:").grid(row=1, column=0)
            self.altura_entry = ttk.Entry(self.datos_frame)
            self.altura_entry.grid(row=1, column=1)
            self.mostrar_imagen('Rectangulo.png')
        elif figura == "Círculo":
            ttk.Label(self.datos_frame, text="Radio:").grid(row=0, column=0)
            self.radio_entry = ttk.Entry(self.datos_frame)
            self.radio_entry.grid(row=0, column=1)
            self.mostrar_imagen('circulo.png')
        elif figura == "Triángulo Rectángulo":
            ttk.Label(self.datos_frame, text="Cateto 1:").grid(row=0, column=0)
            self.cateto1_entry = ttk.Entry(self.datos_frame)
            self.cateto1_entry.grid(row=0, column=1)
            ttk.Label(self.datos_frame, text="Cateto 2:").grid(row=1, column=0)
            self.cateto2_entry = ttk.Entry(self.datos_frame)
            self.cateto2_entry.grid(row=1, column=1)
            self.mostrar_imagen('trianguloRec.png')

#Con la ayuda de Pillow mostramos las imagenes en la interfaz           
   def mostrar_imagen(self, nombre_archivo):
        try:
            if not os.path.isfile(nombre_archivo):
                raise FileNotFoundError(f"No se encontró la imagen: {nombre_archivo}")
            
            # Cargar la imagen usando PIL
            img = Image.open(nombre_archivo)
            self.imagen = ImageTk.PhotoImage(img)
            self.imagen_label.config(image=self.imagen)
        
        except Exception as e:
            self.imagen_label.config(text="Imagen no disponible")
            print(e)  # Imprime el error en la consola para depuració
   
#Se crea la función para realizar el calculo del area en la interfaz    
   def calcular_area(self):
        figura = self.figura_var.get()
        try:
            if figura == "Triángulo Equilátero":
                lado = float(self.lado_entry.get())
                area = CalculadoraGeometrica.calcular_area(figura, lado=lado)
                self.resultado_label.config(text=f"Área: {area:.2f}")
            elif figura == "Cuadrado":
                lado = float(self.lado_entry.get())
                area = CalculadoraGeometrica.calcular_area(figura, lado=lado)
                self.resultado_label.config(text=f"Área: {area:.2f}")
            elif figura == "Rectángulo":
                base = float(self.base_entry.get())
                altura = float(self.altura_entry.get())
                area = CalculadoraGeometrica.calcular_area(figura, base=base, altura=altura)
                self.resultado_label.config(text=f"Área: {area:.2f}")
            elif figura == "Círculo":
                radio = float(self.radio_entry.get())
                area = CalculadoraGeometrica.calcular_area(figura, radio=radio)
                self.resultado_label.config(text=f"Área: {area:.2f}")
            elif figura == "Triángulo Rectángulo":
                cateto1 = float(self.cateto1_entry.get())
                cateto2 = float(self.cateto2_entry.get())
                hipotenusa = CalculadoraGeometrica.calcular_area(figura, cateto1=cateto1, cateto2=cateto2)
                self.resultado_label.config(text=f"Hipotenusa: {hipotenusa:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un valor válido.")

#Se crea todo lo de la pestaña de ecuación
   def crear_pestana_ecuacion(self):
        ttk.Label(self.pestana_ecuacion, text="Ecuación Ax + B = C").grid(row=0, column=0)
        ttk.Label(self.pestana_ecuacion, text="A:").grid(row=1, column=0)
        self.a_entry = ttk.Entry(self.pestana_ecuacion)
        self.a_entry.grid(row=1, column=1)
        
        ttk.Label(self.pestana_ecuacion, text="B:").grid(row=2, column=0)
        self.b_entry = ttk.Entry(self.pestana_ecuacion)
        self.b_entry.grid(row=2, column=1)

        ttk.Label(self.pestana_ecuacion, text="C:").grid(row=3, column=0)
        self.c_entry = ttk.Entry(self.pestana_ecuacion)
        self.c_entry.grid(row=3, column=1)

        ttk.Button(self.pestana_ecuacion, text="Resolver", command=self.resolver_ecuacion).grid(row=4, column=0, columnspan=2)
        self.resultado_ecuacion_label = ttk.Label(self.pestana_ecuacion, text="")
        self.resultado_ecuacion_label.grid(row=5, columnspan=2)

#Se realiza el calculo de la ecuación
   def resolver_ecuacion(self):
        try:
            a = float(self.a_entry.get())
            b = float(self.b_entry.get())
            c = float(self.c_entry.get())
            resultado = CalculadoraGeometrica.resolver_ecuacion(a, b, c)
            self.resultado_ecuacion_label.config(text=f"Resultado: x = {resultado:.2f}")
            
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazCalculadora(root)
    root.mainloop()
