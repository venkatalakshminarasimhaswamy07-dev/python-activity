
# Multi-Route Courier Dispatch Planning

packages = [
    [101, 10, "A", "High"],
    [102, 20, "B", "Medium"],
    [103, 15, "A", "High"],
    [104, 30, "C", "Low"],
    [105, 25, "B", "High"],
    [106, 50, "D", "Medium"]
]

vehicles = {
    "V1": {"capacity": 40, "zones": ["A", "B"]},
    "V2": {"capacity": 50, "zones": ["B", "C"]},
    "V3": {"capacity": 30, "zones": ["A", "C"]}
}

priority = {"High": 1, "Medium": 2, "Low": 3}

packages.sort(key=lambda p: priority[p[3]])

dispatch = {"V1": [], "V2": [], "V3": []}
remaining = {"V1": 40, "V2": 50, "V3": 30}
undispatched = []

for p in packages:
    package_id, weight, zone, level = p
    assigned = False

    for vid in vehicles:
        if (zone in vehicles[vid]["zones"]
                and weight <= remaining[vid]):

            dispatch[vid].append(p)
            remaining[vid] -= weight
            assigned = True
            break

    if not assigned:
        undispatched.append(p)

print("COURIER DISPATCH REPORT")

for vid in vehicles:
    print("\nVehicle:", vid)
    print("Packages assigned:")

    if len(dispatch[vid]) == 0:
        print("No packages")
    else:
        for p in dispatch[vid]:
            print("ID:", p[0], "Weight:", p[1],
                  "Zone:", p[2], "Priority:", p[3])

    print("Remaining capacity:", remaining[vid], "kg")

print("\nUNDISPATCHED PACKAGES")

if len(undispatched) == 0:
    print("All packages dispatched")
else:
    for p in undispatched:
        print("ID:", p[0], "Weight:", p[1],
              "Zone:", p[2], "Priority:", p[3])

print("\nTotal packages:", len(packages))
print("Dispatched:", len(packages) - len(undispatched))
print("Undispatched:", len(undispatched))
