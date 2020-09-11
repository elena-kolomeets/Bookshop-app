""""
A desktop database app that stores this book information:
Title, Author, Year, ISBN

User can view all records, search, add, update and delete an entry,
clear the view, save the data in the text file,
get hints with help buttons
"""

import tkinter as tk
from tkinter import messagebox
from backend_OOP import Database

database = Database('bookshop.db')


class Window:
    def __init__(self, window):
        self.window = window
        self.window.option_add("*Font", ('Times New Roman', 12))
        self.window.option_add("*Background", 'white')
        self.window.title('Bookshop')
        self.window.iconbitmap(r'books.ico')
        self.window.resizable(0, 0)
        self.window.configure(background='white')

        self.title_text = tk.StringVar()
        self.entry_title = tk.Entry(window, textvariable=self.title_text, width=25)
        self.entry_title.grid(row=0, column=1, sticky=tk.W)

        self.author_text = tk.StringVar()
        self.entry_author = tk.Entry(window, textvariable=self.author_text, width=25)
        self.entry_author.grid(row=0, column=3, sticky=tk.W, padx=5)

        self.year_text = tk.StringVar()
        self.entry_year = tk.Entry(window, textvariable=self.year_text, width=25)
        self.entry_year.grid(row=1, column=1, sticky=tk.W)

        self.isbn_text = tk.StringVar()
        self.entry_isbn = tk.Entry(window, textvariable=self.isbn_text, width=25)
        self.entry_isbn.grid(row=1, column=3, sticky=tk.W, padx=5)

        self.label_title = tk.Label(window, text='Title')
        self.label_title.grid(row=0, column=0, sticky=tk.E, padx=5)

        self.label_author = tk.Label(window, text='Author')
        self.label_author.grid(row=0, column=2, sticky=tk.E)

        self.label_year = tk.Label(window, text='Year')
        self.label_year.grid(row=1, column=0, sticky=tk.E, padx=5)

        self.label_isbn = tk.Label(window, text='ISBN')
        self.label_isbn.grid(row=1, column=2, sticky=tk.E)

        self.label_credits = tk.Label(window, text='Made by Elena Kolomeets, September 2020',
                                      font=['Times New Roman', 10], foreground='white')
        self.label_credits.grid(row=9, column=1, columnspan=2, sticky=tk.SW)

        self.box = tk.Listbox(window, height=12, width=50)
        self.box.grid(row=1, column=1, rowspan=9, columnspan=2, sticky=tk.E)

        self.scroll_y = tk.Scrollbar(window)
        self.scroll_y.grid(row=1, column=3, rowspan=9, ipady=96, sticky=tk.W)

        self.box.configure(yscrollcommand=self.scroll_y.set)
        self.scroll_y.configure(command=self.box.yview)

        self.scroll_x = tk.Scrollbar(window, orient=tk.HORIZONTAL)
        self.scroll_x.grid(row=8, column=1, columnspan=2, ipadx=177, sticky=tk.S)

        self.box.configure(xscrollcommand=self.scroll_x.set)
        self.scroll_x.configure(command=self.box.xview)

        self.button_view = tk.Button(window, text='View All', width=12, command=self.fbutton_view)
        self.button_view.grid(row=2, column=3, pady=5)

        self.button_search = tk.Button(window, text='Search Entry', width=12, command=self.fbutton_search)
        self.button_search.grid(row=3, column=3)

        self.button_add = tk.Button(window, text='Add Entry', width=12, command=self.fbutton_add)
        self.button_add.grid(row=4, column=3, pady=5)

        self.button_update = tk.Button(window, text='Update Selected', width=12, command=self.fbutton_update)
        self. button_update.grid(row=5, column=3)

        self. button_delete = tk.Button(window, text='Delete Selected', width=12, command=self.fbutton_delete)
        self.button_delete.grid(row=6, column=3, pady=5)

        self.button_clear = tk.Button(window, text='Clear All', width=12, command=self.fbutton_clear)
        self.button_clear.grid(row=7, column=3)

        self.button_save = tk.Button(window, text='Save in File', width=12, command=self.fbutton_save)
        self.button_save.grid(row=8, column=3, pady=5)

        self.button_popup_search = tk.Button(window, text='?', command=self.popup_search)
        self.button_popup_search.grid(row=3, column=3, sticky=tk.E, padx=10)

        self.button_popup_add = tk.Button(window, text='?', command=self.popup_add)
        self.button_popup_add.grid(row=4, column=3, sticky=tk.E, padx=10)

        self.button_popup_update = tk.Button(window, text='?', command=self.popup_update)
        self.button_popup_update.grid(row=5, column=3, sticky=tk.E, padx=10)

        self.button_popup_save = tk.Button(window, text='?', command=self.popup_save)
        self.button_popup_save.grid(row=8, column=3, sticky=tk.E, padx=10)

    def fbutton_view(self):
        self.box.delete(0, tk.END)
        books = database.view_table()
        if books:
            for book in books:
                self.box.insert(tk.END, '  '.join(book))
        else:
            messagebox.showinfo('Oops!', 'No entries to show')

    def fbutton_search(self):
        if self.title_text.get() != '' or self.author_text.get() != '' or self.year_text.get() != '' \
                or self.isbn_text.get() != '':
            self.box.delete(0, tk.END)
            title = self.title_text.get().title()
            author = self.author_text.get().title()
            year = self.year_text.get().title()
            isbn = self.isbn_text.get().title()
            books = database.search_in_table(title, author, year, isbn)
            self.entry_title.delete(0, tk.END)
            self.entry_author.delete(0, tk.END)
            self.entry_year.delete(0, tk.END)
            self.entry_isbn.delete(0, tk.END)
            if books:
                for book in books:
                    self.box.insert(tk.END, '  '.join(book))
            else:
                messagebox.showinfo('Oops!', 'No entry found')
        else:
            messagebox.showinfo('Hint', 'Please enter one book credential')

    def entry_check(self):
        if self.title_text.get() == '' or self.author_text.get() == '' or self.year_text.get() == '' \
                or self.isbn_text.get() == '':
            messagebox.showinfo('Hint', "Please enter new book credentials or '-'")
        if self.title_text.get() != '' and self.author_text.get() != '' and self.year_text.get() != '' \
                and self.isbn_text.get() != '':
            return True
        else:
            return False

    def fbutton_add(self):
        if self.entry_check():
            title = self.title_text.get().title()
            author = self.author_text.get().title()
            year = self.year_text.get().title()
            isbn = self.isbn_text.get().title()
            database.add_to_table(title, author, year, isbn)
            self.entry_title.delete(0, tk.END)
            self.entry_author.delete(0, tk.END)
            self.entry_year.delete(0, tk.END)
            self.entry_isbn.delete(0, tk.END)
            self.fbutton_view()

    def fbutton_update(self):
        if self.box.curselection():
            if self.title_text.get() != '' or self.author_text.get() != '' or self.year_text.get() != '' \
                    or self.isbn_text.get() != '':
                item = self.box.get(tk.ACTIVE)
                item = item.split('  ')
                title = item[0]
                author = item[1]
                year = item[2]
                isbn = item[3]
                if self.title_text.get():
                    title1 = self.title_text.get().title()
                else:
                    title1 = item[0]
                if self.author_text.get():
                    author1 = self.author_text.get().title()
                else:
                    author1 = item[1]
                if self.year_text.get():
                    year1 = self.year_text.get()
                else:
                    year1 = item[2]
                if self.isbn_text.get():
                    isbn1 = self.isbn_text.get()
                else:
                    isbn1 = item[3]
                database.update_table(title, author, year, isbn, title1, author1, year1, isbn1)
                self.box.delete(0, tk.END)
                self.entry_title.delete(0, tk.END)
                self.entry_author.delete(0, tk.END)
                self.entry_year.delete(0, tk.END)
                self.entry_isbn.delete(0, tk.END)
                self.fbutton_view()
        else:
            messagebox.showinfo('Oops!', 'Nothing is selected')

    def fbutton_delete(self):
        if self.box.curselection():
            item = self.box.get(tk.ACTIVE)
            item = item.split('  ')
            title = item[0]
            author = item[1]
            year = item[2]
            isbn = item[3]
            self.box.delete(tk.ACTIVE)
            database.delete_selected(title, author, year, isbn)
        else:
            messagebox.showinfo('Oops!', 'Nothing is selected')

    def fbutton_clear(self):
        self.box.delete(0, tk.END)

    def fbutton_save(self):
        if self.box.get(0, tk.END):
            with open('books.txt', mode='w', encoding='utf-8') as myfile:
                myfile.write('Title  Author  Year  ISBN')
                for line in self.box.get(0, tk.END):
                    myfile.write('\n' + line)
            messagebox.showinfo('Success!', 'Your data is saved in "books.txt" file')
        else:
            messagebox.showinfo('Oops!', 'No entries to save')

    def popup_search(self):
        messagebox.showinfo('Hint', 'Please enter one book credential (case insensitive) and press button "Search '
                                    'Entry".')

    def popup_add(self):
        messagebox.showinfo('Hint', 'Please enter book credentials (case insensitive) or "-" and press button '
                                    '"Add Entry".')

    def popup_update(self):
        messagebox.showinfo('Hint', 'Please select an item, enter new book credential(s) and press button '
                                    '"Update Selected".')

    def popup_save(self):
        messagebox.showinfo('Hint', 'To save the displayed data into the text file please push the button "Save in '
                                    'File".')


window = tk.Tk()
Window(window)
window.mainloop()
