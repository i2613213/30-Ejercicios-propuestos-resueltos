# =====================================================================================================================
# EJERCICIO 22: Realizar un algoritmo que permita pedir 10 números y determine e imprima cuantos son pares, impares, 
# positivos, neutros y negativos.
# =====================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
numeros = [] 
pares = 0
impares = 0
positivos = 0
neutros = 0
negativos = 0

# --- ENTRADA ---
print("Ingrese 10 números:")


# ----- PROCESO ----
for i in range(10):
    num = float(input(f"Número {i+1}: "))
    numeros = numeros + [num]

for num in numeros:
    
    if int(num) % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    
    if num > 0:
        positivos = positivos + 1
    elif num < 0:
        negativos = negativos + 1
    else:
        neutros = neutros + 1

# --- SALIDA ---
print("--- RESULTADOS ---")
print("Cantidad de pares: ", pares)
print("Cantidad de impares: ", impares)
print("Cantidad de positivos: ", positivos)
print("Cantidad de neutros (cero): ", neutros)
print("Cantidad de negativos: ", negativos)
