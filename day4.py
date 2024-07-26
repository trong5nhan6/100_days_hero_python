def compute_output_matrix(A, B):
    row_A, col_A = len(A), len(A[0])
    row_B, col_B = len(B), len(B[0])
    output_row = row_A - row_B + 1
    output_col = col_A - col_B + 1
    output_matrix = [[0] * output_row for i in range(output_col)]
    return output_row, output_col, output_matrix


def kernel_22():
    x = [0, 0, 1, 1]
    y = [0, 1, 0, 1]
    return x, y


def kernel_33():
    x = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    y = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    return x, y


def convolutional_kernel(A, B, kernel):
    output_row, output_col, output_matrix = compute_output_matrix(A, B)
    if kernel == 2:
        x, y = kernel_22()
    elif kernel == 3:
        x, y = kernel_33()

    for i in range(output_row):
        for j in range(output_col):
            total = 0
            for k in range(len(x)):
                total += A[i+x[k]][j+y[k]] * B[x[k]][y[k]]
            output_matrix[i][j] = total
    return output_matrix


def convolutional_kernel_33(A, B):
    output_row, output_col, output_matrix = compute_output_matrix(A, B)
    x = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    y = [0, 1, 2, 0, 1, 2, 0, 1, 2]


A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[2, 4], [1, 3]]
C = [[1, 1, 1], [0, 0, 0], [1, 1, 1]]
print(convolutional_kernel(A, B, 2))
print(convolutional_kernel(A, C, 3))
