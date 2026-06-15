# ==================================================================================================================
# EJERCICIO 5: Suponga que un individuo desea invertir su capital en un banco y desea saber cuánto dinero ganará 
# después de un año si el banco paga a razón de 2% mensual.
# ===================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
Capital:float
Ganancia:float

# --- ENTRADA ---
Capital = float(input("Ingrese el monto a invertir: "))

# --- PROCESO ---
Ganancia = (Capital * 0.02) * 12

# --- SALIDA ---
print("La comisión a ganar por el periodo de 1 año es: ",Ganancia,"Soles")
