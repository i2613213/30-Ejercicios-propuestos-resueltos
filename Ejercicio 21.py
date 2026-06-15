# =====================================================================================================================
# EJERCICIO 21: Calcular la suma y promedio de los números pares e impares por separado ,de 1 hasta N.
# =====================================================================================================================


# --- DECLARACIÓN DE VARIABLES ---
n = 0
suma_pares = 0
suma_impares = 0
contador_pares = 0
contador_impares = 0
promedio_pares = 0
promedio_impares = 0

# --- ENTRADA ---
n = int(input("Ingrese el valor de N: "))

# ----- PROCESO ----
for i in range(1, n + 1):
    if i % 2 == 0:
        suma_pares = suma_pares + i
        contador_pares = contador_pares + 1
    else:
        suma_impares = suma_impares + i
        contador_impares = contador_impares + 1

if contador_pares > 0:
    promedio_pares = suma_pares / contador_pares
if contador_impares > 0:
    promedio_impares = suma_impares / contador_impares

# --- SALIDA ---
print("\n--- RESULTADOS ---")
print("Suma de números pares: ", suma_pares)
print("Cantidad de pares: ", contador_pares)
print("Promedio de pares: ", round(promedio_pares,1))
print("Suma de números impares: ", suma_impares)
print("Cantidad de impares: ", contador_impares)
print("Promedio de impares: ", round(promedio_impares,1))
