class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def affich(self):
        print(f"point : x = {str(self.x)} ", end='')
        print(f"Y = {str(self.y)} \n")

def where1(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y = {y}")
        case Point(x=x, y=0):
            print(f"X = {x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")

def where2(point):
    if point.x == 0 and point.y == 0:
        print("Origin")
    elif point.x == 0 and point.y != 0:
        print(f"Y = {point.y}")
    elif point.x != 0 and point.y == 0:
        print(f"X = {point.x}")  
    else:
        print("Somewhere else")

P1 = Point(2, 5)
P1.affich()
where1(P1)
where2(P1)
print(type(P1))