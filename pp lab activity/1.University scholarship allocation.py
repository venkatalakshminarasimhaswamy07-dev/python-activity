
students = [
    {
        "id": 101,
        "name": "Ravi",
        "aggregate": 85,
        "subjects": [80, 90, 85],
        "attendance": 90,
        "income": 180000
    },
    {
        "id": 102,
        "name": "Sita",
        "aggregate": 85,
        "subjects": [75, 80, 85],
        "attendance": 95,
        "income": 200000
    },
    {
        "id": 103,
        "name": "Kiran",
        "aggregate": 70,
        "subjects": [65, 70, 75],
        "attendance": 80,
        "income": 150000
    }
]

eligible = []

for s in students:
    reasons = []

    if s["aggregate"] < 75:
        reasons.append("Aggregate below 75%")

    if min(s["subjects"]) < 60:
        reasons.append("Subject marks below 60%")

    if s["attendance"] < 75:
        reasons.append("Attendance below 75%")

    if s["income"] > 250000:
        reasons.append("Income exceeds limit")

    if not reasons:
        eligible.append(s)
    else:
        print(s["name"], "Not eligible:", ", ".join(reasons))

# Ranking and tie-breaking
eligible.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"],
        -min(s["subjects"]),
        s["id"]
    )
)

print("\nScholarship Ranking:")
for rank, s in enumerate(eligible, start=1):
    print(rank, s["name"], s["aggregate"])
