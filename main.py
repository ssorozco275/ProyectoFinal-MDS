cd ~/proyecto_mds
python3 sensor_temperatura_humedad.py




#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lectura de sensor de temperatura y humedad con GrovePi+
y almacenamiento en un archivo CSV.

Requisitos:
    - Raspberry Pi
    - GrovePi+ instalado y librería grovepi disponible
    - Sensor DHT (DHT11 o DHT22) conectado a un puerto digital (D2 por defecto)
"""

import time
import os
import csv
import math
import datetime

try:
    import grovepi
except ImportError:
    raise SystemExit(
        "ERROR: No se pudo importar 'grovepi'.\n"
        "Verifica que tengas instalado el GrovePi:\n"
        "  https://github.com/DexterInd/GrovePi\n"
    )

