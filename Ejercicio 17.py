# ==================================================================================================================
# EJERCICIO 17: Calcular el pago de una llamada, el cobro es por el tiempo que ésta dura, de tal forma que los 
# primeros cinco minutos cuestan S/ 1.00 c/u, los siguientes tres, S/0.80 c/u, los siguientes dos minutos, S/0.70 c/u,
# y a partir del décimo minuto, S/0.50 c/u. Además, se carga un impuesto de 3 % cuando es domingo, y 5% si es domingo
# de turno nocturno. Realice un algoritmo para determinar cuánto debe pagar por cada concepto una persona que realiza 
# una llamada.
# ===================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
Tiempo_minutos: int
cobro: float

Impuesto_domingo = 0.003
Impuesto_domingo_nocturno = 0.005

# --- ENTRADA ---
Tiempo_minutos = int(input("Ingrese los minutos consumidos: "))
Es_domingo = input("Es domingo? S/N: ")
Es_nocturno = input("Es turno nocturno? S/N: ")

# ----- PROCESO Y SALIDA ----
if Tiempo_minutos<=5:
    Pago = Tiempo_minutos * 1
    if Es_domingo == "S" and Es_nocturno == "S":
         Impuesto = Pago * 0.05
    elif Es_domingo == "S" and Es_nocturno == "N":
        Impuesto = Pago * 0.03
    else:
        Impuesto = 0

    Cobro = Pago + Impuesto
    print("El cobro por la llamada es: ", Cobro)

if Tiempo_minutos<=8 and Tiempo_minutos>5:
    Pago = Tiempo_minutos * 0.8
    if Es_domingo =="S" and Es_nocturno == "S":
        Impuesto = Pago * 0.05
    elif Es_domingo == "S" and Es_nocturno == "N":
        Impuesto = Pago * 0.03
    else:
        Impuesto = 0

    Cobro = Pago + Impuesto
    print("El cobro por la llamda es: ",Cobro)

if Tiempo_minutos<=10 and Tiempo_minutos>8:
    Pago = Tiempo_minutos * 0.7
    if Es_domingo =="S" and Es_nocturno == "S":
        Impuesto = Pago * 0.05
    elif Es_domingo == "S" and Es_nocturno == "N":
        Impuesto = Pago * 0.03
    else:
        Impuesto = 0

    Cobro = Pago + Impuesto
    print("El cobro por la llamda es: ",Cobro)

if Tiempo_minutos>10:
    Pago = Tiempo_minutos * 0.5
    if Es_domingo =="S" and Es_nocturno == "S":
        Impuesto = Pago * 0.05
    elif Es_domingo == "S" and Es_nocturno == "N":
        Impuesto = Pago * 0.03
    else:
        Impuesto = 0

    Cobro = Pago + Impuesto
    print("El cobro por la llamda es: ",Cobro)
    




