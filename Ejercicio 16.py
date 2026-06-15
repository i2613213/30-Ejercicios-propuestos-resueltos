# ==================================================================================================================
# EJERCICIO 16: Elabore un programa que lea la hora (HH MM SS) y muestre por pantalla la hora N segundos después.
# ===================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
Hora: int
Minutos:int
Segundos:int
Segundos_a_sumar: int

# --- ENTRADA ---
Hora = int(input("Ingrese la hora: "))
Minutos = int(input("Ingrese los minutos: "))
Segundos = int(input("Ingrese los segundos: "))
N = int(input("Ingrese los segundos a sumar: "))

# ----- PROCESO  ----
Total_segundos = (Hora * 3600) + (Minutos * 60) + Segundos 
Total_segundos = Total_segundos + N

total_segundos = Total_segundos % (24*3600)

Hora_final = total_segundos // 3600
Resto = total_segundos % 3600
Minutos_final = Resto // 60
Segundos_final = Resto % 60

# --- SALIDA ---
print("Hora despues de",(N),"segundos:",Hora_final,":",Minutos_final,":",Segundos_final)
