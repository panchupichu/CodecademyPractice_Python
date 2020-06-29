"""Lesson Number One
   https://www.codecademy.com/courses/learn-python/lessons/student-becomes-the-teacher/exercises/how-is-everybody-doing-
   Python 3 deggued with Thonny
"""

#Create datasets
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}

alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}

tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]

#Print gradebook
for pupil in students:
    print(pupil["name"])
    print("Homework: %s" % pupil["homework"])
    print("Quizzes: %s" % pupil["quizzes"])
    print("Tests: %s" % pupil["tests"])
    print(" ")
    
#Calculate average
def average(numbers):
    total = float(sum(numbers))
    result = total/len(numbers)
    return result

#Weight
def get_average(student):
    homework = average(student["homework"])*0.1
    quizzes = average(student["quizzes"])*0.3
    tests = average(student["tests"])*0.6
    score = [homework, quizzes, tests]
    return sum(score)

#Send a letter
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

#Test the function
print("Lloys\'s letter grade: ")
print(get_letter_grade(get_average(lloyd)))
print()

#Create a funciton to get class average
def get_class_average(class_list):
    results = []
    for student in class_list:
        average_each = get_average(student)
        results.append(average_each)
    return average(results)

print("Class average grade: ")
#Get the class average
average_class = get_class_average(students)
print(average_class)
#Get the class average in letter grade
print(get_letter_grade(average_class))
