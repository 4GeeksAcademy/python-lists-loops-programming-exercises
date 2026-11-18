# Your code here
def matrix_builder(rowsAndCols):
    newMatrix = []
    for i in  range(0,rowsAndCols, 1):
        row = []
        for j in range(0, rowsAndCols, 1):
            row.append(1) 
        newMatrix.append(row)              
    return newMatrix

print(matrix_builder(3))

