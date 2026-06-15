# ==================================================================================================================
# EJERCICIO 4: Un vendedor recibe su sueldo base más 25% extra por comisión de sus ventas; el vendedor desea saber 
# cuánto dinero recibirá por concepto de comisiones por lastres ventas que realiza en el mes y el total que recibirá 
# en el mes tomando en cuenta sueldo base y comisiones.
# ===================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
Sueldo_base: float
Comisión: float 
Sueldo_total: float

# --- ENTRADA ---
Sueldo_base = float(input("Ingrese su sueldo base: "))

# --- PROCESO ---
Comisión = (Sueldo_base * 0.25)*3
Sueldo_total = Sueldo_base + Comisión

# --- SALIDA ---
print("Comisión a recibir por las 3 ventas es: ",Comisión, "Soles")
print("Sueldo total a recibir es: ",Sueldo_total,"Soles")