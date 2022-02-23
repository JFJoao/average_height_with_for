# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇

sum_heights = 0
sum_participants = 0

for n in student_heights:
  sum_heights += n
for n in student_heights:
  sum_participants += 1

average_height = round(sum_heights/sum_participants)
print (average_height)
