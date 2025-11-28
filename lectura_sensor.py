import grovepi
import math
import time

# --- CONFIGURACIÓN ---
puerto_sensor = 4
# 0 = DHT11 (Azul), 1 = DHT22 (Blanco)
tipo_sensor = 0 

print("--- Iniciando Sistema de Monitoreo Ambiental (MDS) ---")
# Sintaxis compatible con versiones anteriores de Python
print("Leyendo sensor en puerto D" + str(puerto_sensor) + "...")

while True:
    try:
        [temp, hum] = grovepi.dht(puerto_sensor, tipo_sensor)

        if math.isnan(temp) == False and math.isnan(hum) == False:
            # Usamos .format() que es compatible con Python 3.0+
            print("Temperatura: {:.2f} C  |  Humedad: {:.2f} %".format(temp, hum))
        else:
            print("Error: Lectura inestable (NaN detectado)")

        time.sleep(2)

    except IOError:
        print("Error de Entrada/Salida (Bus I2C)")
    except KeyboardInterrupt:
        print("\nMonitoreo detenido por el usuario.")
        break
