# ==================================================================================================================
# EJERCICIO 18: Solicite a usuario 3 números enteros (validar que sean diferentes) y en que orden lo desean ver, para
#  luego, mostrarlos a usuario, pero ordenados de manera ascendente o descendente según los que indique el usuario.
# ===================================================================================================================


# --- DECLARACIÓN DE VARIABLES ---
Numeros: int

# --- ENTRADA ---
Numero1 = int(input("Ingrese el primer numero: "))
Numero2 = int(input("Ingrese el segundo numero diferente al primero: "))
Numero3 = int(input("Ingrese el tercer numero diferente al segundo: "))
Orden = input("En que orden lo deseas ver A/D: ")

Numeros = [Numero1, Numero2, Numero3]

# ----- PROCESO Y SALIDA ----
if Orden == "A":
    Resultado = Numeros.sort()
    print("Numeros en orden ascendente: ", Numeros)

elif Orden == "D":
    Resultado = Numeros.sort(reverse=True)
    print("Numeros en orden Descendente: ", Numeros)

else:
    print("Opcion no valida. Debe de ser A o D")




