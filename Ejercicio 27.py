# =====================================================================================================================
# EJERCICIO 27: Crea una aplicación que pida dos números y calcule su factorial de cada número, pero el programa también
# tiene que indicar hasta que valor serian. Ejemplo:
#     7! > 1x2x3x4x5x6x7
#     10! > 1x2x3x4x5x6x7x8x9x10
#     >> son iguales hasta el múltiplo 7
# =====================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
num1 = 0
num2 = 0
factorial1 = 1
factorial2 = 1
menor = 0
mayor = 0
multiplos_comunes = []  
proceso1 = ""  
proceso2 = ""  

# --- ENTRADA ---
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))


# ----- PROCESO ----
# Determinar menor y mayor
if num1 < num2:
    menor = num1
    mayor = num2
else:
    menor = num2
    mayor = num1

# Calcular factorial del primer número y construir proceso
for i in range(1, num1 + 1):
    factorial1 = factorial1 * i
    if i == 1:
        proceso1 = proceso1 + str(i)
    else:
        proceso1 = proceso1 + "x" + str(i)

# Calcular factorial del segundo número y construir proceso
for i in range(1, num2 + 1):
    factorial2 = factorial2 * i
    if i == 1:
        proceso2 = proceso2 + str(i)
    else:
        proceso2 = proceso2 + "x" + str(i)


for i in range(1, menor + 1):
    multiplos_comunes = multiplos_comunes + [i]


# --- SALIDA ---
print("--- RESULTADOS ---")

print(f"{num1}! = {proceso1}")
print(f"Resultado: {factorial1}")

print(f"{num2}! = {proceso2}")
print(f"Resultado: {factorial2}")

print(f">> Son iguales hasta el múltiplo {menor}")
print(f"Múltiplos comunes: ", end="")
for i in range(len(multiplos_comunes)):
    if i == len(multiplos_comunes) - 1:
        print(multiplos_comunes[i])
    else:
        print(multiplos_comunes[i], end=", ")