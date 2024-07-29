def out_put_matrix(A):
    row_A, col_A = len(A), len(A[0])
    out_put_matrix = [[0]*int(col_A/2) for i in range(int(row_A/2))]
    return row_A, col_A, out_put_matrix


def kernel_22():
    x = [0, 0, 1, 1]
    y = [0, 1, 0, 1]
    return x, y


def max_pooling(A):
    row_A, col_A, matrix_result = out_put_matrix(A)
    x, y = kernel_22()
    for i in range(int(row_A/2)):
        for j in range(int(col_A/2)):
            max_pooling = A[i*2 + x[0]][j*2 + y[0]]
            for k in range(len(x)):
                if max_pooling <= A[i*2 + x[k]][j*2 + y[k]]:
                    max_pooling = A[i*2 + x[k]][j*2 + y[k]]
            matrix_result[i][j] = max_pooling

    return matrix_result

def average_pooling(A):
    row_A, col_A, matrix_result = out_put_matrix(A)
    x, y = kernel_22()
    for i in range(int(row_A/2)):
        for j in range(int(col_A/2)):
            total = 0
            for k in range(len(x)):
                total += A[i*2 + x[k]][j*2 + y[k]]
            matrix_result[i][j] = total/len(x)

    return matrix_result

A = [[0, 0, 0, 4], [0, 4, 0, 2], [0, 1, 0, 2], [0, 3, 0, 2]]
print(max_pooling(A))
print(average_pooling(A))
