def fast_exp(a, p):
    result = 1
    base = a
    exponent = (p - 1) // 2
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % p
        base = base * base
        exponent //= 2
    return result

def square_check(a, p):
        if fast_exp(a, p) == 1:
            return True

print(square_check(2377, 6037))
