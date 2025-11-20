import sqlite3

DB_NAME = "users.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            role TEXT,
            status TEXT
        )"""
    )

    # Create default admin if not exists
    c.execute("SELECT * FROM users WHERE username='admin'")
    if not c.fetchone():
        c.execute(
            "INSERT INTO users (username, password, role, status) VALUES (?, ?, ?, ?)",
            ("admin", "admin123", "admin", "active")
        )
    conn.commit()
    conn.close()


def add_user(username, password, role="user"):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        "INSERT INTO users (username, password, role, status) VALUES (?, ?, ?, ?)",
        (username, password, role, "active")
    )
    conn.commit()
    conn.close()


def get_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute(
        "SELECT username, role, status FROM users WHERE username=? AND password=?",
        (username, password)
    )
    result = c.fetchone()
    conn.close()
    return result


def get_all_users():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT username, role, status FROM users")
    result = c.fetchall()
    conn.close()
    return result


def update_status(username, status):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE users SET status=? WHERE username=?", (status, username))
    conn.commit()
    conn.close()
