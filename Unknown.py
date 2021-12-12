import fractions
import numbers


class Unknown:
    def __init__(self, name: str, shift=0, scalar=1):
        self.name = name
        self.shift = shift
        self.scalar = scalar

    def __str__(self):
        scalar = '' if self.scalar == 1 else '-' if self.scalar == -1 else self.scalar
        shift = '' if self.shift == 0 else f"+ {self.shift}" if self.shift > 0 else f"- {abs(self.shift)}"
        return f"{scalar}{self.name} {shift}"

    def __add__(self, other):
        if isinstance(other, numbers.Number):
            return Unknown(self.name, self.shift + other, self.scalar)
        else:
            return NotImplemented

    def __mult__(self, other):
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

