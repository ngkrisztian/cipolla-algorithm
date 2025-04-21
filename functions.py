import random
import field_class

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

def is_irreducible(a, p):
    while True:
        t = random.randrange(p)
        xi = field_class.ExtensionFieldElement(0, 1, t, a, p)
        xi_p = xi ** p
        if xi_p != xi and xi_p.y != 0:
            return t



