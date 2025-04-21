import random

class ExtensionFieldElement:
    def __init__(self, x, y, t, a, p ):
        """Representing the elements x + y * ξ of the ring with tuples
        and since the operations depend on a, t and p we represent
        the elements in the class with 5-tuples"""
        self.x = x
        self.y = y
        self.t = t
        self.a = a
        self.p = p

    # Defining addition
    def __add__(self, other):
        return ExtensionFieldElement(
            (self.x + other.x) % self.p ,
            (self.y + other.y) % self.p,
            self.t,
            self.a,
            self.p
        )

    # Two elements are equal if their x and y coordinates are equal
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Defining multiplication using the fact that ξ^2 = tξ - a
    def __mul__(self, other):
        x1, y1 = self.x, self.y
        x2, y2 = other.x, other.y
        p, t, a = self.p, self.t, self.a
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
            exponent = exponent // 2
        return result

    # If an element lies in the original field it returns True
    def is_in_base_field(self):
        return self.y == 0

# Calculating Legendre (a/p)
def legendre(a, p):
    result = 1
    base = a
    exponent = (p - 1) / 2
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % p
        base = base * base
        exponent = exponent // 2
    return result

# Checking a being a square
def square_check(a, p):
        if legendre(a, p) == 1:
            return True


def is_irreducible(a, p):
    """Checking weather the polynomial which we use for
    factorizing Fp[x] is irreducible or not."""
    while True:
        t = random.randrange(p)
        xi = ExtensionFieldElement(0, 1, t, a, p)
        xi_p = xi ** p
        if xi_p != xi and xi_p.y != 0:
            return t


def cip_alg(a, p):
    """Calculating one of the square roots of a"""
    if not square_check(a, p):
        message = "a is not a square"
        return message
    else:
        t = is_irreducible(a, p)
        xi = ExtensionFieldElement(0, 1, t, a, p)
        b = xi ** ((p + 1) // 2)
        return b.x

print(cip_alg(2377, 9973))


