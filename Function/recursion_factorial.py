def fact(n):
    if n < 0:
        raise ValueError("Negative values are not allowed")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
print(fact(5))  # Output: 120