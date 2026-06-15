# ==================================================================================================================
# EJERCICIO 12: Cómo se podría determinar ¿Cuál de los 3 números brindados por usuario es el menor y mayor de todos ellos?
# ===================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
Numero1:float
Numero2:float
Numero3:float

# --- ENTRADA ---
Numero1 = float(input("Ingrese el primer numero: "))
Numero2 = float(input("Ingrese el segundo numero: "))
Numero3 = float(input("Ingrese el tercer numero>: "))

# --- PROCESO ---
if Numero1>=Numero2 and Numero1>=Numero3:
    Numero_mayor = Numero1

elif Numero2>=1 and Numero2>=Numero3:
    Numero_mayor = Numero2
else:
    Numero_mayor = Numero3

if Numero1<=Numero2 and Numero1<=Numero3:
    Numero_menor = Numero1
elif Numero2<=Numero1 and Numero2<=Numero3:
    Numero_menor = Numero2
else:
    Numero_menor = Numero3

# --- SALIDA ---
print("El numero mayor es: ", Numero_mayor)
print("El numero menor es: ", Numero_menor)




