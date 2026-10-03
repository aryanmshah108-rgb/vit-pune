Name = (input("Enter Student Name:"))
Roll_no = int(input("Enter Students Roll no.:"))

# check result
English = float(input("Enter English marks:"))
Maths = float(input("Enter Maths marks:"))
Science = float(input("Enter Science marks:"))
SocialStudies = float(input("Enter Social Studies marks:"))
Hindi = float(input("Enter Hindi marks:"))
Computer = float(input("Enter Computer marks:"))

Total_Marks = English + Maths + Science + SocialStudies + Hindi + Computer
print("Your total marks:", Total_Marks)
Percentage = (Total_Marks/600)*100
print("Your Percentage:", Percentage)

Attendance = 85

#conditions
if(Percentage>=50 and Attendance>=75):
    print("You are Pass")

if(Percentage>=50 and Attendance<=75):
    print("You are Pass but you will be promoted to lower division in next class")

if(Percentage<=50 and Attendance>=75):
    print("You are fail")

if(Percentage<=50 and Attendance<=75):
    print("You are fail")


