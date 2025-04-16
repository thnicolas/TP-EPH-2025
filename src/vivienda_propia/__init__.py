import csv
import os

def porcentaje_viviendas_propia(nombre_archivo):
    archivo_path = os.path.join("..", nombre_archivo)

    if not os.path.exists(archivo_path):
        print(f"⚠️ Archivo no encontrado en: {archivo_path}")
        return 0

    with open(archivo_path, encoding="utf-8") as archivo:
        reader = csv.reader(archivo, delimiter=';')
        encabezado = next(reader)

        idx_tenencia = encabezado.index('II7')       # Régimen de tenencia
        idx_pondera = encabezado.index('PONDERA')    # Ponderación del hogar

        total_ponderado = 0
        propietarios_ponderado = 0

        for row in reader:
        
                tenencia = row[idx_tenencia]
                ponderacion = float(row[idx_pondera])
                total_ponderado += ponderacion

                if tenencia == '1' :
                    propietarios_ponderado += ponderacion
            

        if total_ponderado == '0':
            return 0

        porcentaje = (propietarios_ponderado / total_ponderado) * 100
        
        return porcentaje 
