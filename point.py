#Session 1 in economic modeling
import random


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    x = 2
    y = 3

a = Point(2, 3)
b = Point(7, 9)

print(f"a=({a.x}, {a.y})")
print(f"b=({b.x}, {b.y})")


# creating a list of random 5 points
points = [] # initialize an empty list
for _ in range(5):
   # x = random.randint(-100, 100)
   # y = random.randint(-100, 100)
   #  random_point = Point(x, y)
   # points.append(random_point)

    # or in a single line like this
    points.append(Point(random.randint(-100, 100),
                        random.randint(-100, 100)))

for point in points:
    print(f"p({point.x}, {point.y})")
# try to print the first point
print(points[0])

class Point:
    def __init__(self, x, y):
        """

        :param x: the value of x
        :param y: the value of y
        """
        self.x = y
        self.y = x

def __str__(self):
    """
    This will return the string value used in printing the point
    :return:
    """
    return f""

from point import Point
colors = ["red", "blue", "green", "purple", "pink", "beige", "bordeaux", "marsala", "peach", "turquoise", "saffron", "magenta"]
class ColoredPoint(Point): #this class inherits from point
    def _init_(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    def _str_(self):
        return f"{self.color}({self.x}, {self.y})"

#creating a list of rando 5 points
points = [] # initialize an empty list

for _ in range(5):
 #   x = random.randint(-100,100)
  #  y = random.randint(-100, 100)
   # random_point = Point(x,y)
    #points.append(random_point)

# or in a single line like this
  points.append(Point(random.randint(-100,100),
                        random.randint(-100,100)))

for point in points:
    print(f"p({point.x}, {point.y})")

#try to print the first point
print("This is the first point:", points[0])
print(points)
a = Point(3,4)
print(f"distance_origin a ={a.distance_origin()}")
b = Point(5,12)
print(f"distance_origin b ={b.distance_origin()}")
print(f"a>b= {a>b}, a<b = {a<b}")
print(f"a=b:{a==b}")

points.sort()
print(f"largest point is {points[-1]}")

