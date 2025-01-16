internal_records = {
    "TXN001": 500,
    "TXN002": 1200,
    "TXN003": 300,
    "TXN004": 700,
}

external_records = {
    "TXN001": 500,
    "TXN002": 1200,
    "TXN003": 350,  # Mismatch
    "TXN005": 900,  # Extra transaction in external
}

# Reconciliation logic
missing_in_external = {}
missing_in_internal = {}
mismatched_transactions = {}

# Check for differences
for txn_id, amount in internal_records.items():
    if txn_id not in external_records:
        missing_in_external[txn_id] = amount
    elif amount != external_records[txn_id]:
        mismatched_transactions[txn_id] = {
            "Internal": amount,
            "External": external_records[txn_id],
        }

for txn_id, amount in external_records.items():
    if txn_id not in internal_records:
        missing_in_internal[txn_id] = amount

# Output results
print("Missing in External Records:")
for txn_id, amount in missing_in_external.items():
    print(f"  {txn_id}: ${amount}")

print("\nMissing in Internal Records:")
for txn_id, amount in missing_in_internal.items():
    print(f"  {txn_id}: ${amount}")

print("\nMismatched Transactions:")
for txn_id, amounts in mismatched_transactions.items():
    print(f"  {txn_id}: Internal=${amounts['Internal']} External=${amounts['External']}")

# Totals for comparison
internal_total = sum(internal_records.values())
external_total = sum(external_records.values())
difference = internal_total - external_total

print(f"\nInternal Total: ${internal_total}")
print(f"External Total: ${external_total}")
print(f"Difference: ${difference}")
