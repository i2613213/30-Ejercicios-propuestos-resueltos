# ==================================================================================================================
# EJERCICIO 2: Un estudiante realiza cuatro exámenes, los cuales tienen la misma ponderación. Calcular el promedio 
# de las calificaciones obtenidas.
# ===================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
Nota1:float
Nota2:float
Nota3:float
Nota4:float
Promedio:float

# --- ENTRADA ---
Nota1 = float(input("Ingrese la nota 1: "))
Nota2 = float(input("Ingrese la nota 2: "))
Nota3 = float(input("Ingrese la nota 3: "))
Nota4 = float(input("Ingrese la nota 4: "))

# --- PROCESO ---
Promedio = (Nota1 + Nota2 + Nota3 + Nota4)/4

# --- SALIDA ---
print("El promedio final es: ",round(Promedio,0))



