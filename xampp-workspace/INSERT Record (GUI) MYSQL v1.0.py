# Author: Jay Garcia BSCPE - CPE12S1
# Created: 05/09/2024
# INSERT Record (GUI) MYSQL v1.0 - Lab Activity

from tkinter import *
from tkinter import messagebox
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "db_16"
)

mycursor = mydb.cursor()
def press():    

    if entry_1.get() == "" or entry_2.get() == "" or entry_3.get() == "":
        messagebox.showwarning("showwarning", "Do not leave blanks")
        entry_1.focus_set()
    
    else:
        sql = "INSERT INTO tblstudents VALUES (NULL,'" + entry_1.get() + "','" + entry_2.get() + "'," + entry_3.get() + ")"
        mycursor.execute(sql)
        mydb.commit()
        messagebox.showinfo("showinfo", "Records Inserted")
        ClearEntries()

def ClearEntries():
    entry_1.delete(0, END)
    entry_2.delete(0, END)
    entry_3.delete(0, END)
    entry_1.focus_set()

root = Tk()
root.title("Place Sample")
root.geometry("500x300")
root.resizable(width= False, height= False)

label_title = Label(root, text= "INSERT Record (GUI) MYSQL", font= "Arial 20 bold")
label_1 = Label(root, text= "First Name:", font= "Arial 20 bold")
label_2 = Label(root, text= "Last Name:", font= "Arial 20 bold")
label_3 = Label(root, text= "Age:", font= "Arial 20 bold")
  # place value coordinates
label_title.place(x= 250, y= 20, anchor= "center")
label_1.place(x= 30, y= 60)
label_2.place(x= 30, y= 100)
label_3.place(x= 30, y= 140)

entry_1 = Entry(root, font= "Arial 20 bold")
entry_2 = Entry(root, font= "Arial 20 bold")
entry_3 = Entry(root, font= "Arial 20 bold")
  # place value coordinates
entry_1.place(x= 200, y= 60, width= 270)
entry_2.place(x= 200, y= 100, width= 270)
entry_3.place(x= 200, y= 140, width= 270)

button_1 = Button(root, text= "Insert", font= "Arial 20 bold", command= press)
  # place value coordinates
button_1.place(x= 250, y= 230, width= 440, anchor= "center")
showvalue= StringVar()

root.mainloop()
