# ==================================================================================================================
# EJERCICIO 13: Para tributar un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos iguales o 
# superiores a S/3000 mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y 
# muestre por pantalla si el usuario tiene que tributar o no y mostrar el monto a tributar que siempre es el 5% del 
# ingreso mensual.
# ===================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
Edad:int
Ingreso_mensual:float
Monto_tributar:float

# --- ENTRADA ---
Edad = int(input("Digite su edad: "))
Ingreso_mensual = float(input("Digite su ingreso mensual: "))

# --- PROCESO Y SALIDA ---
if Edad>=18 and Ingreso_mensual>=3000:
    Monto_tributar = Ingreso_mensual * 0.05
    print("Usted tiene que tributar: ",Monto_tributar,"Soles")
else:
    Monto_tributar = 0
    print("Usted no tributa: ",Monto_tributar,"Soles")
