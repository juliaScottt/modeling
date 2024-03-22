from colorpoint import ColoredPoint

class AdvancedColorPoint(ColoredPoint):
    def _init_(self, x, y, color):
        self._x=x
        self._y = y
        if color  in self.COLORS:
            self._color = color
        else:
            raise Exception(f"That is an invalid color, accepted colors are {self.COLORS}")



@property
def x(self):
    return self._x

@property
def y(self):
    return self._y

@property
def color(self):
    return self._color

p = ColoredPoint(10,10,"blue")
print(p)

