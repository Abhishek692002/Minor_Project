import sqlite3

# Create table if not exists
def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT,
                    name TEXT
                )''')
    conn.commit()
    conn.close()

def add_user(username, password, name):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password, name) VALUES (?, ?, ?)",
                  (username, password, name))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return False
    conn.close()
    return True

def get_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT name, username FROM users WHERE username=? AND password=?",
              (username, password))
    result = c.fetchone()
    conn.close()
    return result
