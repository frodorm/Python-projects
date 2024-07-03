import sqlite3

def main():
    connection = sqlite3.connect('realty.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE offers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        url TEXT,
        offer_id INTEGER,
        date TEXT,
        price INTEGER,
        address TEXT,
        area INTEGER,
        floor INTEGER
        )
    """)

    connection.close()




main()