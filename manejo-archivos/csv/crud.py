import csv

PATH = "manejo-archivos/csv/datos_crud.csv"


def buscar_persona(nombre: str):
    with open(PATH, mode="r") as file:
        reader = csv.DictReader(file)
        for line in reader:
            if line["nombre"].lower() == nombre.lower():
                return line
        return None


def agregar_persona(nombre: str, edad: int, ciudad: str):
    fila = [nombre, edad, ciudad]
    with open(PATH, "a") as file:
        writer = csv.writer(file)
        writer.writerow(fila)


def editar_persona(nombre: str, edad=None, ciudad=None):
    with open(PATH, mode="r") as line:
        reader = csv.DictReader(line)
        header = reader.fieldnames
        rows = []
        for line in reader:
            if line["nombre"].lower() == nombre.lower():
                if edad != None:
                    line["edad"] = edad
                if ciudad != None:
                    line["ciudad"] = ciudad
            rows.append(line)

    with open(PATH, "w") as line:
        if header is None:
            header = ["nombre", "edad", "ciudad"]
        writer = csv.DictWriter(line, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)


def eliminar(nombre: str):
    with open(PATH) as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames
        rows = []
        for line in reader:
            if line["nombre"].lower() == nombre.lower():
                continue
            rows.append(line)

    with open(PATH, "w") as file:
        if header is None:
            header = ["nombre", "edad", "ciudad"]
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)
