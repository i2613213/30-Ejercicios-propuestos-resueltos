# =====================================================================================================================
# EJERCICIO 26: Hacer un programa que muestre un cronometro (hh:mm:ss), indicando las horas, minutos y segundos(Considerar
#  que el tiempo no será exacto al de un cronometro real solo será referencial).
# =====================================================================================================================

# --- DECLARACIÓN DE VARIABLES ---
import time

horas = 0
minutos = 0
segundos = 0
duracion = 0  

# --- ENTRADA ---
print("CRONÓMETRO REFERENCIAL")
print("Presione Ctrl+C para detener")
duracion = int(input("¿Hasta cuantos segundos cuento? Pon 0 si no quieres limite: "))

# ----- PROCESO ----
print("--- INICIANDO CRONÓMETRO ---")
try:
    contador = 0
    while True:
        
        print(f"\r{horas:02d}:{minutos:02d}:{segundos:02d}", end="", flush=True)
        
        time.sleep(1) 
        segundos = segundos + 1
        
        if segundos == 60:
            segundos = 0
            minutos = minutos + 1
        if minutos == 60:
            minutos = 0
            horas = horas + 1
        
        contador = contador + 1
        if duracion > 0 and contador >= duracion:
            break
            
except KeyboardInterrupt:
    pass

# --- SALIDA ---
print(f"--- CRONÓMETRO DETENIDO ---")
print(f"Tiempo transcurrido: {horas:02d}:{minutos:02d}:{segundos:02d}")
print(f"Total en segundos: {horas*3600 + minutos*60 + segundos}")
