"""
diccionario = {"5": 10, "7": 12, "9": 21, "20": 0}
inverted = dict()

for k,v in diccionario.items():
    inverted[v] = k

print(inverted)"""

"""
# {"hola": 2, "mundo": 1, "python": 1}
lista = input("Ingresa la frase: ").split(" ")
lista_sin_repetidos = list(dict.fromkeys(lista))
dic = dict()
for palabra in lista_sin_repetidos:
    dic[palabra] = lista.count(palabra)

print(dic)"""

"""
frase = input("Ingresa la frase: ").split()

dic = {}

for palabra in frase:
    dic[palabra] = dic.get(palabra, 0) + 1

print(dic)
"""


"""
personas = [
    {"nombre": "Ana", "edad": 20},
    {"nombre": "Luis", "edad": 25},
    {"nombre": "Pedro", "edad": 20}
]
{
    20: ["Ana", "Pedro"],
    25: ["Luis"]
}
"""
"""
personas = [
    {"nombre": "Ana", "edad": 20},
    {"nombre": "Luis", "edad": 25},
    {"nombre": "Pedro", "edad": 20},
]

agrupados = dict()

for diccionario in personas:
    edad = diccionario["edad"]
    nombre = diccionario["nombre"]

    if edad not in agrupados:
        agrupados[edad] = []

    agrupados[edad].append(nombre)

print(agrupados)
"""

estudiantes = {
    "001": {"nombre": "Ana", "notas": [4.0, 3.5, 5.0]},
    "002": {"nombre": "Luis", "notas": [3.0, 4.0, 4.5]},
}

for k, v in estudiantes.items():
    promedio = sum(v["notas"]) / len(v["notas"])
    print(f"{k} -> {estudiantes[k]["nombre"]} -> promedio: {promedio:2f}")

precios = {"manzana": 2, "banana": 1, "cereza": 5}
dic = {k: v for k, v in precios.items() if v > 2}
print(dic)
