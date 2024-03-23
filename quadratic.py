class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def standard_form(self):
        return f"{self.a}x^2 + {self.b}x + {self.c}"

    def vertex_form(self):
        h = -self.b / (2 * self.a)
        k = self.a * h**2 + self.b * h + self.c
        return f"y = {self.a}(x - {h})^2 + {k}"

    # Add methods to calculate the discriminant, roots, and vertex of the quadratic
    def discriminant(self):
        return self.b**2 - 4 * self.a * self.c

    def roots(self):
        d = self.discriminant()
        if d > 0:
            root1 = (-self.b + d**0.5) / (2 * self.a)
            root2 = (-self.b - d**0.5) / (2 * self.a)
            return root1, root2
        elif d == 0:
            return -self.b / (2 * self.a),
        else:
            return "No real roots"

    def vertex(self):
        h = -self.b / (2 * self.a)
        k = self.a * h**2 + self.b * h + self.c
        return h, k
