# =====================================================================================================================
# EJERCICIO 23: Hacer un programa que permita ingresar un conjunto de N números y un numero más X mostrar como resultado:
# • Porcentaje de números menores que X.
# • Porcentaje de números mayores de X.
# • Porcentaje de números iguales de X.
# • Porcentaje de números comprendidos entre 1 y X.
# • Porcentaje de números que no cumple ninguna condición.
# =====================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
n = 0
x = 0.0
numeros = [] 
menores_x = 0
mayores_x = 0
iguales_x = 0
entre_1_y_x = 0
ninguna_condicion = 0
porc_menores = 0.0
porc_mayores = 0.0
porc_iguales = 0.0
porc_entre = 0.0
porc_ninguna = 0.0


# --- ENTRADA ---
n = int(input("Ingrese la cantidad de números (N): "))
x = float(input("Ingrese el número X de referencia: "))

print(f"Ingrese los {n} números:")

# ----- PROCESO ----
for i in range(n):
    num = float(input(f"Número {i+1}: "))
    numeros = numeros + [num]


for num in numeros:
    cumple_alguna = False
    
    if num < x:
        menores_x = menores_x + 1
        cumple_alguna = True
    if num > x:
        mayores_x += 1
        cumple_alguna = True
    if num == x:
        iguales_x = iguales_x + 1
        cumple_alguna = True
    if 1 <= num <= x:
        entre_1_y_x = entre_1_y_x + 1
        cumple_alguna = True
    
    if not cumple_alguna:
        ninguna_condicion = ninguna_condicion + 1

if n > 0:
    porc_menores = (menores_x / n) * 100
    porc_mayores = (mayores_x / n) * 100
    porc_iguales = (iguales_x / n) * 100
    porc_entre = (entre_1_y_x / n) * 100
    porc_ninguna = (ninguna_condicion / n) * 100

# --- SALIDA ---
print("--- RESULTADOS (PORCENTAJES) ---")
print("Menores que X: ", round(porc_menores,2),"%")
print("Mayores que X: ", round(porc_mayores,2),"%")
print("Iguales a X: ",round(porc_mayores,2),"%")
print("Comprendidos entre 1 y X: ", round(porc_entre,2),"%")
print("No cumplen ninguna condición: ",round(porc_ninguna,2),"%")
