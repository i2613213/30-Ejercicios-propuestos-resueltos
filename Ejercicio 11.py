# ==================================================================================================================
# EJERCICIO 11: Calcular el total que una persona debe pagar en una llantera, si el precio de cada llanta es de S/150
# si se compran menos de 5 llantas y de S/120 si se compran 5 o más.
# ===================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
Precio_llanta:float
Total_pagar:float

# --- ENTRADA ---
Cantidad = float(input("Ingrese la cantidad de llantas a comprar: "))

# --- PROCESO ---
if Cantidad>=5:
    Total_pagar = 120 * Cantidad

else:
    Total_pagar = 150 * Cantidad

# --- SALIDA ---
print("El monto a pagar es de: ",Total_pagar,"Soles")


