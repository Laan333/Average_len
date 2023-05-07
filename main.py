#all functions (len, summ, mean - module statistics)
student_heights = input("Input a list of student heights ").split()
all_sum = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

for person in student_heights:
  all_sum += person
all_sum = all_sum/len(student_heights)
all_sum = round(all_sum)
print(f"Average len students {all_sum}")