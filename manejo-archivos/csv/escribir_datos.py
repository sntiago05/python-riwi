import csv

RUTA = "manejo-archivos/csv/datos.csv"


def agregar_una_fila(row: str):
    with open(RUTA, mode="a") as file:
        file.write(row + "\n")


def agregar_fila_csv(row: list):
    with open(RUTA, mode="a") as file:
        writer = csv.writer(file)
        writer.writerow(row)


def editar():
    filas = []
    with open(RUTA, "r") as file:
        next(file)
        for line in file:
            row = line.strip().split(",")
            if row[0].lower() == "Juan".lower():
                row[1] = "19"
            filas.append(row)

    with open(RUTA, "w") as file:
        file.write("nombre,edad,ciudad\n")
        for row2 in filas:
            file.write(",".join(row2) + "\n")


def editar_csv():
    with open(RUTA, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        print(rows)
        header = reader.fieldnames
        if header is None:
            header = ["nombre", "edad", "ciudad"]
        for row in rows:
            if row["nombre"].lower() == "juan":
                row["edad"] = 35  

    
    with open(RUTA, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        writer.writerows(rows)


#editar_csv()
# editar()
agregar_una_fila("Taliana ,18,Valledupar")
# agregar_fila_csv(["Mora", 32, "Barranquilla"])
