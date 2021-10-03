inputArray = [3, 6, -2, -5, 7, 3]
longitud = len(inputArray)
prodadj = 0
prodmayor = 0 #ponemos esta variable para antener el valor del prodadj que obtenemos y de esta manera irá comparando hasta cambiar cuando un prodadj sea mayor que el prodmayor
for num in range(len(inputArray)-1): #utilizo len porque necesito saber las posiciones de cada número
    prodadj = inputArray[num] * inputArray[num+1]
    if prodmayor < prodadj:
        prodmayor = prodadj
print(prodmayor)
