# ==================================================================================================================
# EJERCICIO 1: etermina la velocidad final de un auto si su velocidad inicial es 0 km/h y su aceleración es 0.8 m/s2; 
# y el tiempo transcurrido es de 30 segundos.
# ===================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
velocidad_final:float
velocidad_inicial:float
tiempo:float
aceleración:float

# --- ENTRADA ---
velocidad_inicial = float(input("Ingrese la velocidad inicial: "))
tiempo = float(input("Ingrese el tiempo: "))
aceleración = float(input("Ingrese la aceleración: "))

# --- PROCESO ---
velocidad_final = ((((velocidad_inicial * 100)/6) + (aceleración * tiempo))*6)/100

# --- SALIDA ---
print("La velocidad final es: ", velocidad_final, "km/h")