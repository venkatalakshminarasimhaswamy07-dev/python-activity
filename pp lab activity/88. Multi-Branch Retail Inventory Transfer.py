
# Multi-Branch Retail Inventory Transfer

branches = {
    "Branch A": {
        "stock": {"Laptop": 20, "Mouse": 50, "Keyboard": 15},
        "target": {"Laptop": 15, "Mouse": 40, "Keyboard": 25}
    },
    "Branch B": {
        "stock": {"Laptop": 5, "Mouse": 20, "Keyboard": 30},
        "target": {"Laptop": 15, "Mouse": 30, "Keyboard": 20}
    },
    "Branch C": {
        "stock": {"Laptop": 10, "Mouse": 35, "Keyboard": 10},
        "target": {"Laptop": 10, "Mouse": 25, "Keyboard": 15}
    }
}

MAX_TRANSFER = 10

# Step 1: Calculate surplus and shortage
surplus = {}
shortage = {}

for branch, data in branches.items():
    for item, target in data["target"].items():
        current = data["stock"].get(item, 0)
        difference = current - target

        if difference > 0:
            surplus.setdefault(item, []).append(
                [branch, difference]
            )
        elif difference < 0:
            shortage.setdefault(item, []).append(
                [branch, -difference]
            )

# Step 2: Display surplus and shortage
print("=== SURPLUS STOCK ===")
for item, entries in surplus.items():
    for branch, quantity in entries:
        print(f"{branch} - {item}: {quantity} units")

print("\n=== SHORTAGE STOCK ===")
for item, entries in shortage.items():
    for branch, quantity in entries:
        print(f"{branch} - {item}: {quantity} units")

# Step 3: Generate transfers
print("\n=== TRANSFER REPORT ===")
transfers = []

for item in shortage:
    available = surplus.get(item, [])
    required = shortage[item]

    for receiver in required:
        receiver_branch, needed = receiver

        for donor in available:
            donor_branch, extra = donor

            if needed <= 0:
                break

            if extra <= 0 or donor_branch == receiver_branch:
                continue

            quantity = min(needed, extra, MAX_TRANSFER)

            if quantity > 0:
                transfers.append(
                    (item, donor_branch, receiver_branch, quantity)
                )

                donor[1] -= quantity
                receiver[1] -= quantity
                needed -= quantity

                branches[donor_branch]["stock"][item] -= quantity
                branches[receiver_branch]["stock"][item] += quantity

                print(
                    f"{item}: {donor_branch} -> {receiver_branch} "
                    f"({quantity} units)"
                )

# Step 4: Display remaining shortages
print("\n=== REMAINING SHORTAGES ===")
remaining = False

for item, entries in shortage.items():
    for branch, quantity in entries:
        if quantity > 0:
            print(f"{branch} - {item}: {quantity} units")
            remaining = True

if not remaining:
    print("All shortages have been fulfilled.")

# Step 5: Display final stock
print("\n=== FINAL BRANCH STOCK ===")
for branch, data in branches.items():
    print(f"\n{branch}:")
    for item, quantity in data["stock"].items():
        print(f"  {item}: {quantity} units")
