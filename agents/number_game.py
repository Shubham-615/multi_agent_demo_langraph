def number_game_agent(state):
    print("\n🎯 Think of a number between 1 and 50 (inclusive).")
    print("I will try to guess it.")
    print("➡️ Reply 'yes' if your number is greater than my guess.")
    print("➡️ Reply 'no' if your number is less than or equal to my guess.\n")

    low, high = 1, 50
    attempts = 0

    while low < high:
        mid = (low + high) // 2
        print(f"Is your number greater than {mid}? (yes/no)")
        response = input("> ").strip().lower()
        attempts += 1

        if response == "yes":
            low = mid + 1
        elif response == "no":
            high = mid
        else:
            print("⚠️ Please respond with 'yes' or 'no'.")

    print(f"\n🎉 I guessed your number! It is {low}. Took me {attempts} attempts.")
    state["number_game_count"] += 1
    state["total_games_played"] += 1
    state["current_game"] = None
    return state
