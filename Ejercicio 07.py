# ==================================================================================================================
# EJERCICIO 7: Un estacionamiento requiere determinar el cobro que debe aplicar a las personas que lo utilizan. 
# Considere que el cobro es con base en las horas que lo disponen y que las fracciones de hora se toman como 
# completas y realice un programa que permita determinar el cobro. El pago por hora es de S/5.00 y el pago por los 
# minutos restantes de S/0.10 por minuto.
# ===================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
Horas_de_estacionamiento:float
Cobro_Total:float

# --- ENTRADA ---
Horas_de_estacionamiento = int(input("Ingrese el tiempo de horas de estacionamiento: "))
Minutos_de_estacionamiento = int(input("Ingrese los minutos restantes: "))

# --- PROCESO ---
Cobro_Horas = Horas_de_estacionamiento * 5
Cobro_Minutos = Minutos_de_estacionamiento * 0.10

Cobro_Total = Cobro_Horas + Cobro_Minutos

# --- SALIDA ---
print("El monto a pagar por el estacionamiento es de: ",Cobro_Total,"Soles")
