
from langgraph.graph import StateGraph
from typing import TypedDict, Optional
from agents.game_selector import game_selector_agent
from agents.number_game import number_game_agent
from agents.word_game import word_game_agent

class GameState(TypedDict):
    current_game: Optional[str]
    number_game_count: int
    word_game_count: int
    total_games_played: int
    session_id: int

def build_game_graph():
    builder = StateGraph(state_schema=GameState)

    builder.add_node("game_selector", game_selector_agent)
    builder.add_node("number_game", number_game_agent)
    builder.add_node("word_game", word_game_agent)

    builder.set_entry_point("game_selector")

    def route_games(state: GameState) -> str:
        if state["current_game"] == "number":
            return "number_game"
        elif state["current_game"] == "word":
            return "word_game"
        else:
            return "game_selector"

    builder.add_conditional_edges("game_selector", route_games)
    builder.add_edge("number_game", "game_selector")
    builder.add_edge("word_game", "game_selector")

    return builder.compile()
