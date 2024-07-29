def Euclidean_distance(A):
    total = 0
    for i in range(len(A)):
        total += A[i]**2
    return total**0.5


def dot_product(A, B):
    total = 0
    for i in range(len(A)):
        total += A[i]*B[i]
    return total


def cosine_similarity(A, B):
    result = dot_product(A, B) / (Euclidean_distance(A)
                                  * Euclidean_distance(B))
    return result


A = [1, 2]
B = [4, 5]

# cosine = CosineSimilarity(A, B)
cosine = cosine_similarity(A, B)
print(cosine)
