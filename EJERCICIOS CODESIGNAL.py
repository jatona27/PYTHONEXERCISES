#EJERCICIO 1:
print("Please enter a number between -1000 and 1000: ")
param1 = 1
param2 = 2
def add(param1, param2):
    return param1 + param2

#EJERCICIO 2:
def centuryFromYear(year):
    return (year - 1) // 100 + 1
print(centuryFromYear(2017))

#EJERCICIO 3:
def checkPalindrome(inputString):
    sigo = False
    isPalindrome = False
    lenString = len(inputString)
    print(lenString)
    revindex = lenString - 1
    for index in range(lenString):
        if index == revindex:
            sigo = True
            break
        if index < revindex:
            if inputString[index]  == inputString[revindex]:
                sigo = True
                revindex -= 1
            else:
                sigo = False
                break
        else:
            break
    return sigo

#EJERCICIO 4:
inputArray = [3, 6, -2, -5, 7, 3]
longitud = len(inputArray)
prodadj = 0
prodmayor = 0 #ponemos esta variable para tener el valor del prodadj que obtenemos y de esta manera irá comparando hasta cambiar cuando un prodadj sea mayor que el prodmayor
for num in range(len(inputArray)-1): #utilizo len porque necesito saber las posiciones de cada número
    prodadj = inputArray[num] * inputArray[num+1]
    if prodmayor < prodadj:
        prodmayor = prodadj
print(prodmayor)


#como pueden haber números negativos y el 0 es mayor que ellos hemos tenido que cambiar el código por éste:
inputArray = []
longitud = len(inputArray)
def adjacentElementsProduct(inputArray):
    prodmayor = 0 #nos obliga a definirlo
    for num in range(len(inputArray)-1):
        prodadj = inputArray[num] * inputArray[num+1]
        if num == 0:
            prodmayor = prodadj #le decimos que asigne el primer valor de prodadj para que en caso de que haya un negativo y el prodmayor sea 0 np nos de problema, ya que ahora el prodmayor será negativo/positivo dependiendo del primer valor de prodadj
        if prodmayor < prodadj:
            prodmayor = prodadj
    return prodmayor
resultado = adjacentElementsProduct(inputArray)
print(resultado)


#EJERCICIO 5: SHAPEAREA

def shapeArea(n):
    if (n == 1):
        return 1
    else:
        a = 1
        for i in range(1, n+1):
            a = a + i * 4 - 4
        return a

#EJERCICIO 6:
def makeArrayConsecutive2(statues):
    statues = [6, 2, 3, 8]
    statues.sort()
    valormax = statues[len(statues) - 1]
    valormin = statues[0]
    item_buscar = valormin + 1
    not_found = []
    while item_buscar < valormax:
        encontrado = False
        for statue in statues:
            if item_buscar == statue:
                encontrado = True
                break
        if encontrado == False:
            not_found.append(item_buscar)
        item_buscar += 1
    print("Faltan ", len(not_found), " estatuas")
    print(not_found)

    #EJERCICIO 7:




