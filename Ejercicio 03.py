# ==================================================================================================================
# EJERCICIO 3: Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una 
# cantidad distinta. Obtener el porcentaje que cada uno invierte con respecto a la cantidad total invertida.
# ===================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
Socio1:float
Socio2:float
Socio3:float
Total_inversión:float

# --- ENTRADA ---
Socio1 = float(input("Ingrese el Monto del socio 1: "))
Socio2 = float(input("Ingrese el Monto del socio 2: "))
Socio3 = float(input("Ingrese el Monto del socio 3: "))

# --- PROCESO ---
Total_inversión = Socio1 +  Socio2 + Socio3 

# --- SALIDA ---
print("El porcentaje invertido del socio 1 es: ", round(((Socio1 / Total_inversión)*100),0), "%")
print("EL porcentaje invertido del socio 2 es: ", round(((Socio2 / Total_inversión)*100),0), "%")
print("EL porcentaje invertido del socio 3 es: ", round(((Socio3 / Total_inversión)*100),0), "%")