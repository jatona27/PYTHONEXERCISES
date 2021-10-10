#notas = {}
asignaturas = ["Programacion", "Skills", "Fundamentos"]
alumnos = ["Pilar", "Jaime", "Rafa"]
'''
for asignatura in asignaturas:
    print("Introduza la nota de ", asignatura)
    nota = input()
    notas[asignatura] = nota
print(notas)
suma = 0
for asig,n in notas.items():
    print(asig)
    print(n)
    suma = suma + float(n)
media = round(suma/len(notas),2)
print(media)
notas["Nota media"] = media
print(notas)
'''

# diccionadio de diccionarios

def introduce_notas(asignaturas):
    notas = {}
    for asignatura in asignaturas:
        print("Introduza la nota de ", asignatura)
        nota = input()
        notas[asignatura] = nota
    return notas

notas_alumnos = {}
for alumn in alumnos:
    print("Notas del alumno: ", alumn)
    notas = introduce_notas(asignaturas)
    notas_alumnos[alumn] = notas
print(notas_alumnos)