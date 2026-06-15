# ==================================================================================================================
# EJERCICIO 15: Determinar mediante el ingreso de los 3 lados de un triángulo, si este es Equilátero (Mostrar el 
# perímetro del), Isósceles (Indicar que lados son Iguales) o Escaleno (triángulo mostrar el área del triángulo).
# ===================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
Lados_triangulo:float
Triangulo_equilatero: str
Triangulo_isosceles:str
Triangulo_escaleno:str

# --- ENTRADA ---
Lado1 = float(input("Ingrese el primer lado del triangulo: "))
Lado2 = float(input("Ingrese el segundo lado del triangulo: "))
Lado3 = float(input("Ingrese el tercer lado del triangulo: "))

# --- PROCESO Y SALIDA ---
if Lado1 == Lado2 and Lado2 == Lado3:
    print("El triangulo es equilatero: ")
    print("El perimetro es: ",(Lado1 + Lado2 + Lado3))

elif Lado1 == Lado2 and Lado2 != Lado3:
    print("El triangulo es Isosceles")
    print("Lados iguales: ","Lado 1 y Lado 2")
else:
    print("El triangulo es Escaleno")
    S = (Lado1 + Lado2 + Lado3)/2
    Area_triangulo = (S * (S - Lado1)*(S-Lado2)*(S-Lado3))**0.5

    print("El area del triangulo es: ",Area_triangulo)

