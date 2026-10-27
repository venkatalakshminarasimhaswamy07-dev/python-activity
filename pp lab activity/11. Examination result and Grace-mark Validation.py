
# Examination Result and Grace-Mark Validation

n = int(input("Enter number of subjects: "))
subjects = []

total = 0
grace_limit = 5
grace_used = 0

for i in range(n):
    print("\nSubject", i + 1)

    name = input("Enter subject name: ")
    maximum = int(input("Enter maximum marks: "))
    marks = int(input("Enter obtained marks: "))
    pass_mark = int(input("Enter minimum pass marks: "))

    if maximum <= 0 or pass_mark < 0 or pass_mark > maximum:
        print("Invalid subject criteria!")
        continue

    if marks < 0 or marks > maximum:
        print("Invalid marks! Enter marks within the maximum.")
        continue

    grace = 0

    # Apply grace marks if the student narrowly fails
    if marks < pass_mark:
        needed = pass_mark - marks

        if needed <= grace_limit - grace_used:
            grace = needed
            grace_used += grace
            marks += grace

    # Ensure marks never exceed maximum marks
    marks = min(marks, maximum)

    total += marks

    if marks >= pass_mark:
        status = "PASS"
    else:
        status = "FAIL"

    subjects.append((name, marks, maximum, status, grace))

print("\n========== FINAL RESULT ==========")

all_pass = True

for name, marks, maximum, status, grace in subjects:
    print(f"{name}: {marks}/{maximum} | {status} | Grace: {grace}")
    if status == "FAIL":
        all_pass = False

max_total = sum(subject[2] for subject in subjects)
percentage = (total / max_total * 100) if max_total > 0 else 0

if all_pass:
    if percentage >= 75:
        classification = "Distinction"
    elif percentage >= 60:
        classification = "First Class"
    elif percentage >= 50:
        classification = "Second Class"
    else:
        classification = "Pass Class"
else:
    classification = "Fail"

print("----------------------------------")
print("Total Marks:", total, "/", max_total)
print("Percentage:", round(percentage, 2), "%")
print("Grace Marks Used:", grace_used)
print("Final Classification:", classification)
