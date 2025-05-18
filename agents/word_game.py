import random

WORD_LIST = ["apple", "chair", "elephant", "guitar", "rocket", "pencil", "tiger"]

# define properties for each word
WORD_FACTS = {
    "apple":     [ "yes", "no",  "no",  "no",  "no" ],
    "chair":     [ "no",  "no",  "yes", "no",  "no" ],
    "elephant":  [ "no",  "yes", "no",  "yes", "yes"],
    "guitar":    [ "no",  "no",  "no",  "no",  "yes"],
    "rocket":    [ "no",  "no",  "no",  "yes", "yes"],
    "pencil":    [ "no",  "no",  "yes", "no",  "no" ],
    "tiger":     [ "no",  "yes", "no",  "yes", "yes"]
}

CLUES = [
    "Is it something you can eat?",
    "Is it an animal?",
    "Is it used in a classroom?",
    "Is it bigger than a car?",
    "Does it make sound?"
]

def word_game_agent(state):
    print("\n🤫 Pick a word from the list (in your mind):")
    print(", ".join(WORD_LIST))
    print("I'll ask 5 questions... answer with yes/no/maybe\n")

    possible_words = WORD_LIST.copy()

    for i, question in enumerate(CLUES):
        print(f"Q{i+1}: {question}")
        answer = input("> ").strip().lower()

        # Filter based on user response
        possible_words = [
            word for word in possible_words
            if WORD_FACTS[word][i] == answer or answer == "maybe"
        ]

        if not possible_words:
            print("\n🛑 Hmm... your answers don't match any known word.")
            print("Let's go back to the main menu.")
            return "game_selector", state

    print("\n🧠 Thinking...")
    guess = random.choice(possible_words)
    print(f"Is your word '{guess}'?")

    user_response = input("(yes/no): ").strip().lower()
    state["word_game_count"] += 1
    state["total_games_played"] += 1
    state["current_game"] = None

    if user_response == "yes":
        print("🎉 Yay! I guessed it right!")
    else:
        print("😢 I guessed wrong. Maybe next time!")

    # Update state
    state["word_game_count"] += 1
    state["total_games_played"] += 1
    state["current_game"] = None

    # return for LangGraph
    return {
        "__next__": "game_selector",
        **state
    }
