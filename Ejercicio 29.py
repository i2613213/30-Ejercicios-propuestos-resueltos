# =====================================================================================================================
# EJERCICIO 29: Calcular el producto utilizando arrays: 100 x 98 x 96 x 94 x . . . x 1 en este orden.
# =====================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
numeros = []        
proceso = ""        
i = 100             

# ----- PROCESO ----
while i >= 2:
    numeros = numeros + [i]
    
    # Construir la cadena del proceso
    if i == 100:
        proceso = proceso + str(i)
    else:
        proceso = proceso + " x " + str(i)
    
    i -= 2  # Decrementar de 2 en 2 (pares descendentes)

# --- SALIDA ---
print("--- SECUENCIA DE MULTIPLICACIÓN ---")
print(f"Operación:")
print(f"{proceso}")
print(f"Array de números: {numeros}")


