coche = {}
coches = {}
caracteristicas = ["Km", "Combustible", "Color", "Marca"]
propietarios = ["Joan", "Jaime", "Ali", "Rocio", "Angela"]

def introduce_caract(caracteristicas):
    for caract in caracteristicas:
        print("Introduzca detalle de la característica: ",caract)
        savecaract = input()
        coche[caract] = savecaract
    return coche

for prop in propietarios:
    print("Introduzca detalle del coche de: ",prop)
    coche = introduce_caract(caracteristicas)
    coches[prop] = coche
print(coches)

