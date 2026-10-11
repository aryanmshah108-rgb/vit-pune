marks = 40
attendance = 20
marks_condition = marks >= 50
attendance_condition = attendance >= 75

#AND : Both conditions must be true
eligible = marks_condition and attendance_condition

#OR : At least one condition must be true
condition_met = marks_condition or attendance_condition

#NOT : Reverses the result
not_eligible = not eligible

print("Marks condition=", marks_condition)
print("Attendance condition=", attendance_condition)
print("AND=", eligible)
print("OR=", condition_met)
print("NOT=", not_eligible)