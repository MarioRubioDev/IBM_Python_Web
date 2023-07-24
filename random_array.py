'''
Genera una matriz de tamaño NxN y la llene con números aleatorios entre 0 y 9
'''

import random

def main():
    '''
    Bloque principal del programa
    '''
    try:
        number = int(input("Escribe un número para la matriz NxN: ")) 
        if number <= 0:
            raise ValueError()

        myArray=(makeArray(number))
        sumRowList=(sumRows(myArray))
        sumColumnList = (sumColumns(myArray))

        print('Array creado:')
        for i in range(len(myArray)):
            print(f' - Fila {i}: {myArray[i]}')

        print('Suma de filas:')
        for i in range(len(sumRowList)):
            print(f' - Fila {i} suma: {sumRowList[i]}')

        print('Suma de columnas:')
        for i in range(len(sumColumnList)):
            print(f' - Columna {i} suma: {sumColumnList[i]}')

    except ValueError as error:
        print(f'Error : Solo puede ingresar números enteros positivos')

def makeArray(number):
    '''
    Devuelve una matriz de NxN formada por números aleatorios entre el 0 y el 9 incluidos
    '''
    myRandomArray = []
    for i in range(number):
        listOfNumbers = randomNumber(number)
        myRandomArray.append(listOfNumbers)
    return myRandomArray

def randomNumber(number):
    '''
    Devuelve una lista con N números aleatorios entre el 0 y el 9 incluidos
    '''
    randomList = []
    for i in range(number):
        randomList.append(random.randrange(0,10))
    return randomList

def sumRows(myArray):
    '''
    Devuelde la suma de cada fila de la matriz que se pasa como argumento
    '''
    sumRowsList = []
    for i in range(len(myArray)):
        mySum = sum(myArray[i])
        sumRowsList.append(mySum)
    return sumRowsList

def sumColumns(myArray):
    '''
    Devuelde la suma de cada columna de la matriz que se pasa como argumento
    '''
    sumColumnsList = []
    for i in range(len(myArray)):
        mySum = 0
        for j in range(len(myArray)):
            mySum = mySum + (myArray[j][i])
        sumColumnsList.append(mySum)
    return sumColumnsList

if __name__ == '__main__':
    main()





