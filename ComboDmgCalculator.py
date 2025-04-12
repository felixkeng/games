def calculate_avg_dmg(max_combos, combo_rate):
    # Basic attack always deals 1 damage
    base_dmg = 1
    # Expected additional damage from combos
    # Each combo has combo_rate chance to trigger, up to max_combos
    expected_combo_dmg = 0
    for i in range(max_combos):
        # Probability of reaching this combo (combo_rate for each prior success)
        prob = combo_rate ** i
        # Probability of triggering this combo (and not beyond)
        trigger_prob = prob * combo_rate
        # Damage contribution (1 damage per combo)
        expected_combo_dmg += trigger_prob * 1
    
    return base_dmg + expected_combo_dmg

def main():
    print("Combat Damage Calculator")
    print("Note: Basic attack and combos each deal 1 damage")
    
    # Get max combos
    while True:
        try:
            max_combos = int(input("Enter maximum number of combos (positive integer): "))
            if max_combos > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid integer.")
    
    # Get combo rate
    while True:
        try:
            combo_rate = float(input("Enter combo trigger rate (0 to 1, e.g., 0.5 for 50%): "))
            if 0 <= combo_rate <= 1:
                break
            print("Please enter a number between 0 and 1.")
        except ValueError:
            print("Please enter a valid number.")
    
    # Calculate and display average damage
    avg_dmg = calculate_avg_dmg(max_combos, combo_rate)
    print(f"\nAverage damage per round: {avg_dmg:.4f}")

if __name__ == "__main__":
    main()