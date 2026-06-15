# =====================================================================================================================
# EJERCICIO 24: De una lista de N números determinar simultáneamente el máximo y mínimo número.
# =====================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
n = 0
numeros = [] 
maximo = 0
minimo = 0

# --- ENTRADA ---
n = int(input("Ingrese la cantidad de números (N): "))

print(f"Ingrese los {n} números:")

# ----- PROCESO ----
for i in range(n):
    num = float(input(f"Número {i+1}: "))
    numeros = numeros + [num]


if n > 0:
    maximo = numeros[0]
    minimo = numeros[0]
    
    for num in numeros:
        if num > maximo:
            maximo = num
        if num < minimo:
            minimo = num

# --- SALIDA ---
print("--- RESULTADOS ---")
print("Lista de números ingresados: ",numeros)
print("Máximo número: ", maximo)
print("Mínimo número: ",minimo)
