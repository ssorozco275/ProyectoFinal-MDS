import grovepi
import math
import time
import mysql.connector # Librería para hablar con MariaDB

# --- CONFIGURACIÓN ---
puerto_sensor = 4
tipo_sensor = 0 # 0=Blue, 1=White

print("--- Iniciando Sistema MDS: Sensor -> Base de Datos ---")

# --- CONEXIÓN A BASE DE DATOS (El cambio importante) ---
try:
    db = mysql.connector.connect(
        host="localhost",       # La BD está en la misma Raspberry
        user="santi",      # Usuario que creamos en SQL
        password="1234567890",    # La contraseña que definimos
        database="ProyectoMDS"  # Nombre de la BD
    )
    cursor = db.cursor()
    print("Conexión a Base de Datos: EXITOSA")
except Exception as e:
    print("Error conectando a la BD:", e)
    exit() # Si no hay BD, cerramos el programa

# --- BUCLE PRINCIPAL ---
while True:
    try:
        [temp, hum] = grovepi.dht(puerto_sensor, tipo_sensor)

        if math.isnan(temp) == False and math.isnan(hum) == False:
            # 1. Mostrar en pantalla (Feedback visual)
            print("Guardando -> Temp: {:.2f} C | Hum: {:.2f} %".format(temp, hum))
            
            # 2. Insertar en Base de Datos (SQL)
            sql = "INSERT INTO Lecturas (temperatura, humedad, sensor_id) VALUES (%s, %s, %s)"
            val = (temp, hum, "Raspi_Lab1")
            
            cursor.execute(sql, val)
            db.commit() # ¡IMPORTANTE! Esto guarda los cambios permanentemente
            
        else:
            print("Error: Lectura NaN")

        time.sleep(5) # Guardamos cada 5 segundos para no llenar la BD tan rápido

    except IOError:
        print("Error de Hardware")
    except KeyboardInterrupt:
        print("\nCerrando conexión y saliendo...")
        db.close() # Buena práctica: cerrar la conexión al salir
        break
