def matrix_multiply(matrix1, matrix2):
    if not matrix1 or not matrix2:
        raise ValueError("One or both matrices are empty")

    if len(matrix1[0]) != len(matrix2):
      # if len(matrix2[0]) == len(matrix1):
      #   matrix1, matrix2 = matrix2, matrix1
      # else:
        raise ValueError("Incompatible matrices for multiplication")
    
    def are_all_elements_numeric(matrix):
      return all(isinstance(element, (int, float, complex)) for row in matrix for element in row)
    if (not are_all_elements_numeric(matrix1)) or (not are_all_elements_numeric(matrix2)):
       raise TypeError("A matrix has non numeric values as elements")

  
    m = len(matrix1)
    n = len(matrix1[0])
    p = len(matrix2[0])

    
    if any(len(row) != n for row in matrix1) or any(len(row) != p for row in matrix2):
        raise ValueError("Rows in a matrix have inconsistent lengths")

    C = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(m):
      for j in range(p):
        for k in range(n):
          C[i][j] += matrix1[i][k] * matrix2[k][j]



    return C