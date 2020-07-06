# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def matrixInput():
    print("Called from inside matrixInput")
    rowSize = int(input("Please input you're 'm' size row "))
    columnSize = int(input("Please input you're 'n' size column "))
    matrixOne = [[0 for i in range(columnSize)] for j in range(rowSize)] 
    rowIterator = 0
    print("Type in your matrix inputs starting from first row input")
    while rowIterator < rowSize:
        columnIterator = 0
        while columnIterator < columnSize:
            matrixOne[rowIterator][columnIterator] = int(input())
            columnIterator += 1
        rowIterator += 1
    return matrixOne

def matarixMultTest(firstMatrix,secondMatrix):
    print("Inside matrixMult()")
    newRow = int(len(firstMatrix))
    rowMax = int(len(firstMatrix))
    newColumn = len(secondMatrix[0])
    columnMax = int(len(secondMatrix[0]))
    print("new Row and new Column are")
    print(newRow)
    print(newColumn)
    if isinstance(newRow, int):
        print("myInput is an int")
    else:
        print("myInput is not an int")
    newMatrix = [[0 for i in range(newColumn)] for j in range(newRow)]
    for newRow in newMatrix:
        print(newRow)
    numberOfSums = len(secondMatrix)
    rowIterator = 0
    while rowIterator < rowMax:
        columnIterator = 0
        while columnIterator < columnMax:
            sumIterator = 0
            while sumIterator < numberOfSums:
                print("first matrix")
                print(firstMatrix[rowIterator][sumIterator])
                print("second matrix")
                print(secondMatrix[sumIterator][columnIterator])
                newMatrix[rowIterator][columnIterator] += firstMatrix[rowIterator][sumIterator] * secondMatrix[sumIterator][columnIterator]
                sumIterator += 1
                for newRow in newMatrix:
                    print(newRow)
            print("I'm out of lowerIterator while loop")
            columnIterator += 1
        rowIterator += 1
    print("I'm out of the masterIterator while loop")
    print("I made it outside the matrix sum loop")
    for newRow in newMatrix:
        print(newRow)
        
def RREF(matrix):
    print("Inside RREF funcation")
    
      
def main():
    while True:
        firstArray = matrixInput()
        secondArray = matrixInput()
        columeSize = len(firstArray[0])
        rowSize = len(secondArray)
        if columeSize == rowSize:
            print ("Matrix can be mulitiplied")
        else:
            print("These two matrix can not be mulitplied")
        matarixMultTest(firstArray, secondArray)
        print(rowSize)
        junkEraseMe = int(input("Testing while loop"))
        if junkEraseMe == 0:
            break


    print("End")

main()














"""
    print("Called from inside main")
    print("Input for size for second matrix")
    rowSize = int(input("Please input you're 'm' size row "))
    columnSize = int(input("Please input you're 'n' size column "))
    matrixTwo = [[0 for i in range(columnSize)] for j in range(rowSize)]
    rowIterator = 0
    print("Type in your matrix inputs starting from first row input")
    while rowIterator < rowSize:
        columnIterator = 0
        while columnIterator < columnSize:
            matrixTwo[rowIterator][columnIterator] = int(input())
            columnIterator += 1
        rowIterator += 1

    for rowSize in matrixTwo: 
        print(rowSize) 
    junkInt = 100
    matrixInput(junkInt) 
    
    def matrixMulti(firstMatrix, secondMatrix):
    print("Inside matrixMult()")
    newRow = int(len(firstMatrix))
    Counter = int(len(firstMatrix))
    newColumn = len(secondMatrix[0])
    print("new Row and new Column are")
    print(newRow)
    print(newColumn)
    if isinstance(newRow, int):
        print("myInput is an int")
    else:
        print("myInput is not an int")
    newMatrix = [[0 for i in range(newColumn)] for j in range(newRow)]
    for newRow in newMatrix:
        print(newRow)
    numberOfSums = len(secondMatrix)
    newRowMatrixIterator = 0
    if isinstance(newRow, int):
        print("myInput is an int")
    else:
        print("myInput is not an int")
    while newRowMatrixIterator < Counter:
        newColumnMatrixIterator = 0
        while newColumnMatrixIterator < newColumn:
            masterIterator = 0
            while masterIterator < newColumn:
                lowerIterator = 0
                while lowerIterator < numberOfSums:
                    print("first matrix")
                    print(firstMatrix[newRowMatrixIterator][lowerIterator])
                    print("second matrix")
                    print(secondMatrix[lowerIterator][masterIterator])
                    newMatrix[newRowMatrixIterator][masterIterator] += firstMatrix[newRowMatrixIterator][lowerIterator] * secondMatrix[lowerIterator][masterIterator]
                    lowerIterator += 1
                    for newRow in newMatrix:
                        print(newRow)
                print("I'm out of lowerIterator while loop")
                masterIterator += 1
            newColumnMatrixIterator += 1
            print("I'm out of the masterIterator while loop")
        newRowMatrixIterator += 1
    print("I made it outside the matrix sum loop")
    for newRow in newMatrix:
        print(newRow)

    
    
    
"""






"""
    if isinstance(rowSize, int):
        print("myInput is an int")
    else:
        print("myInput is not an int")
    if isinstance(rowSize, str):
        print("myInput is a string!")
        
    print(type(rowSize))
    print(type(columnSize))

        
"""