import os
import pandas as pd
from datos import guardar_csv, ingresar_ventas

# BASE DE DATOS (lista) para manjear los datos de ventas
VENTAS_DATA = []

if __name__ == "__main__":
    print("Sistema de Gestión de Ventas")
    print("----------------------------")
    ingresar_ventas(VENTAS_DATA)
