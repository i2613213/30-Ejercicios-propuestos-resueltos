# =====================================================================================================================
# EJERCICIO 30: Desarrolla un programa que para N (con un mínimo de 5 y máximo de 20) estudiantes permita leer sus notas
#  (calificación) obtenidas en un curso. Se debe validar que la nota tenga un valor entre 0 y 20. Se sabe que la mínima 
# nota aprobatoria es 13. Al final calcule:
# a) La mayor nota
# b) La menor nota
# c) La cantidad de alumnos que obtuvieron la mayor nota
# d) La cantidad de alumnos que obtuvieron la menor nota
# e) El promedio de notas del salón
# f) La cantidad de notas pares
# g) La cantidad de notas impares
# h) La cantidad de alumnos aprobados
# i) La cantidad de alumnos desaprobados
# j) El porcentaje de alumnos aprobados
# k) El porcentaje de alumnos desaprobados
# =====================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
MIN_ESTUDIANTES = 5
MAX_ESTUDIANTES = 20
NOTA_MINIMA = 0
NOTA_MAXIMA = 20
NOTA_APROBATORIA = 13

n = 0                          
notas = []                      
suma_notas = 0
mayor_nota = 0
menor_nota = 0
cantidad_mayor_nota = 0
cantidad_menor_nota = 0
cantidad_notas_pares = 0
cantidad_notas_impares = 0
aprobados = 0
desaprobados = 0
promedio_salon = 0.0
porcentaje_aprobados = 0.0
porcentaje_desaprobados = 0.0

# --- ENTRADA ---
print("SISTEMA DE CALIFICACIONES")

# Validar cantidad de estudiantes
while True:
    n = int(input(f"Ingrese cantidad de estudiantes ({MIN_ESTUDIANTES}-{MAX_ESTUDIANTES}): "))
    if MIN_ESTUDIANTES <= n <= MAX_ESTUDIANTES:
        break
    print(f"Error: Debe ser entre {MIN_ESTUDIANTES} y {MAX_ESTUDIANTES}")

# Ingresar y validar notas
print(f"--- Ingrese las {n} notas (0-20) ---")
for i in range(n):
    while True:
        nota = float(input(f"Nota del estudiante {i+1}: "))
        if NOTA_MINIMA <= nota <= NOTA_MAXIMA:
            notas.append(nota)
            break
        print(f"Error: La nota debe estar entre {NOTA_MINIMA} y {NOTA_MAXIMA}")


# ----- PROCESO ----
# Inicializar mayor y menor con la primera nota
mayor_nota = notas[0]
menor_nota = notas[0]

for nota in notas:
    # Suma para promedio
    suma_notas += nota
    
    # Mayor y menor nota
    if nota > mayor_nota:
        mayor_nota = nota
    if nota < menor_nota:
        menor_nota = nota
    
    # Pares e impares (parte entera)
    if int(nota) % 2 == 0:
        cantidad_notas_pares += 1
    else:
        cantidad_notas_impares += 1
    
    # Aprobados y desaprobados
    if nota >= NOTA_APROBATORIA:
        aprobados += 1
    else:
        desaprobados += 1

# Contar cuántos tienen la mayor y menor nota
for nota in notas:
    if nota == mayor_nota:
        cantidad_mayor_nota += 1
    if nota == menor_nota:
        cantidad_menor_nota += 1

# Cálculos finales
promedio_salon = suma_notas / n
porcentaje_aprobados = (aprobados / n) * 100
porcentaje_desaprobados = (desaprobados / n) * 100


# --- SALIDA ---
print("--- RESULTADOS ESTADÍSTICOS ---")
print(f"Notas ingresadas: {notas}")
print(f"    a) Mayor nota: {mayor_nota}")
print(f"    b) Menor nota: {menor_nota}")
print(f"    c) Cantidad con mayor nota ({mayor_nota}): {cantidad_mayor_nota}")
print(f"    d) Cantidad con menor nota ({menor_nota}): {cantidad_menor_nota}")
print(f"    e) Promedio del salón: {promedio_salon:.2f}")
print(f"    f) Cantidad de notas pares: {cantidad_notas_pares}")
print(f"    g) Cantidad de notas impares: {cantidad_notas_impares}")
print(f"    h) Alumnos aprobados (≥{NOTA_APROBATORIA}): {aprobados}")
print(f"    i) Alumnos desaprobados (<{NOTA_APROBATORIA}): {desaprobados}")
print(f"    j) Porcentaje de aprobados: {porcentaje_aprobados:.2f}%")
print(f"    k) Porcentaje de desaprobados: {porcentaje_desaprobados:.2f}%")

