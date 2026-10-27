ROWS = 3
COLS = 4
EMPTY = 0
RESERVED = -1
MAX_ROLL = 20

seats = [
    [1, 2, 3, 4],
    [5, 6, 2, RESERVED],
    [9, EMPTY, 11, 25]
]

valid = True
seen = set()

print("Examination Seating Validation\n")

for i in range(ROWS):
    for j in range(COLS):
        roll = seats[i][j]
        print(f"Seat ({i + 1}, {j + 1}): {roll}", end=" -> ")

        if roll == EMPTY:
            print("Empty seat")
            valid = False

        elif roll == RESERVED:
            print("Reserved position")

        elif roll < 1 or roll > MAX_ROLL:
            print("Invalid roll number")
            valid = False

        elif roll in seen:
            print("Duplicate roll number")
            valid = False

        else:
            print("Valid allocation")
            seen.add(roll)

if valid:
    print("\nSeating matrix is valid.")
else:
    print("\nSeating matrix has validation errors.")
