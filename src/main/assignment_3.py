import numpy as np

def Gaussian_Elimination(matrix, coefficient_matrix):
    return np.linalg.solve(matrix, coefficient_matrix)
    
def L_U_Factor(matrix):
    n = len(matrix)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    det = np.linalg.det(matrix)
    
    for i in range(n):
        for k in range(i, n):
            sum = 0
            for j in range(i):
                sum += (L[i][j] * U[j][k])
            U[i][k] = matrix[i][k] - sum
        
        for k in range(i, n):
            if i == k:
                L[i][i] = 1  
            else:
                sum = 0
                for j in range(i):
                    sum += (L[k][j] * U[j][i])
                L[k][i] = (matrix[k][i] - sum) / U[i][i]
    
    return det, L, U

def Diag_Dom(matrix):
    if len(matrix) != len(matrix[0]):
        return False

    for i in range(len(matrix)):
        diagonal = np.abs(matrix[i, i])
        row_sum = np.sum(np.abs(matrix[i, :])) - diagonal
        
        if diagonal <= row_sum:
            return False

    return True

def Positive_Definite(matrix):
    if len(matrix) != len(matrix[0]) or not np.allclose(matrix, matrix.T):
        return False
    
    eigenvalues = np.linalg.eigvals(matrix)

    for i in range(len(eigenvalues)):
        if eigenvalues[i] < 0:
            return False
    return True
