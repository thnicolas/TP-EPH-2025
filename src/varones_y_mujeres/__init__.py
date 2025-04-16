import csv
import os

def contar_sexo_ponderado(nombre_archivo):
    # Construir la ruta completa desde donde se ejecuta el notebook (carpeta notebook/)
    archivo_path = os.path.join("..", nombre_archivo)

    # Validar si el archivo existe
    if not os.path.exists(archivo_path):
        print(f"⚠️ El archivo no fue encontrado en: {archivo_path}")
        return 0, 0

    # Leer el archivo y procesar
    with open(archivo_path, encoding="utf-8") as archivo:
        reader = csv.reader(archivo, delimiter=';')
        encabezado = next(reader)

        idx_ch04 = encabezado.index('CH04')      # Sexo
        idx_pondih = encabezado.index('PONDERA')  # Ponderación

        total_varones = 0
        total_mujeres = 0

        for row in reader:
            sexo = row[idx_ch04]
            ponderacion = float(row[idx_pondih])  # Convertir a float para sumar correctamente

            if sexo == '1':
                total_varones += ponderacion
            elif sexo == '2':
                total_mujeres += ponderacion

        return total_varones, total_mujeres
