def compute_interest(money, period):
    for i in range(period):
        money *= 1 + 1/period
    result = money
    return result


print(compute_interest(1, 12))
print(compute_interest(1, 365))
print(compute_interest(1, 730))
