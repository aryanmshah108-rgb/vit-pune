a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))

if a>b and a>c:
    print("a is maximum number")
elif b>a and b>c:
    print("b is maximum number")
elif c>a and c>b:
    print("c is maximum number")

if a==b==c:
    print("All numbers are equal")
elif a==b:
    print("a and b are equal")
elif b==c:
    print("b and c are equal")
elif a==c:
    print("a and c are equal")