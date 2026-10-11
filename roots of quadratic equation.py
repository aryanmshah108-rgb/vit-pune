#roots of equation:ax^2+bx+c=0
import math

a = float(input("Enter coefficient a:"))
b = float(input("Enter coefficient b:"))
c = float(input("Enter coefficient c:"))

d = b**2 - 4*a*c

if d>0:
    root1 = (-b + math.sqrt(d)) / (2*a)
    root2 = (-b - math.sqrt(d)) / (2*a)
    print(f"Two real roots: {root1} and {root2}")
elif d== 0:
    root = -b / (2*a)
    print(f"One real root: {root}")
else:
    real_part = -b / (2*a)
    img_part = math.sqrt(-d) / (2*a)
    print(f"Complex roots: {real_part} + {img_part}i and {real_part} - {img_part}i")