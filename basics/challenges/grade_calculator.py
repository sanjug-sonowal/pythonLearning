'''Grade Calculator
5 subjects ke marks lo. Average nikalo. Grade do:

90+ → A+
80-89 → A
70-79 → B
60-69 → C
Below 60 → F

Agar kisi bhi subject me 33 se kam hai toh regardless → "FAIL"'''

subjects = {
    "maths":90,
    "chemistry":90,
    "biology":95,
    "economics":70,
    "Accounting":90
}

total = 0

for marks in subjects.values():
    if marks < 33:
        print("Fail")
        exit()

for number in subjects.values():
    total += number

avg = total / len(subjects)

if avg > 90:
    print("A+")
elif avg >= 80:
    print("A")
elif avg >= 70:
    print("B")
elif avg >= 60:
    print("C")
else:
    print("F")
