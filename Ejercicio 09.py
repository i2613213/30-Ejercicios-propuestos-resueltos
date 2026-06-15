# ==================================================================================================================
# EJERCICIO 9: Cuanto pagaría un cliente por una compra con descuento y cuanto sería el cambio que recibiría en un 
# pago en efectivo. Ingresar el monto base, el porcentaje de descuento y el con cuánto dinero está pagando el cliente.
# ===================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
Precio_del_producto:float
Descuento:float
Pago:float

# --- ENTRADA ---
Precio_del_producto = float(input("Ingrese el precio del producto: "))
Descuento = float(input("Ingrese el porcentaje de descuento del producto: "))

Monto_a_pagar = Precio_del_producto - (Precio_del_producto * (Descuento/100))

print("El precio total a pagar es de: ",Monto_a_pagar,"soles")


Dinero_recibido = float(input("¿Con cuanto dinero pagara?: "))

Cambio = Dinero_recibido - Monto_a_pagar
print("Su cambio es de: ",round(Cambio,2),"soles")
