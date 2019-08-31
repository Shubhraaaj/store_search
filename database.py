import sqlite3

def connect():
    conn = sqlite3.connect("dictionary.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS dict (id INTEGER PRIMARY KEY, word TEXT)")
    conn.commit()
    conn.close()

def insert(word):
    conn = sqlite3.connect("dictionary.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO dict VALUES (NULL,?)", (word,))
    conn.commit()
    conn.close()

def search(word=""):
    conn = sqlite3.connect("dictionary.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM dict WHERE word=?", (word,))
    rows = cur.fetchall()
    conn.close()
    return rows

def clearAll():
    conn = sqlite3.connect("dictionary.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM dict")
    conn.commit()
    conn.close()

connect()
