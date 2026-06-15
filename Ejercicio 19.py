# ==================================================================================================================
# EJERCICIO 19: Permita calcular el total a pagar por la compra de N camisas. Si se compran entre 1 a 4 camisas se 
# aplica un descuento del 12.5%, si se compra una cantidad comprendida entre 5 y 8 camisas se aplica un descuento 
# del 20% y si se compran cantidades mayores, se aplica un descuento del 31.5% sobre el total de la compra. Debe 
# imprimirse en pantalla la compra final sin descuento, monto del descuento y la compra con descuento.
# ===================================================================================================================


# --- DECLARACIÓN DE VARIABLES ---
Numero_camisas: int
Precio_camisa: float
Total:float

# --- ENTRADA ---
Precio_camisa = float(input("Digite el precio de la camisa: "))
Numero_camisas = int(input("Digite el numero de camisas a llevar: "))

# ----- PROCESO Y SALIDA ----
if Numero_camisas<=4 and Numero_camisas>=1:
    Descuento = Precio_camisa * 0.125
    Total_pagar = Precio_camisa - Descuento
    print("La compra es de: ",Precio_camisa,"Soles")
    print("El monto del descuento es de: ", round(Descuento,1),"Soles")
    print("Total a pagar es de: ",round(Total_pagar,1),"Soles")
elif Numero_camisas>=5 and Numero_camisas<=8:
    Descuento = Precio_camisa * 0.2
    Total_pagar = Precio_camisa - Descuento
    print("La compra es de: ",Precio_camisa,"Soles")
    print("El monto del descuento es de: ",round(Descuento,1),"Soles")
    print("Total a pagar es de: ",round(Total_pagar,1),"Soles")
else:
    Descuento = Precio_camisa * 0.315
    Total_pagar = Precio_camisa - Descuento
    print("La compra es de: ",Precio_camisa,"Soles")
    print("El monto del descuento es de: ",round(Descuento,1),"Soles")
    print("Total a pagar es de: ",round(Total_pagar,1),"Soles")


