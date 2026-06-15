# ==================================================================================================================
# EJERCICIO 20: El costo de llamadas telefónicas internacionales depende de clave (identifica a la zona geográfica) 
# en la que se encuentra el destino y del número de minutos hablados. En la siguiente tabla se presenta el costo del
# minuto por zona. A cada zona se le ha asociado una clave. Construya un diagrama de flujo que permita mostrar en 
# nombre del área y calcular e imprimir el costo total de una llamada y el nombre de la zona a la cual llamó.
# 
# ============================================================
#  CODIGO | ZONA GEOGRAFICA    | COSTO X MINUTO (S/) 
# ============================================================
#      10 | América del norte  | 2.2 
#      12 | América del centro | 2.5 
#      20 | América del sur    | 1.2 
#      22 | Asia               | 3.5 
#      30 | Europa             | 3.0 
#      32 | África             | 3.2 
# ===================================================================================================================


# --- DECLARACIÓN DE VARIABLES ---
codigo: int
zona_geografica: str
costo_po_minuto: float

# --- ENTRADA ---
print("=== COSTO LLAMADA INTERNACIONAL ===")

codigo = int(input("Ingresa el código de zona: "))
minutos = int(input("Ingresa los minutos hablados: "))

# ----- PROCESO ----
if codigo == 10:
    zona = "América del norte"
    costo_minuto = 2.2
elif codigo == 12:
    zona = "América del centro"
    costo_minuto = 2.5
elif codigo == 20:
    zona = "América del sur"
    costo_minuto = 1.2
elif codigo == 22:
    zona = "Asia"
    costo_minuto = 3.5
elif codigo == 30:
    zona = "Europa"
    costo_minuto = 3.0
elif codigo == 32:
    zona = "África"
    costo_minuto = 3.2
else:
    zona = None
    costo_minuto = 0
    print("Error: Código de zona no válido")


# --- SALIDA ---
if zona!= None:
    costo_total = minutos * costo_minuto
    print("Zona geográfica: ",zona)
    print("Costo por minuto: ","S/",round(costo_minuto,2))
    print("Minutos hablados: ",minutos)
    print("COSTO TOTAL: ","S/",round(costo_total,2))
    