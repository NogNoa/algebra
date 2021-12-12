import fractions
import numbers


class Unknown:
    def __init__(self, name: str, shift=0, scalar=1, recip=False):
        self.name = name
        self.shift = shift
        self.scalar = scalar
        self.recip = recip

    def __str__(self):
        scalar = '' if self.scalar == 1 else '-' if self.scalar == -1 else str(self.scalar) + (
            '/' if self.recip else "*")
        shift = '' if self.shift == 0 else f"+ {self.shift}" if self.shift > 0 else f"- {abs(self.shift)}"
        return f"{scalar}{self.name} {shift}"

    def __add__(self, other):
        if isinstance(other, numbers.Number):
            return Unknown(self.name, self.shift + other, self.scalar)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return Unknown(self.name, self.shift * other, self.scalar * other)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, numbers.Number):
            return Unknown(self.name, self.shift - other, self.scalar)
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, numbers.Number):
            return Unknown(self.name, other - self.shift, -self.scalar)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, numbers.Number):
            return Unknown(self.name, fractions.Fraction(self.shift, other), fractions.Fraction(self.scalar, other))
        else:
            return NotImplemented

    def __neg__(self):
        return self*-1


def alg_addition(a: Unknown, b: Unknown):
    if a.name == b.name:
        if a.recip == b.recip:
            return Unknown(a.name, a.shift + b.shift, a.scalar + b.scalar)

#   todo: object of single unknown and it's scalar, and seperete object of one side of the equation.

