# ==================================================================================================================
# EJERCICIO 10: Se necesita saber la cantidad de dinero que un cajero automático debe proporcionar en diferentes 
# denominaciones, teniendo en cuenta que el usuario debe ingresar la cantidad a retirar y el cajero tiene disponible 
# las siguientes denominaciones de dinero: 200, 100, 50, 20, 10, 5, 1. Se debe buscar entregar la menor cantidad de 
# dinero por parte del cajero.
# ===================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
denominaciones = [200, 100, 50, 20, 10, 5, 1]

monto = int(input("Ingrese el monto a retirar: "))
resto = monto

# --- PROCESO Y SALIDA  ---
for billete in denominaciones:
    if resto >= billete:
        cantidad = resto // billete
        resto = resto % billete
        print("Billetes de S/.",billete,":",cantidad)
