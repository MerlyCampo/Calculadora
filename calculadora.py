import math

class CalculadoraGeometrica:
    @staticmethod
    def area_triangulo_equilatero(lado):
        return (math.sqrt(3) / 4) * (lado ** 2)

    @staticmethod
    def area_cuadrado(lado):
        return lado ** 2

    @staticmethod
    def area_rectangulo(base, altura):
        return base * altura

    @staticmethod
    def area_circulo(radio):
        return math.pi * (radio ** 2)

    @staticmethod
    def hipotenusa(cateto1, cateto2):
        return math.sqrt(cateto1 ** 2 + cateto2 ** 2)

    @staticmethod
    def resolver_ecuacion(a, b, c):
        if a == 0:
            raise ValueError("El coeficiente A no puede ser cero.")
        return (c - b) / a

    @staticmethod
    def calcular_area(figura, **kwargs):
        if figura == "Triángulo Equilátero":
            return CalculadoraGeometrica.area_triangulo_equilatero(kwargs['lado'])
        elif figura == "Cuadrado":
            return CalculadoraGeometrica.area_cuadrado(kwargs['lado'])
        elif figura == "Rectángulo":
            return CalculadoraGeometrica.area_rectangulo(kwargs['base'], kwargs['altura'])
        elif figura == "Círculo":
            return CalculadoraGeometrica.area_circulo(kwargs['radio'])
        elif figura == "Triángulo Rectángulo":
            return CalculadoraGeometrica.hipotenusa(kwargs['cateto1'], kwargs['cateto2'])
        else:
            raise ValueError("Figura no válida.")
