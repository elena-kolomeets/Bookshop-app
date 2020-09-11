""""
A desktop database app that stores this book information:
Title, Author, Year, ISBN

User can view all records, search, add, update and delete an entry,
clear the view, save the data in the text file,
get hints with help buttons
"""

import tkinter as tk
from tkinter import messagebox
import backend as be

window = tk.Tk()
window.option_add("*Font", ('Times New Roman', 12))
window.title('Bookshop')
window.iconbitmap(r'books.ico')
window.resizable(0, 0)


def fbutton_view():
    box.delete(0, tk.END)
    books = be.view_table()
    if books:
        for book in books:
            box.insert(tk.END, '  '.join(book))


def fbutton_search():
    if title_text.get() != '' or author_text.get() != '' or year_text.get() != '' or isbn_text.get() != '':
        box.delete(0, tk.END)
        title = title_text.get().title()
        author = author_text.get().title()
        year = year_text.get().title()
        isbn = isbn_text.get().title()
        books = be.search_in_table(title, author, year, isbn)
        entry_title.delete(0, tk.END)
        entry_author.delete(0, tk.END)
        entry_year.delete(0, tk.END)
        entry_isbn.delete(0, tk.END)
        if books:
            for book in books:
                box.insert(tk.END, '  '.join(book))
        else:
            messagebox.showinfo('Oops!', 'No entry found')
    else:
        messagebox.showinfo('Hint', 'Please enter one book credential')


def entry_check():
    if title_text.get() == '' or author_text.get() == '' or year_text.get() == '' or isbn_text.get() == '':
        messagebox.showinfo('Hint', "Please enter new book credentials or '-'")
    if title_text.get() != '' and author_text.get() != '' and year_text.get() != '' and isbn_text.get() != '':
        return True
    else:
        return False


def fbutton_add():
    if entry_check():
        title = title_text.get().title()
        author = author_text.get().title()
        year = year_text.get().title()
        isbn = isbn_text.get().title()
        be.add_to_table(title, author, year, isbn)
        entry_title.delete(0, tk.END)
        entry_author.delete(0, tk.END)
        entry_year.delete(0, tk.END)
        entry_isbn.delete(0, tk.END)


def fbutton_update():
    if box.curselection():
        if title_text.get() != '' or author_text.get() != '' or year_text.get() != '' or isbn_text.get() != '':
            item = box.get(tk.ACTIVE)
            item = item.split('  ')
            title = item[0]
            author = item[1]
            year = item[2]
            isbn = item[3]
            if title_text.get():
                title1 = title_text.get().title()
            else:
                title1 = item[0]
            if author_text.get():
                author1 = author_text.get().title()
            else:
                author1 = item[1]
            if year_text.get():
                year1 = year_text.get()
            else:
                year1 = item[2]
            if isbn_text.get():
                isbn1 = isbn_text.get()
            else:
                isbn1 = item[3]
            be.update_table(title, author, year, isbn, title1, author1, year1, isbn1)
            box.delete(0, tk.END)
            entry_title.delete(0, tk.END)
            entry_author.delete(0, tk.END)
            entry_year.delete(0, tk.END)
            entry_isbn.delete(0, tk.END)
            fbutton_view()
    else:
        messagebox.showinfo('Oops!', 'Nothing is selected')


def fbutton_delete():
    if box.curselection():
        item = box.get(tk.ACTIVE)
        item = item.split('  ')
        title = item[0]
        author = item[1]
        year = item[2]
        isbn = item[3]
        box.delete(tk.ACTIVE)
        be.delete_selected(title, author, year, isbn)
    else:
        messagebox.showinfo('Oops!', 'Nothing is selected')


def fbutton_clear():
    box.delete(0, tk.END)


def fbutton_save():
    if box.get(0, tk.END):
        with open('my_books.txt', mode='w', encoding='utf-8') as myfile:
            myfile.write('Title  Author  Year  ISBN')
            for line in box.get(0, tk.END):
                myfile.write('\n' + line)
        messagebox.showinfo('Success!', 'Your data is saved in "my_books.txt" file')


def popup_search():
    top = tk.Toplevel(window)
    top.iconbitmap(r'question.ico')
    top.resizable(0, 0)
    x_y = (button_search.winfo_x() + 40, button_search.winfo_y() + 30)
    top.geometry('+%s+%s' % x_y)
    message = tk.Message(top, text='Please enter one book credential (case insensitive) and press button '
                                   '"Add Entry".')
    message.pack(pady=10)
    ok = tk.Button(top, text='Got it!', command=top.destroy)
    ok.pack(pady=10)


def popup_add():
    top = tk.Toplevel(window)
    top.iconbitmap(r'question.ico')
    top.resizable(0, 0)
    x_y = (button_add.winfo_x() + 40, button_add.winfo_y() + 10)
    top.geometry('+%s+%s' % x_y)
    message = tk.Message(top, text='Please enter book credential (case insensitive) and press button '
                                   '"Search Entry".')
    message.pack(pady=10)
    ok = tk.Button(top, text='Got it!', command=top.destroy)
    ok.pack(pady=10)


def popup_update():
    top = tk.Toplevel(window)
    top.iconbitmap(r'question.ico')
    top.resizable(0, 0)
    x_y = (button_update.winfo_x() + 40, button_update.winfo_y() + 10)
    top.geometry('+%s+%s' % x_y)
    message = tk.Message(top, text='Please select an item, enter new book credential(s) and press button '
                                   '"Update Selected".')
    message.pack(pady=10)
    ok = tk.Button(top, text='Got it!', command=top.destroy)
    ok.pack(pady=10)


def popup_save():
    top = tk.Toplevel(window)
    top.iconbitmap(r'question.ico')
    top.resizable(0, 0)
    x_y = (button_save.winfo_x() + 40, button_save.winfo_y() + 10)
    top.geometry('+%s+%s' % x_y)
    message = tk.Message(top, text='To save the displayed data as a text file please push the button "Save in File".')
    message.pack(pady=10)
    ok = tk.Button(top, text='Got it!', command=top.destroy)
    ok.pack(pady=10)


title_text = tk.StringVar()
entry_title = tk.Entry(window, textvariable=title_text, width=25)
entry_title.grid(row=0, column=1, sticky=tk.W)

author_text = tk.StringVar()
entry_author = tk.Entry(window, textvariable=author_text, width=25)
entry_author.grid(row=0, column=3, sticky=tk.W, padx=5)

year_text = tk.StringVar()
entry_year = tk.Entry(window, textvariable=year_text, width=25)
entry_year.grid(row=1, column=1, sticky=tk.W)

isbn_text = tk.StringVar()
entry_isbn = tk.Entry(window, textvariable=isbn_text, width=25)
entry_isbn.grid(row=1, column=3, sticky=tk.W, padx=5)

label_title = tk.Label(window, text='Title')
label_title.grid(row=0, column=0, sticky=tk.E, padx=5)

label_author = tk.Label(window, text='Author')
label_author.grid(row=0, column=2, sticky=tk.E)

label_year = tk.Label(window, text='Year')
label_year.grid(row=1, column=0, sticky=tk.E, padx=5)

label_isbn = tk.Label(window, text='ISBN')
label_isbn.grid(row=1, column=2, sticky=tk.E)

box = tk.Listbox(window, height=11, width=50)
box.grid(row=2, column=1, rowspan=8, columnspan=2, pady=5, sticky=tk.E)

scroll = tk.Scrollbar(window)
scroll.grid(row=2, column=2, rowspan=8, ipady=86, pady=5, sticky=tk.E)

# set 'scroll' as a scrollbar for the 'box' on vertical axe (y)
box.configure(yscrollcommand=scroll.set)
# set 'scroll' to change vertical (y) view of 'box'
scroll.configure(command=box.yview)

button_view = tk.Button(window, text='View All', width=12, command=fbutton_view)
button_view.grid(row=2, column=3, pady=5)

button_search = tk.Button(window, text='Search Entry', width=12, command=fbutton_search)
button_search.grid(row=3, column=3)

button_add = tk.Button(window, text='Add Entry', width=12, command=fbutton_add)
button_add.grid(row=4, column=3, pady=5)

button_update = tk.Button(window, text='Update Selected', width=12, command=fbutton_update)
button_update.grid(row=5, column=3)

button_delete = tk.Button(window, text='Delete Selected', width=12, command=fbutton_delete)
button_delete.grid(row=6, column=3, pady=5)

button_clear = tk.Button(window, text='Clear All', width=12, command=fbutton_clear)
button_clear.grid(row=7, column=3)

button_save = tk.Button(window, text='Save in File', width=12, command=fbutton_save)
button_save.grid(row=8, column=3, pady=5)

button_popup_search = tk.Button(window, text='?', command=popup_search)
button_popup_search.grid(row=3, column=3, sticky=tk.E, padx=10)

button_popup_add = tk.Button(window, text='?', command=popup_add)
button_popup_add.grid(row=4, column=3, sticky=tk.E, padx=10)

button_popup_update = tk.Button(window, text='?', command=popup_update)
button_popup_update.grid(row=5, column=3, sticky=tk.E, padx=10)

button_popup_save = tk.Button(window, text='?', command=popup_save)
button_popup_save.grid(row=8, column=3, sticky=tk.E, padx=10)

window.mainloop()
