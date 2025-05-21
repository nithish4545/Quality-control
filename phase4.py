# quality_control.py

# Sample data: Measurements from a manufacturing batch
# (could be from sensors, database, etc.)
batch_measurements = [10.1, 9.9, 10.3, 10.0, 9.7, 10.5, 10.2, 9.6, 10.1]

# Tolerance limits (e.g., for product weight in grams)
lower_tolerance = 9.8
upper_tolerance = 10.2

def check_quality(batch, lower, upper):
    """
    Checks each measurement in the batch to see if it falls within the specified tolerance limits.
    
    Parameters:
        batch (list): List of measurements.
        lower (float): Lower tolerance limit.
        upper (float): Upper tolerance limit.
    
    Returns:
        tuple: Two lists containing passed and failed items.
    """
    passed = []
    failed = []
    
    for index, measurement in enumerate(batch):
        if lower <= measurement <= upper:
            passed.append((index + 1, measurement))  # Store item number and value
        else:
            failed.append((index + 1, measurement))  # Store item number and value
    
    return passed, failed

# Run quality control
passed_items, failed_items = check_quality(batch_measurements, lower_tolerance, upper_tolerance)

# Output results
print("Quality Control Report")
print("-" * 30)
print(f"Total items checked: {len(batch_measurements)}")
print(f"Passed: {len(passed_items)}")
print(f"Failed: {len(failed_items)}\n")

if failed_items:
    print("Defective Items:")
    for idx, val in failed_items:
        print(f"Item {idx}: {val} (OUT OF TOLERANCE)")
else:
    print("All items passed quality control.")
