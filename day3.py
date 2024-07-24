def find_squared_root(a):
    EPSILON = 0.001
    x_n = a
    while True:
        f_x_n = x_n**2 - a
        f_prime_x_n = 2 * x_n

        x_n1 = x_n - f_x_n / f_prime_x_n

        if abs(x_n1 - x_n) < EPSILON:
            return x_n1

        x_n = x_n1


find_squared_root(2)
print(find_squared_root(3))
