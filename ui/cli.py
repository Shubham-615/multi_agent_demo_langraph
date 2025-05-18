import random

def generate_session_id():
    return str(random.randint(100000, 999999))  # 6-digit

def run_cli_ui(graph):
    # Generate  ID once
    session_id = generate_session_id()
    print(f"Session id : {session_id}")

    state = {
        "session_id": session_id,
        "current_game": None,
        "number_game_count": 0,
        "word_game_count": 0,
        "total_games_played": 0,
    }

    while True:
        state = graph.invoke(state)


