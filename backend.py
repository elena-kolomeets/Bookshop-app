import sqlite3


def create_table():
    conn = sqlite3.connect('bookshop.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS bookshop (title TEXT, author TEXT, year TEXT, isbn TEXT)")
    conn.commit()
    conn.close()


def view_table():
    conn = sqlite3.connect('bookshop.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookshop")
    books = cur.fetchall()
    conn.close()
    return books


def search_in_table(title, author, year, isbn):
    conn = sqlite3.connect('bookshop.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM bookshop WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    books = cur.fetchall()
    conn.close()
    return books


def add_to_table(title, author, year, isbn):
    conn = sqlite3.connect('bookshop.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO bookshop VALUES (?,?,?,?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


def update_table(title, author, year, isbn, title1, author1, year1, isbn1):
    conn = sqlite3.connect('bookshop.db')
    cur = conn.cursor()
    cur.execute("UPDATE bookshop SET title=?, author=?, year=?, isbn=? WHERE title=? AND author=? AND year=? AND isbn=?"
                , (title1, author1, year1, isbn1, title, author, year, isbn))
    conn.commit()
    conn.close()


def delete_selected(title, author, year, isbn):
    conn = sqlite3.connect('bookshop.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM bookshop WHERE title=? AND author=? AND year=? AND isbn=?", (title, author, year, isbn))
    conn.commit()
    conn.close()


create_table()
