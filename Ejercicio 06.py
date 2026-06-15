# ==================================================================================================================
# EJERCICIO 6: SRealice un programa que representen el algoritmo donde se ingrese la edad de un apersona para 
# determinar aproximadamente cuántos meses, semanas, días y horas ha vivido una persona.
# ===================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
Edad: int
Meses: int
Semanas:int
Dias: int
Horas: int

# --- ENTRADA ---
Edad = int(input("Ingrese su edad: "))

# --- PROCESO ---
Meses = Edad * 12
Semanas = Edad * 52
Dias = Edad * 365
Horas = Edad * 8760

# --- SALIDA ---
print("El tiempo vivido es de: ",Meses,"Meses",",",Semanas,"Semanas",",",Dias,"Dias","y",Horas,"Horas")

