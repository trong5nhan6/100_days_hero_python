from day4 import compute_output_matrix, kernel_22, kernel_33, convolutional_kernel


def padding(A):
    row_A, col_A = len(A), len(A[0])
    for i in range(row_A):
        A[i].insert(0, 0)
        A[i].append(0)
    zero_row = [0 for i in range(len(A[0]))]
    A.insert(0, zero_row)
    A.append(zero_row)
    return A


A = [[0, 0, 0], [0, 4, 0], [0, 1, 0]]
B = [[1, 1], [1, 1]]
C = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
A_padding = padding(A)

print(convolutional_kernel(A_padding, B, 2))
print(convolutional_kernel(A_padding, C, 3))
