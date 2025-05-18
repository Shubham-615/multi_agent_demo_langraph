# project structure:
# - main.py
# - db_utils.py
# - core/graph.py
# - agents/game_selector.py
# - agents/number_game.py
# - agents/word_game.py
# - ui/cli.py
# - db/game_stat.db
# - requirements.txt

# -------------------------------------------------------------------------------

from core.graph import build_game_graph
from ui.cli import run_cli_ui
from db_utils import init_db

if __name__ == "__main__":
    init_db()
    print("\n🎮 Welcome to the Multi-Agent Game Hub! 🎮")
    graph = build_game_graph()
    run_cli_ui(graph)
