
# Sports Tournament Ranking System

teams = {}

n = int(input("Enter number of teams: "))

# Initialize team details
for i in range(n):
    name = input(f"Enter team {i + 1} name: ")
    teams[name] = {
        "played": 0,
        "won": 0,
        "drawn": 0,
        "lost": 0,
        "goals_for": 0,
        "goals_against": 0,
        "points": 0
    }

m = int(input("Enter number of matches: "))

# Store and process match results
for i in range(m):
    print(f"\nMatch {i + 1}")

    team1 = input("Enter first team: ")
    team2 = input("Enter second team: ")

    if team1 not in teams or team2 not in teams or team1 == team2:
        print("Invalid team names. Match skipped.")
        continue

    score1 = int(input(f"Enter goals scored by {team1}: "))
    score2 = int(input(f"Enter goals scored by {team2}: "))

    if score1 < 0 or score2 < 0:
        print("Invalid scores. Match skipped.")
        continue

    teams[team1]["played"] += 1
    teams[team2]["played"] += 1

    teams[team1]["goals_for"] += score1
    teams[team1]["goals_against"] += score2

    teams[team2]["goals_for"] += score2
    teams[team2]["goals_against"] += score1

    if score1 > score2:
        teams[team1]["won"] += 1
        teams[team1]["points"] += 3
        teams[team2]["lost"] += 1

    elif score2 > score1:
        teams[team2]["won"] += 1
        teams[team2]["points"] += 3
        teams[team1]["lost"] += 1

    else:
        teams[team1]["drawn"] += 1
        teams[team2]["drawn"] += 1
        teams[team1]["points"] += 1
        teams[team2]["points"] += 1

# Calculate goal difference and ranking
ranking = []

for name, data in teams.items():
    goal_difference = data["goals_for"] - data["goals_against"]

    ranking.append((
        name,
        data["played"],
        data["won"],
        data["drawn"],
        data["lost"],
        data["points"],
        goal_difference,
        data["goals_for"]
    ))

# Ranking policy:
# 1. Highest points
# 2. Highest goal difference
# 3. Highest goals scored
ranking.sort(key=lambda x: (x[5], x[6], x[7]), reverse=True)

# Display final table
print("\n========== TOURNAMENT RANKINGS ==========")
print(f"{'Rank':<6}{'Team':<15}{'P':<5}{'W':<5}"
      f"{'D':<5}{'L':<5}{'Pts':<6}{'GD':<6}")

for rank, team in enumerate(ranking, start=1):
    name, played, won, drawn, lost, points, gd, goals = team

    print(f"{rank:<6}{name:<15}{played:<5}{won:<5}"
          f"{drawn:<5}{lost:<5}{points:<6}{gd:<6}")
