"""
Kolton Chiu
This program uses the database novel which includes a novel name and the author,
the user will get 3 choices when the program starts. The user can view all available books,
and add new books to the database.
"""
# Imports
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sqlite3 as sq

# Identify where the database is located
con = sq.connect("noveldata.db")
c = con.cursor()

#asign writer for add novel
def joe():
    author_id = 1
    return
def jane():
    author_id = 2
    return
def john():
    author_id = 3
    return

# This functions get data from table novel, and author
def find_novel():
    res = c.execute("SELECT isbn,title,name from novel JOIN author WHERE author.authorid = novel.authorid")
    data = c.fetchall()  # Gets the data from the table
    return data

# This functions get data from author
def find_author_name():
    res = c.execute("SELECT name from author")
    data = c.fetchall()  # Gets the data from the table
    return data

# This function gets all data from the database and displays it for the user
def render_novel():
    novels = find_novel()
    tbl = "~~  isbn number   ~  novel name  ~  author's name ~~\n\n|"
    for row in novels:
        for field in row:
            tbl += str(field)
            tbl += ", "
        tbl += "\n\n|"
    tbl += "---------------------------"
    messagebox.showinfo("~           Novels in the Database           ~", tbl)

#list for author names
def author_lb(w, f, author):
    lblauthor = Label(f,text = "authors").pack(side = TOP)

    Lb = Listbox(f, height = 8, width = 26,font=("arial", 12), exportselection = False) 
    Lb.pack(side = TOP, fill = Y)
                
    scroll = Scrollbar(w, orient = VERTICAL) # set scrollbar to list box for when entries exceed size of list box
    scroll.config(command = Lb.yview)
    scroll.pack(side = RIGHT, fill = Y)
    Lb.config(yscrollcommand = scroll.set)
    

    i = 0
    for name in author:
        Lb.insert(i, name)
        i += 1
    Lb.selection_set(first = 0)

    return Lb

#add novel
def insert_info(x,y,z):
    ins_str = 'INSERT INTO novel (isbn, authorid, title) Values (' + str(x) + ', ' + str(y) + ', "' + str(z) + '");'
    res = c.execute(ins_str)
    con.commit()
    return
    

# This function is used to add a new novel to the database
def add_novel():
    res_req_win = Tk()
    res_req_win.title("Reservation Request")
    res_req_win.geometry("400x400")
    
    info_frame = Frame(res_req_win)
    info_frame.pack(side = LEFT)

    new_novel = tk.StringVar(res_req_win)
    new_isbn = tk.StringVar(res_req_win)

    lbl = Label(info_frame, text = "Choose an author and type in the correct information").pack()
    lblname = Label(info_frame, text = "Novel Title").pack()
    booktitle = Entry(info_frame, text="novel name here", textvariable = new_novel).pack()

    lblname = Label(info_frame, text = "ISBN num").pack()
    isbn_num = Entry(info_frame, text="input isbn", textvariable = new_isbn).pack()

    option_frame = Frame(res_req_win)
    option_frame.pack(side = RIGHT)

    authors = find_author_name()
    author_picked = author_lb(res_req_win, option_frame, authors)

    author_picked = author_lb.curselection()[0][0]
    
    if author_picked == "Joe":
        author_id = 1
    elif author_picked == "Joe":
        author_id = 2
    elif author_picked == "Joe":
        author_id = 3
    
    finalbutton = Button(info_frame, text="add novel", command = insert_info(new_novel.get(), author_id.get(), new_isbn.get())).pack(side=bottom)
    
    res_req_win.mainloop()
    
# Main screen of program, print is outside to prevent two prints of this message
def render_menu():
    window = Tk()
    window.title("~~~ Kolton's novel database ~~~")
    window.geometry("300x150")

    title = tk.Label(text="~~~ Please Pick an Option Below ~~~")
    title.pack(side=TOP)

    design = tk.Label(text="~~~                             ~~~")
    design.pack(side=TOP)
    
    res = Button(window, text="Display Novels", command = render_novel)
    res.pack(side=TOP)

    rpt = Button(window, text="Add a novel to database", command = add_novel)
    rpt.pack(side=TOP)

    ext = Button(window, text="Close program", command = lambda:end_program(window))
    ext.pack(side=TOP)

    design = tk.Label(text="~~~                             ~~~")
    design.pack(side=TOP)
    
    window.mainloop()
     
def end_program(w):
    con.close()
    w.destroy()

while render_menu():
    render_menu()
