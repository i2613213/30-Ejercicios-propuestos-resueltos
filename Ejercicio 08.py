# ==================================================================================================================
# EJERCICIO 8: Una empresa constructora vende terrenos con la forma A de la figura. Obtener el área respectiva de un 
# terreno de medidas ingresando el valor de los 3 lados.
# La figura es un trapecio restangulo:
#   A |‾‾‾‾ \
#     |_____ \
#     |        \ 
#   C |_________\
#         B
# ===================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
Área_total_del_terreno: float
Base:float
Altura_Mayor:float
Altura_Menor:float

# --- ENTRADA ---
Base = float(input("Ingrese la distancia de la base: "))
Altura_Mayor = float(input("Ingrese la alrura mayor: "))
Altura_Menor = float(input("Ingrese la altura menor: "))

# --- PROCESO ---
Área_del_terreno1 = Base * Altura_Menor
Área_del_terreno2 = (Base * (Altura_Mayor - Altura_Menor))/2
Área_total_del_terreno = Área_del_terreno1 + Área_del_terreno2

# --- SALIDA ---
print("El área del terreno es de: ",Área_total_del_terreno,"metros cuadrados")