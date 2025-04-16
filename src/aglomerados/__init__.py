import csv
import os

def contar_aglomerados(nombre_archivo):
    """
    Cuenta hogares de dos personas sin baño por aglomerado a partir de un archivo CSV.
    Devuelve un diccionario con clave = aglomerado y valor = cantidad de hogares.
    """
    archivo_path = os.path.join("..", nombre_archivo)

    if not os.path.exists(archivo_path):
        print(f"⚠️ El archivo no fue encontrado en: {archivo_path}")
        return {}

    conteo = {}

    with open(archivo_path, encoding="utf-8") as archivo:
        reader = csv.reader(archivo, delimiter=";")
        encabezado = next(reader)

        idx_aglomerado = encabezado.index("AGLOMERADO")
        idx_ii9 = encabezado.index("II9")
        idx_ix_tot = encabezado.index("IX_TOT")
        idx_pondera = encabezado.index("PONDERA")
      

        for row in reader:
            if row[idx_ii9] == '4' and row[idx_ix_tot] == '2':
                aglo = int(row[idx_aglomerado])
                pondera = float(row[idx_pondera])
                if aglo in conteo:
                    conteo[aglo] += pondera
                else:
                    conteo[aglo] = pondera

        print("📊 Aglomerados con hogares de 2 personas sin baño:")
        for aglo, cantidad in conteo.items():
            print(f"Aglomerado {aglo}: {cantidad} hogares")
            

    return conteo


def obtener_max_min(conteo):
    """
    Devuelve una tupla con (aglomerado_max, cantidad_max, aglomerado_min, cantidad_min)
    a partir del conteo de hogares por aglomerado.
    """
    if not conteo:
        return None, 0, None, 0

    max_aglo = max(conteo, key=conteo.get)
    min_aglo = min(conteo, key=conteo.get)
    return max_aglo, conteo[max_aglo], min_aglo, conteo[min_aglo]
