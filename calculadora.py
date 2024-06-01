import math

def calcularareacirculo(radio):
    return math.pi * radio ** 2

def calculardiametrocirculo(radio):
    return 2 * radio

if __name == "__main":
    try:
        radio = float(input("Ingresa el radio del círculo: "))
        if radio <= 0:
            raise ValueError("El radio debe ser un número positivo")
        area = calcular_area_circulo(radio)
        diametro = calcular_diametro_circulo(radio)
        print(f"El área del círculo es: {area}")
        print(f"El diámetro del círculo es: {diametro}")
    except ValueError as e:
        print(e) 
