# =====================================================================================================================
# EJERCICIO 28: A una fiesta asistieron personas de diferentes edades y sexos. Construir un algoritmo donde se ingrese 
# los datos de los N asistentes. Calcular:
# • Cuantas personas asistieron a la fiesta
# • Cuantos hombres y cuantas mujeres
# • Promedio de edades por sexo
# • La edad de la persona de menor y mayor edad que asistió.
# Nota: El sistema debe permitir al menos el ingreso los datos de una persona y solicitar si se desasea registrar a otra.
# =====================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
asistentes = []       
total_asistentes = 0
hombres = 0
mujeres = 0
suma_edad_hombres = 0
suma_edad_mujeres = 0
promedio_edad_hombres = 0.0
promedio_edad_mujeres = 0.0
edad_mayor = 0
edad_menor = 0
nombre_mayor = ""
nombre_menor = ""
continuar = "s"         

# --- ENTRADA ---
print("REGISTRO DE ASISTENTES A LA FIESTA")

while continuar.lower() == "s":
    print(f"--- Asistente #{total_asistentes + 1} ---")
    
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    sexo = input("Sexo (M/F): ").upper()
    
    # Validar sexo
    while sexo not in ["M", "F"]:
        print("Error: Ingrese M para Masculino o F para Femenino")
        sexo = input("Sexo (M/F): ").upper()
    
    
    asistentes.append({
        "nombre": nombre,
        "edad": edad,
        "sexo": sexo
    })
    
    total_asistentes += 1
    
    continuar = input("¿Desea registrar otro asistente? (s/n): ")


# ----- PROCESO ----
# Inicializar mayor y menor con el primer asistente
if total_asistentes > 0:
    edad_mayor = asistentes[0]["edad"]
    edad_menor = asistentes[0]["edad"]
    nombre_mayor = asistentes[0]["nombre"]
    nombre_menor = asistentes[0]["nombre"]


for persona in asistentes:
    # Contar por sexo
    if persona["sexo"] == "M":
        hombres = hombres + 1
        suma_edad_hombres = suma_edad_hombres + persona["edad"]
    else:
        mujeres = mujeres + 1
        suma_edad_mujeres = suma_edad_mujeres + persona["edad"]
    
    # Mayor edad
    if persona["edad"] > edad_mayor:
        edad_mayor = persona["edad"]
        nombre_mayor = persona["nombre"]
    
    # Menor edad
    if persona["edad"] < edad_menor:
        edad_menor = persona["edad"]
        nombre_menor = persona["nombre"]

# Calcular promedios
if hombres > 0:
    promedio_edad_hombres = suma_edad_hombres / hombres
if mujeres > 0:
    promedio_edad_mujeres = suma_edad_mujeres / mujeres


# --- SALIDA ---
print("--- ESTADÍSTICAS DE LA FIESTA ---")
print(f"Total de personas que asistieron: {total_asistentes}")
print(f"Por sexo:")
print(f"   Hombres: {hombres}")
print(f"   Mujeres: {mujeres}")
print(f"Promedio de edades por sexo:")
if hombres > 0:
    print(f"   Hombres: {promedio_edad_hombres:.1f} años")
else:
    print(f"   Hombres: No hay registrados")
    
if mujeres > 0:
    print(f"   Mujeres: {promedio_edad_mujeres:.1f} años")
else:
    print(f"   Mujeres: No hay registradas")

print(f"Persona de MAYOR edad: {nombre_mayor} ({edad_mayor} años)")
print(f"Persona de MENOR edad: {nombre_menor} ({edad_menor} años)")

# Mostrar lista completa
print(f"Lista completa de asistentes:")

for i, persona in enumerate(asistentes, 1):
    sexo_texto = "Hombre" if persona["sexo"] == "M" else "Mujer"
    print(f"{i}. {persona['nombre']} - {persona['edad']} años - {sexo_texto}")


