import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS bookshop (title TEXT, author TEXT, year TEXT, isbn TEXT)")
        self.conn.commit()

    def view_table(self):
        self.cur.execute("SELECT * FROM bookshop")
        books = self.cur.fetchall()
        return books

    def search_in_table(self, title, author, year, isbn):
        self.cur.execute("SELECT * FROM bookshop WHERE title=? OR author=? OR year=? OR isbn=?",
                         (title, author, year, isbn))
        books = self.cur.fetchall()
        return books

    def add_to_table(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO bookshop VALUES (?,?,?,?)", (title, author, year, isbn))
        self.conn.commit()

    def update_table(self, title, author, year, isbn, title1, author1, year1, isbn1):
        self.cur.execute("UPDATE bookshop SET title=?, author=?, year=?, isbn=? WHERE title=? AND author=? AND year=? "
                         "AND isbn=?", (title1, author1, year1, isbn1, title, author, year, isbn))
        self.conn.commit()

    def delete_selected(self, title, author, year, isbn):
        self.cur.execute("DELETE FROM bookshop WHERE title=? AND author=? AND year=? AND isbn=?",
                         (title, author, year, isbn))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
