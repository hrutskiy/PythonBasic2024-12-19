class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Знаменник не може бути нулем")
        self.a = a
        self.b = b

    # Множення дробів
    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_a = self.a * other.a
            new_b = self.b * other.b
            return Fraction(new_a, new_b)
        return NotImplemented

    # Додавання дробів без скорочення
    def __add__(self, other):
        if isinstance(other, Fraction):
            new_a = self.a * other.b + self.b * other.a
            new_b = self.b * other.b
            return Fraction(new_a, new_b)
        return NotImplemented

    # Віднімання дробів без скорочення
    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_a = self.a * other.b - self.b * other.a
            new_b = self.b * other.b
            return Fraction(new_a, new_b)
        return NotImplemented

    # Порівняння дробів на рівність
    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b == self.b * other.a
        return NotImplemented

    # Порівняння (більше)
    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b > self.b * other.a
        return NotImplemented

    # Порівняння (менше)
    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b < self.b * other.a
        return NotImplemented

    # Вивід дробу у вигляді рядка
    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

# Тести
f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')