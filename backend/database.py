# database.py
import sqlite3

DB = "database.db"

def init_data_tables():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS farms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        area REAL,
        lat REAL,
        lon REAL
    )
    """)

    conn.commit()
    conn.close()

def add_farm(name, area, lat, lon):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO farms (name, area, lat, lon) VALUES (?, ?, ?, ?)",
              (name, area, lat, lon))
    conn.commit()
    conn.close()

def get_farms():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT * FROM farms")
    data = c.fetchall()
    conn.close()
    return data