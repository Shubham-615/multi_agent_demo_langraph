
import sys
from db_utils import upsert_user_stats

def game_selector_agent(state):
    print("\n--- Main Menu ---")
    print("1: Number Guessing Game")
    print("2: Word Clue Guesser")
    print("3: Exit")

    choice = input("Enter choice (1-3): ").strip()

    if choice == "1":
        state["current_game"] = "number"
    elif choice == "2":
        state["current_game"] = "word"
    elif choice == "3":
        print("👋 Goodbye!")
        print(f"🧾 You({state['session_id']}) played {state['word_game_count']} word game(s) and {state['number_game_count']} number game(s).")

        # Save stats before exit
        upsert_user_stats(
            session_id=state.get("session_id", "unknown"),
            total_games=state.get("total_games_played", 0),
            word_count=state.get("word_game_count", 0),
            number_count=state.get("number_game_count", 0),
        )
        sys.exit(0)

    else:
        print("\n⚠️ Invalid choice.")
        print(f"🧾 You({state['session_id']}) played {state['word_game_count']} word game(s) and {state['number_game_count']} number game(s).")

        # Save stats before exit
        upsert_user_stats(
            session_id=state.get("session_id", "unknown"),
            total_games=state.get("total_games_played", 0),
            word_count=state.get("word_game_count", 0),
            number_count=state.get("number_game_count", 0),
        )
        sys.exit(0)

    return state