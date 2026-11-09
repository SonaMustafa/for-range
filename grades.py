students = [("Aysel", 95), ("Murad", 72), ("Leyla", 84), ("Elvin", 48), ("Nigar", 63)]
for i in range(len(students)):
    name, score = students[i]
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(name, ":", score, "→", grade)