# ==================================================================================================================
# EJERCICIO 14: En una escuela la colegiatura de los alumnos se determina según el número de materias que cursan 
# (Solicitar al usuario). El costo de todas las materias es el mismo S/100. Se ha establecido un programa para 
# estimular a los alumnos, el cual consiste en lo siguiente: si el promedio obtenido por un alumno en el último 
# periodo es mayor o igual que 18, se le hará un descuento del 50% sobre la mitad de los cursos; si el promedio 
# obtenido es menor que 18 deberá pagar la colegiatura completa. Obtener cuanto debe pagar un alumno.
# ===================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
Numero_materias:int
Promedio:float

# --- ENTRADA ---
Numero_materias = int(input("Ingrese el numero de materias que cursas: "))
Promedio = float(input("Ingrese el promedio del ultimo periodo: "))

Costo_por_materia = 100

# --- PROCESO Y SALIDA ---
if Promedio>=18:
    Colegiatura_total = (Numero_materias /2) * Costo_por_materia
    print("El total a pagar de la colegiatura es: ",Colegiatura_total,"Soles")

else:
    Colegiatura_total = Numero_materias * Costo_por_materia
    print("El total a pagar de la colegiatura es: ",Colegiatura_total,"Soles")

