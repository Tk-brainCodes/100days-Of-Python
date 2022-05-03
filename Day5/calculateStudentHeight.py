student_heights = input("Input a list of students height \n").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    print(student_heights)

total_student_heights = sum(student_heights) 

#average student
for val in student_heights:
    average_height = total_student_heights / len(student_heights)
    average_height_rounded = round(average_height)
print(f"Average height: {average_height_rounded}")

#hightest score [2,3,5,6,7]
max_number = 0
for max in student_heights:
    if max > max_number:
        max_number = max
        print(f"Your maximun number is: {max}")