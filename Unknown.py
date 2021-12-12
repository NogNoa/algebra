import fractions
import numbers


class Unknown:
    def __init__(self, name: str, deg=1, scalar=1):
        self.name = name
        self.deg = deg
        self.scalar = scalar

    def __str__(self):
        scalar = self.scalar if self.deg == 0 else '' if self.scalar == 1 else '-' if self.scalar == -1 else str(
            self.scalar) + ('/' if self.deg < 0 else '*' if isinstance(self.scalar, fractions.Fraction) else '')
        return f"{scalar}{self.name}"

    def __eq__(self,other):
        if isinstance(other, Unknown):
            return (self.name, self.deg, self.scalar) == (other.name, other.deg, other.scalar)
        elif isinstance(other, numbers.Number):
            if self.deg == 0 or self.scalar == 0:
                return other == self.scalar
            else:
                return False
        else:
            return NotImplemented


class formula:
    def __init__(self, degi: dict[int:Unknown]):
        self.degi = degi

    @property
    def highest(self):
        return max(self.degi.keys())

    @property
    def lowest(self):
        return min(self.degi.keys())

    def __getitem__(self, d):
        return self.degi[d]

    def __str__(self):
        back = ''
        for d in range(self.highest, self.lowest-1, -1):
            if self[d] == 0:
                continue
            oper = "" if d == self.highest else "+ " if self[d].scalar >= 0 else "- "
            back += f"{oper}{self[d]} "
        return back

"""
    def __add__(self, other):
        if isinstance(other, numbers.Number):
            return formula(self.name, self.shift + other, self.scalar)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return formula(self.name, self.shift * other, self.scalar * other)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, numbers.Number):
            return formula(self.name, self.shift - other, self.scalar)
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, numbers.Number):
            return formula(self.name, other - self.shift, -self.scalar)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, numbers.Number):
            return formula(self.name, fractions.Fraction(self.shift, other), fractions.Fraction(self.scalar, other))
        else:
            return NotImplemented

    def __neg__(self):
        return self * -1


def alg_addition(a: formula, b: formula):
    if a.name == b.name:
        return formula(a.name, a.shift + b.shift, a.scalar + b.scalar)
"""

#   todo: object of single unknown and it's scalar, and seperete object of one side of the equation.
