class IntervalMath(object):
    def __init__(self, lower, upper):
        self.lo = lower
        self.up = upper

    def __add__(self, other):
        a, b, c, d = self.lo, self.up, other.lo, other.up
        return IntervalMath(a + c, b + d)

    def __sub__(self, other):
        a, b, c, d = self.lo, self.up, other.lo, other.up
        return IntervalMath(a - d, b - c)

    def __mul__(self, other):
        a, b, c, d = self.lo, self.up, other.lo, other.up
        return IntervalMath(min(a*c, a*d, b*c, b*d),
                            max(a*c, a*d, b*c, b*d))

    def __truediv__(self, other):
        a, b, c, d = self.lo, self.up, other.lo, other.up
        # [c,d] ne peut pas contenir zéro :
        if c*d <= 0:
            raise ValueError (f'Intervalle {other} ne peut être le dénominateur car il contient zéro')
        return IntervalMath(min(a/c, a/d, b/c, b/d), max(a/c, a/d, b/c, b/d))
    
    def __rmul__(self, other):
        return IntervalMath(other, other)*self


    def __repr__(self):
        return f'[{self.lo:.2f}, {self.up:.2f}]'
