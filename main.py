import functions
import sys
import field_class


# Choose input p and a
p = 11
a = 3

if not functions.square_check(a, p):
    sys.exit("a is not a square")

t = functions.is_irreducible(a, p)

xi = field_class.ExtensionFieldElement(0, 1, t, a, p)

b = xi ** ((p + 1) / 2)

# Checking everything
if b.is_in_base_field():
    print("That is good")

a_in_field = field_class.ExtensionFieldElement(a, 0, t, a, p)
if b ** 2 == a_in_field:
    print("That is also good")

print(b.x)