# Lists

timetable = ["Computer Science", "Math", "English", "Art", "Sport"]

timetable = ["Computer Science", "Math", "English", "Art", "Sport"]
print(timetable)

timetable = ["Computer Science", "Math", "English", "Art", "Sport"]
print(timetable[1])
print()
# Changing Lists
timetable = ["Computer Science", "Math", "English", "Art", "Sport"]
print(timetable[0])
print(timetable[1])
print(timetable[2])
print(timetable[3])
print(timetable[4])
print()
timetable[4] = "Watch TV"
print(timetable[0])
print(timetable[1])
print(timetable[2])
print(timetable[3])
print(timetable[4])
print()
# Lists and Loops
timetable = ["Computer Science", "Math", "English", "Art", "Watch TV"]
for lesson in timetable:
    print(lesson)

print()
# day32 challenge
import random

greetings = ["Hello there!", "Konnichiwa", "Guten Tag!", "Bore Da!"]
index = random.randint(0, 3)
print(greetings[index])



