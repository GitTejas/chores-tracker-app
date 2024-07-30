import sqlite3

CONN = sqlite3.connect('chores.db')
CURSOR = CONN.cursor()
