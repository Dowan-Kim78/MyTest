import random

def monty_hall_simulation(num_trials=10000, switch=True):
    """
    Simulate the Monty Hall problem.

    Args:
        num_trials (int): Number of simulations to run.
        switch (bool): Whether the player switches doors.

    Returns:
        float: Probability of winning by chosen strategy.
    """
    wins = 0
    for _ in range(num_trials):
        # Randomly place the car behind one of the 3 doors
        car = random.randint(0, 2)
        # Player makes a random choice
        choice = random.randint(0, 2)
        # Host opens a door that is not the car and not the player's choice
        possible_doors = [i for i in range(3) if i != choice and i != car]
        host_opens = random.choice(possible_doors)
        # If player switches, pick the remaining unopened door
        if switch:
            remaining = [i for i in range(3) if i != choice and i != host_opens][0]
            final_choice = remaining
        else:
            final_choice = choice
        if final_choice == car:
            wins += 1
    return wins / num_trials

if __name__ == "__main__":
    trials = 10000
    win_rate_switch = monty_hall_simulation(trials, switch=True)
    win_rate_stay = monty_hall_simulation(trials, switch=False)
    print(f"Switching: Win rate = {win_rate_switch:.2%}")
    print(f"Staying: Win rate = {win_rate_stay:.2%}")