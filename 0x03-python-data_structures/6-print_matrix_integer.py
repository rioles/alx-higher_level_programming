def print_matrix_integer(matrix=[[]]):
    k = 0
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[i])):
            print(matrix[i][j], end = ' ')
            if j == (len(matrix[i]) - 1):
                print('\n')
        


