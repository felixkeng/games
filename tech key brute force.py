import random
import time

# Define probabilities and corresponding values (in epic equivalents)
probabilities = [0.03, 0.0933, 0.2272, 0.6495]  # Sums to 1
values = [1.0, 0.125, 1/24, 1/72]  # Epic, Purple, Blue, Green

# Number of keys to simulate
num_keys = 10000

# Track runtime
start_time = time.time()

# Track history of drops to enforce guarantees
drop_history = []

# Track total value in epic equivalents
total_value = 0

# Counters for guarantee mechanics
purple_guarantee_counter = 0
epic_guarantee_counter = 0
force_purple_next = False

# Simulate num_keys
for i in range(num_keys):
    # Check for guarantees
    purple_guarantee = False
    epic_guarantee = False
    
    # Check epic guarantee (last 79 keys have no epic)
    if epic_guarantee_counter >= 59 and not force_purple_next:
        if i >= 79 and not any(drop == 1.0 for drop in drop_history[-79:]):
            epic_guarantee = True
    
    # Check purple guarantee (last 9 keys have no purple)
    if purple_guarantee_counter >= 9 and not epic_guarantee and not force_purple_next:
        if i >= 9 and not any(drop == 0.125 for drop in drop_history[-9:]):
            purple_guarantee = True
    
    # If both guarantees are triggered, prioritize epic, then purple on the next key
    if epic_guarantee and purple_guarantee_counter >= 9:
        purple_guarantee = False
        force_purple_next = True
    
    # Apply guarantees or roll normally
    if force_purple_next:
        drop_value = 0.125  # Force purple
        force_purple_next = False
    elif epic_guarantee:
        drop_value = 1.0  # Force epic
    elif purple_guarantee:
        drop_value = 0.125  # Force purple
    else:
        # Roll based on base probabilities using random.choices
        drop_value = random.choices(values, weights=probabilities, k=1)[0]
    
    # Update counters
    if drop_value == 1.0:
        epic_guarantee_counter = 0
    else:
        epic_guarantee_counter += 1
    
    if drop_value == 0.125:
        purple_guarantee_counter = 0
    else:
        purple_guarantee_counter += 1
    
    # Add to history
    drop_history.append(drop_value)
    
    # Add the drop value to total
    total_value += drop_value

# Calculate average value per key
average_value_per_key = total_value / num_keys

# Calculate average keys to get 1 epic
average_keys_for_one_epic = 1 / average_value_per_key

# Calculate runtime
runtime = time.time() - start_time

# Output results
print(f"Total value (in epic equivalents) over {num_keys} keys: {total_value:.6f}")
print(f"Average value per key: {average_value_per_key:.6f}")
print(f"Average keys to get 1 epic: {average_keys_for_one_epic:.2f}")
print(f"Runtime: {runtime:.2f} seconds")