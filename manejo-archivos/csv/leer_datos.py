import csv

RUTA = "manejo-archivos/csv/datos.csv"


# mostrar
def leer_lineas():
    with open(RUTA) as file:
        for line in file:
            print(line)


# leer con csv
def leer_con_csv():
    with open(RUTA, encoding="utf-8") as file:
        lector = csv.reader(file)
        for fila in lector:
            print(fila)


# por columnas
def por_columnas():
    with open(RUTA) as file:
        for line in file:
            row = line.strip().split(",")
            print(row)


# ignorar encabezado
def ignorar_encabezado():
    with open(RUTA) as file:
        next(file)
        for line in file:
            print(line)


# saltar encabezado con csv
def ignorar_encabezado_csv():
    with open(RUTA, encoding="utf-8") as file:
        lector = csv.reader(file)
        next(lector)
        for fila in lector:
            print(fila)


def imprimir_mensaje(name_search: str):
    with open(RUTA) as file:
        next(file)
        for line in file:
            row = line.strip().split(",")
            if len(row) != 3:
                continue
            name, age, city = row
            if name.lower() == name_search.lower():
                print(f"{name} tiene {age} años y vive en {city}")
                break
        else:
            print("No se encontró a la persona")


def imprimir_mensaje_csv(name_search: str):
    with open(RUTA) as file:
        reader = csv.DictReader(file)
        for line in reader:
            if line["nombre"].lower() == name_search.lower():
                return line

        return None


# leer_lineas()
# por_columnas()
# ignorar_encabezado()
# imprimir_mensaje("juan")

persona = imprimir_mensaje_csv("sofia")
if persona:
    print(
        f"{persona['nombre']} tiene {persona['edad']} años y vive en {persona['ciudad']}"
    )
else:
    print("Persona no encontrada")
