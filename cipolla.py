import random

class ExtensionFieldElement:
    def __init__(self, x, y, t, a, p ):
        """Represents x + y*ξ where ξ^2 = tξ - a"""
        self.x = x % p
        self.y = y % p
        self.t = t
        self.a = a
        self.p = p

    def __add__(self, other):
        return ExtensionFieldElement(
            self.x + other.x,
            self.y + other.y,
            self.t,
            self.a,
            self.p
        )

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y and
                self.t == other.t and self.a == other.a and self.p == other.p)

    def __mul__(self, other):
        x1, y1 = self.x, self.y
        x2, y2 = other.x, other.y
        p, t, a = self.p, self.t, self.a
        # ξ^2 = tξ - a
        new_x = (x1 * x2 + y1 * y2 * (-a)) % p
        new_y = (x1 * y2 + x2 * y1 + y1 * y2 * t) % p
        return ExtensionFieldElement(new_x, new_y, t, a, p)

    # Fast exponentiation
    def __pow__(self, exponent):
        result = ExtensionFieldElement(1, 0, self.t, self.a, self.p)
        base = self
        while exponent > 0:
            if exponent % 2 == 1:
                result = result * base
            base = base * base
            exponent //= 2
        return result

    def is_in_base_field(self):
        if self.y == 0:
            return True

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
        xi = ExtensionFieldElement(0, 1, t, a, p)
        xi_p = xi ** p
        if xi_p != xi and xi_p.y != 0:
            return t

def cip_alg(a, p):
    if not square_check(a, p):
        message = "a is not a square"
        return message
    else:
        t = is_irreducible(a, p)
        xi = ExtensionFieldElement(0, 1, t, a, p)
        b = xi ** ((p + 1) // 2)
        return b.x


