# =====================================================================================================================
# EJERCICIO 25: Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si al final de cada mes 
# deposita cantidades variables de dinero; se quiere saber cuánto lleva ahorrado cada vez que haga un deposito en cada
# mes y luego mostrar el ahorro final de 12 meses.
# =====================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
meses = 12
depositos = []  
ahorro_acumulado = 0.0
ahorro_por_mes = []  

# --- ENTRADA ---
print("Ingrese la cantidad depositada al final de cada mes:")

# ----- PROCESO ----
for i in range(meses):
    deposito = float(input(f"Depósito del mes {i+1}: "))
    depositos = depositos + [deposito]


for i in range(meses):
    ahorro_acumulado = ahorro_acumulado +  depositos[i]
    ahorro_por_mes = ahorro_por_mes + [ahorro_acumulado]


# --- SALIDA ---
print("--- REGISTRO DE AHORRO MENSUAL ---")
print("-" * 45)
print(f"{'Mes':<10} {'Depósito':<15} {'Ahorro Acumulado':<20}")
print("-" * 45)
for i in range(meses):
    print(f"{i+1:<10} S/{depositos[i]:<14.2f} S/{ahorro_por_mes[i]:<19.2f}")
print("-" * 45)
print(f">>> AHORRO FINAL DESPUÉS DE 12 MESES: S/{ahorro_acumulado:.2f}")
