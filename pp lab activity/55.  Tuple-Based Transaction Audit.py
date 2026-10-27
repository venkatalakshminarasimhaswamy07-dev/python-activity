
# Tuple-Based Transaction Audit

transactions = [
    ("T101", 500, "CREDIT"),
    ("T102", 200, "DEBIT"),
    ("T103", -100, "CREDIT"),
    ("T101", 300, "DEBIT"),
    ("T104", 15000, "DEBIT"),
    ("T105", 0, "CREDIT"),
    ("T106", 700, "TRANSFER")
]

seen_ids = set()
previous_type = None

print("TRANSACTION AUDIT REPORT")
print("-" * 50)

for transaction in transactions:
    trans_id, amount, trans_type = transaction
    errors = []

    # Check duplicate transaction ID
    if trans_id in seen_ids:
        errors.append("Duplicate ID")
    else:
        seen_ids.add(trans_id)

    # Check invalid amount
    if amount <= 0:
        errors.append("Invalid amount")

    # Check transaction type
    if trans_type not in ("CREDIT", "DEBIT"):
        errors.append("Invalid transaction type")

    # Check suspicious sequence
    if previous_type == "DEBIT" and trans_type == "DEBIT":
        errors.append("Suspicious consecutive debits")

    # Display result
    if errors:
        print(trans_id, "->", ", ".join(errors))
    else:
        print(trans_id, "-> Valid transaction")

    previous_type = trans_type

print("-" * 50)
print("Audit completed.")
