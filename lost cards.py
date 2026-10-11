N = int(input("Enter N:"))
a = int(input("Enter first card number:"))
b = int(input("Enter second card number:"))
c = int(input("Enter third card number:"))
d = int(input("Enter fourth card number:"))

total = a+b+c+d+N
add = a+b+c+d

lost_cards = total - add
print("The number of lost cards is:", lost_cards)