import csv
import os

def contar_mayores_con_secundario(nombre_archivo):
    archivo_path = os.path.join("..", nombre_archivo)

    if not os.path.exists(archivo_path):
        print(f"⚠️ El archivo no fue encontrado en: {archivo_path}")
        return 0

    with open(archivo_path, encoding="utf-8") as archivo:
        reader = csv.reader(archivo, delimiter=';')
        encabezado = next(reader)

        idx_edad = encabezado.index('CH06')         # Edad
        idx_nivel = encabezado.index('CH12')        # Nivel más alto alcanzado
        idx_finalizo = encabezado.index('CH13')     # Si finalizó el nivel
        idx_ponderacion = encabezado.index('PONDERA')  # Ponderación

        total_ponderado = 0

        for row in reader:
            
                edad = int(row[idx_edad])
                nivel = int(row[idx_nivel])
                finalizo = int(row[idx_finalizo])
                ponderacion = float(row[idx_ponderacion])

                if edad >= 18 and nivel == 4 and finalizo == 1:
                    total_ponderado += ponderacion
            

        return total_ponderado
