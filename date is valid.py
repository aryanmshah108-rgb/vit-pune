date = int(input("Enter date:"))
month = int(input("Enter month:"))
year = int(input("Enter year:"))
valid = True

if month < 1 or month>12:
    valid = False
elif date < 1 or date > 31:
    valid = False
elif month in [4,6,9,11] and date > 30:
    valid = False
elif month == 2:
    if(year%400 == 0) or (year%4 == 0 and year%100 != 0):
        if date>29:
            valid = False
    elif date > 28:
        valid = False

if valid:
    print(f"{date}/{month}/{year} is a valid date")
else:
    print(f"{date}/{month}/{year} is not a valid date")