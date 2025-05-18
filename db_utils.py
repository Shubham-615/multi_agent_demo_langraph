import sqlite3
from datetime import datetime

DB_PATH = "db/game_stats.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_game_stats (
        session_id TEXT PRIMARY KEY,
        total_games_played INTEGER,
        word_game_count INTEGER,
        number_game_count INTEGER,
        last_played TIMESTAMP
    )
    """)
    conn.commit()
    conn.close()

def upsert_user_stats(session_id, total_games, word_count, number_count):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    now = datetime.now().isoformat()
    cursor.execute("""
    INSERT INTO user_game_stats (session_id, total_games_played, word_game_count, number_game_count, last_played)
    VALUES (?, ?, ?, ?, ?)
    ON CONFLICT(session_id) DO UPDATE SET
        total_games_played=excluded.total_games_played,
        word_game_count=excluded.word_game_count,
        number_game_count=excluded.number_game_count,
        last_played=excluded.last_played
    """, (session_id, total_games, word_count, number_count, now))
    conn.commit()
    conn.close()
