import math

def quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2

def triangle_area(base, height):
    area = 0.5 * base * height
    return area

def linear(m,b):
    root = -(b/m)
    return root
