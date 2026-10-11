A = int(input("Enter no.of students:"))
B = int(input("Enter no.of students:"))
C = int(input("Enter no.of students:"))

bench1 = A/2
bench2 = B/2
bench3 = C/2

sum = bench1+bench2+bench3

if (bench1%2 == 0) && (bench2%2 == 0) && (bench3%2 == 0):
    print("All students are sitted on the benches")
elif (bench1+1)//2 & (bench2+1)//2 & (bench3+1)//2:
    print("Some students are singally sitted")
      