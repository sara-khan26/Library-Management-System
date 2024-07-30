from tkinter import*
from tkinter import ttk
import tkinter
import tkinter.messagebox
import mysql.connector
from tkinter import messagebox
import datetime
from tkinter import Listbox


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")
        
        # =========Variables===============================
        self.member_var = StringVar()
        self.prn_var = StringVar()
        self.id_var = StringVar()
        self.firstname_var = StringVar()
        self.lastname_var = StringVar()
        self.address1_var = StringVar()
        self.address2_var = StringVar()
        self.postcode_var = StringVar()
        self.mobile_var = StringVar()
        self.bookid_var = StringVar()
        self.booktitle_var = StringVar()
        self.author_var = StringVar()
        self.dateborrowed_var = StringVar()
        self.datedue_var = StringVar()
        self.daysonbook_var = StringVar()
        self.latereturnfine_var = StringVar()
        self.dateoverdue_var = StringVar()
        self.finalprice_var = StringVar()
        
        lbltitle = Label(self.root, text = "LIBRARY MANAGEMENT SYSTEM", bg="grey", bd = 20, relief=RIDGE, font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 50, "bold"), padx = 2, pady = 6)
        lbltitle.pack(side= TOP, fill =X)
        
        frame = Frame(self.root, bd = 12, relief=RIDGE, padx=20, bg = "grey")
        frame.place(x = 0, y = 130, width = 1530, height= 400)
        
        # ============DataFrameLeft========================
        DataFrameLeft = LabelFrame(frame, text = "Library Membership Information", bg="grey", bd = 12, relief=RIDGE, font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"))
        DataFrameLeft.place(x = 0, y = 5, width = 900, height = 350)
        
        lblMember = Label(DataFrameLeft, bg = "grey", text="Memeber Type:", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), padx=2, pady=6)
        lblMember.grid(row = 0, column=0, sticky=W)
        
        comMember = ttk.Combobox(DataFrameLeft, textvariable=self.member_var ,font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 10, "bold"), width = 35, state = "readonly")
        comMember["value"] = ("Admin staff", "Student", "Lecturer")
        comMember.grid(row = 0, column = 1)
        
        lblref = Label(DataFrameLeft, bg = "grey", text="PRN No:", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), padx=2, pady=6)
        lblref.grid(row = 1, column=0, sticky=W)
        txtref = Entry(DataFrameLeft, textvariable=self.prn_var,font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12), width=29)
        txtref.grid(row = 1, column=1)
        
        lblTitle = Label(DataFrameLeft, bg = "grey", text="ID No:", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), padx=2, pady=6)
        lblTitle.grid(row = 2, column=0, sticky=W)
        txtTitle = Entry(DataFrameLeft,textvariable=self.id_var, font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12), width=29)
        txtTitle.grid(row = 2, column=1)
        
        lblFirstName = Label(DataFrameLeft, bg = "grey", text="First Name:", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), padx=2, pady=6)
        lblFirstName.grid(row = 3, column=0, sticky=W)
        txtFirstName = Entry(DataFrameLeft, textvariable=self.firstname_var,font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12), width=29)
        txtFirstName.grid(row = 3, column=1)
        
        lblLastName = Label(DataFrameLeft, bg = "grey", text="Surname:", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), padx=2, pady=6)
        lblLastName.grid(row = 4, column=0, sticky=W)
        txtLastName = Entry(DataFrameLeft,textvariable=self.lastname_var, font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12), width=29)
        txtLastName.grid(row = 4, column=1)
        
        lblAddress1 = Label(DataFrameLeft, bg = "grey", text="Address 1:", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), padx=2, pady=6)
        lblAddress1.grid(row = 5, column=0, sticky=W)
        txtAddress1 = Entry(DataFrameLeft,textvariable=self.address1_var, font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12), width=29)
        txtAddress1.grid(row = 5, column=1)
        
        lblAddress2 = Label(DataFrameLeft, bg = "grey", text="Address 2:", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), padx=2, pady=6)
        lblAddress2.grid(row = 6, column=0, sticky=W)
        txtAddress2 = Entry(DataFrameLeft,textvariable=self.address2_var, font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12), width=29)
        txtAddress2.grid(row = 6, column=1)
        
        lblPostCode = Label(DataFrameLeft, bg = "grey", text="Post code:", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), padx=2, pady=6)
        lblPostCode.grid(row = 7, column=0, sticky=W)
        txtPostCode = Entry(DataFrameLeft,textvariable=self.postcode_var, font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12), width=29)
        txtPostCode.grid(row = 7, column=1)
        
        lblMobile = Label(DataFrameLeft, bg = "grey", text="Mobile:", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row = 8, column=0, sticky=W)
        txtMobile = Entry(DataFrameLeft,textvariable=self.mobile_var, font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12), width=29)
        txtMobile.grid(row = 8, column=1)
        
        lblBookId = Label(DataFrameLeft, bg = "grey", text="Book ID:", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), padx=2, pady=6)
        lblBookId.grid(row = 0, column=2, sticky=W)
        txtBookId = Entry(DataFrameLeft,textvariable=self.bookid_var, font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12), width=29)
        txtBookId.grid(row = 0, column=3)
        
        lblBookTitle = Label(DataFrameLeft, bg = "grey", text="Book Title:", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), padx=2, pady=6)
        lblBookTitle.grid(row = 1, column=2, sticky=W)
        txtBookTitle = Entry(DataFrameLeft,textvariable=self.booktitle_var, font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12), width=29)
        txtBookTitle.grid(row = 1, column=3)
        
        lblAuthor = Label(DataFrameLeft, bg = "grey", text="Author:", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), padx=2, pady=6)
        lblAuthor.grid(row = 2, column=2, sticky=W)
        txtAuthor = Entry(DataFrameLeft,textvariable=self.author_var, font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12), width=29)
        txtAuthor.grid(row = 2, column=3)
        
        lblDateBorrowed = Label(DataFrameLeft, bg = "grey", text="Date Borrowed:", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), padx=2, pady=6)
        lblDateBorrowed.grid(row = 3, column=2, sticky=W)
        txtDateBorrowed = Entry(DataFrameLeft,textvariable=self.dateborrowed_var, font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12), width=29)
        txtDateBorrowed.grid(row = 3, column=3)
        
        lblDateDue = Label(DataFrameLeft, bg = "grey", text="Date Due:", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), padx=2, pady=6)
        lblDateDue.grid(row = 4, column=2, sticky=W)
        txtDateDue = Entry(DataFrameLeft,textvariable=self.datedue_var, font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12), width=29)
        txtDateDue.grid(row = 4, column=3)
        
        lblDaysOnBook = Label(DataFrameLeft, bg = "grey", text="Days on Book:", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), padx=2, pady=6)
        lblDaysOnBook.grid(row = 5, column=2, sticky=W)
        txtDaysOnBook = Entry(DataFrameLeft,textvariable=self.daysonbook_var, font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12), width=29)
        txtDaysOnBook.grid(row = 5, column=3)
        
        lblLateReturnFine = Label(DataFrameLeft, bg = "grey", text="Late Return Fine:", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), padx=2, pady=6)
        lblLateReturnFine.grid(row = 6, column=2, sticky=W)
        txtLateReturnFine = Entry(DataFrameLeft,textvariable=self.latereturnfine_var, font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12), width=29)
        txtLateReturnFine.grid(row = 6, column=3)
        
        lblDateOverDate = Label(DataFrameLeft, bg = "grey", text="Date over due:", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), padx=2, pady=6)
        lblDateOverDate.grid(row = 7, column=2, sticky=W)
        txtDateOverDate = Entry(DataFrameLeft,textvariable=self.dateoverdue_var, font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12), width=29)
        txtDateOverDate.grid(row = 7, column=3)
        
        lblActualPrice = Label(DataFrameLeft, bg = "grey", text="Actual Price:", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), padx=2, pady=6)
        lblActualPrice.grid(row = 8, column=2, sticky=W)
        txtActualPrice = Entry(DataFrameLeft,textvariable=self.finalprice_var, font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12), width=29)
        txtActualPrice.grid(row = 8, column=3)
        
        # ===========DataFrameRight===============================
        
        DataFrameRight = LabelFrame(frame, text = "Book Details", bg="grey", bd = 12, relief=RIDGE, font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"))
        DataFrameRight.place(x = 910, y = 5, width = 540, height = 350)
        
        self.txtBox = Text(DataFrameRight, font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), width = 32, height = 16, padx = 2, pady = 6)
        self.txtBox.grid(row=0, column=2)
        
        listBooks = ["Pride and Prejudice",
                     "1984",
                     "Don Quixote",
                     "To Kill a Mockingbird",
                     "The Lord of the Rings",
                     "Jane Eyre",
                     "Catch-22",
                     "Lolita",
                     "Moby-Dick",
                     "The Catcher in the Rye",
                     "Adventures of Huckleberry Finn",
                     "Brave New World",
                     "War and Peace",
                     "Frankenstein",
                     "Harry Potter and the Philosopher’s Stone",
                     "Little Women",
                     "The Great Gatsby",
                     "Middlemarch",
                     "Alice's Adventures in Wonderland",
                     "Heart of Darkness"]
        # 'Don Quixote', "Alice's Adventures in Wonderland", 'The Adventures of Huckleberry Finn','The Adventures of Tom Sawyer', 'Treasure Island','Pride and Prejudice','Wuthering Heights', 'Jane Eyre','Moby Dick','The Scarlet Letter'
    
        def SelectBook(event=None):
            value  = str(listBox.get(listBox.curselection()))
            if value == "Pride and Prejudice":
                self.bookid_var.set("BKID121")
                self.booktitle_var.set("Pride and Prejudice")
                self.author_var.set("Jane Austen")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.788")
            
            elif value == "1984":
                self.bookid_var.set("BKID122")
                self.booktitle_var.set("1984")
                self.author_var.set("George Orwell")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.200")
            
            elif value == "Don Quixote":
                self.bookid_var.set("BKID123")
                self.booktitle_var.set("Don Quixote")
                self.author_var.set("Miguel de Cervantes")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.200")
            
            elif value == "To Kill a Mockingbird":
                self.bookid_var.set("BKID124")
                self.booktitle_var.set("To Kill a Mockingbird")
                self.author_var.set("Harper Lee")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.200")
            
            elif value == "The Lord of the Rings":
                self.bookid_var.set("BKID125")
                self.booktitle_var.set("The Lord of the Rings")
                self.author_var.set("J. R. R. Tolkien")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.200")
            
            elif value == "Jane Eyre":
                self.bookid_var.set("BKID126")
                self.booktitle_var.set("Jane Eyre")
                self.author_var.set("Charlotte Brontë")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.200")
            
            elif value == "Catch-22":
                self.bookid_var.set("BKID127")
                self.booktitle_var.set("Catch-22")
                self.author_var.set("Joseph Heller")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.200")
            
            elif value == "Lolita":
                self.bookid_var.set("BKID128")
                self.booktitle_var.set("Lolita")
                self.author_var.set("Vladimir Nabokov")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.200")
            
            elif value == "Moby-Dick":
                self.bookid_var.set("BKID129")
                self.booktitle_var.set("Moby-Dick")
                self.author_var.set("Herman Melville")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.200")
            
            elif value == "The Catcher in the Rye":
                self.bookid_var.set("BKID1210")
                self.booktitle_var.set("The Catcher in the Rye")
                self.author_var.set("J. D. Salinger")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.200")
            
            elif value == "Adventures of Huckleberry Finn":
                self.bookid_var.set("BKID1210")
                self.booktitle_var.set("Adventures of Huckleberry Finn")
                self.author_var.set("Mark Twain")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.200")
            
            elif value == "Brave New World":
                self.bookid_var.set("BKID1210")
                self.booktitle_var.set("Brave New World")
                self.author_var.set("Aldous Huxley")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.200")
            
            elif value == "War and Peace":
                self.bookid_var.set("BKID1210")
                self.booktitle_var.set("War and Peace")
                self.author_var.set("Leo Tolstoy")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.200")
            
            elif value == "Frankenstein":
                self.bookid_var.set("BKID1210")
                self.booktitle_var.set("Frankenstein")
                self.author_var.set("Mary Shelley")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.200")
            
            elif value == "Harry Potter and the Philosopher’s Stone":
                self.bookid_var.set("BKID1210")
                self.booktitle_var.set("Harry Potter and the Philosopher’s Stone")
                self.author_var.set("J. K. Rowling")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.200")
            
            elif value == "Little Women":
                self.bookid_var.set("BKID1210")
                self.booktitle_var.set("Little Women")
                self.author_var.set("Louisa May Alcott")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.200")
            
            elif value == "The Great Gatsby":
                self.bookid_var.set("BKID1210")
                self.booktitle_var.set("The Great Gatsby")
                self.author_var.set("F. Scott Fitzgerald")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.200")
            
            elif value == "Middlemarch":
                self.bookid_var.set("BKID1210")
                self.booktitle_var.set("Middlemarch")
                self.author_var.set("George Eliot")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.200")
            
            elif value == "Alice's Adventures in Wonderland":
                self.bookid_var.set("BKID1210")
                self.booktitle_var.set("Alice's Adventures in Wonderland")
                self.author_var.set("Lewis Carroll")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.200")
            
            elif value == "Heart of Darkness":
                self.bookid_var.set("BKID1210")
                self.booktitle_var.set("Heart of Darkness")
                self.author_var.set("Joseph Conrad")

                d1 = datetime.date.today()
                d2 = datetime.timedelta(days=15)
                d3 = d1 + d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.latereturnfine_var.set("Rs.25")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.200")
            
            
    
        listBox = Listbox(DataFrameRight, font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), width = 20, height = 16)
        listBox.bind("<<ListboxSelect>>", SelectBook)
        listBox.grid(row=0, column=0, padx=4)
        # Scrollbar.config(command=listBox.yview)
        
        for item in listBooks:
            listBox.insert(END,item)
        
        # ========Bottons frame============================
        
        Framebutton = Frame(self.root, bd = 12, relief=RIDGE, padx=20, bg = "grey")
        Framebutton.place(x = 0, y = 530, width = 1530, height= 60)
        
        btnAddData = Button(Framebutton, command = self.add_data ,text="Add Data", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), width = 23, bg = "black", fg = "white")
        btnAddData.grid(row=0, column=0)
        
        btnAddData = Button(Framebutton, command = self.showData, text="show Data", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), width = 23, bg = "black", fg = "white")
        btnAddData.grid(row=0, column=1)
        
        btnAddData = Button(Framebutton, command = self.update ,text="Update", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), width = 23, bg = "black", fg = "white")
        btnAddData.grid(row=0, column=2)
        
        btnAddData = Button(Framebutton, command = self.delete,text="Delete", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), width = 23, bg = "black", fg = "white")
        btnAddData.grid(row=0, column=3)
        
        btnAddData = Button(Framebutton, command = self.reset, text="Reset", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), width = 23, bg = "black", fg = "white")
        btnAddData.grid(row=0, column=4)
        
        btnAddData = Button(Framebutton, command = self.iExit, text="Exit", font=("'Trebuchet MS', 'Lucida Sans Unicode', 'Lucida Grande', 'Lucida Sans', Arial, sans-serif", 12, "bold"), width = 23, bg = "black", fg = "white")
        btnAddData.grid(row=0, column=5)
        
        # ========Info frame============================
        
        FrameDetails = Frame(self.root, bd = 12, relief=RIDGE, padx=20, bg = "grey")
        FrameDetails.place(x = 0, y = 600, width = 1530, height= 195)
        
        Table_frame = Frame(FrameDetails, bd = 6, relief=RIDGE, bg = "grey")
        Table_frame.place(x = 0, y = 2, width = 1460, height= 190)
        
        xscroll = ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll = ttk.Scrollbar(Table_frame,orient=VERTICAL)
        
        self.library_table = ttk.Treeview(Table_frame, columns=("membertype","prnno","title","firstname","lastname","address1","address2","postid","mobile","bookid","booktitle","author","dateborrowed","datedue","days","latereturnfine","dateoverdue","finalprice"), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)
        
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        self.library_table.heading("membertype", text = "Member Type")
        self.library_table.heading("prnno", text = "PRN N0.")
        self.library_table.heading("title", text = "Title")
        self.library_table.heading("firstname", text = "First Name")
        self.library_table.heading("lastname", text = "Last Name")
        self.library_table.heading("address1", text = "Address1")
        self.library_table.heading("address2", text = "Address2")
        self.library_table.heading("postid", text = "Post ID")
        self.library_table.heading("mobile", text = "Mobile Number")
        self.library_table.heading("bookid", text = "Book ID")
        self.library_table.heading("booktitle", text = "BookTitle")
        self.library_table.heading("author", text = "Author")
        self.library_table.heading("dateborrowed", text = "Date Of Borrowed")
        self.library_table.heading("datedue", text = "Date Due")
        self.library_table.heading("days", text = "DaysOnBook")
        self.library_table.heading("latereturnfine", text = "LateReturnFine")
        self.library_table.heading("dateoverdue", text = "DateOverDue")
        self.library_table.heading("finalprice", text = "Final Price")
        
        self.library_table["show"] = "headings"
        self.library_table.pack(fill = BOTH, expand=1)
        
        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("address1",width=100)
        self.library_table.column("address2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("author",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("latereturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)
        
        self.fetch_data()
        self.library_table.bind("<ButtonRelease-1>", self.get_cursor)
    
    def add_data(self):
        if self.member_var.get() == "" or self.prn_var.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="srkhsrkh", database="project")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into libproj values( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (self.member_var.get(), self.prn_var.get(),self.id_var.get(),self.firstname_var.get(),self.lastname_var.get(), self.address1_var.get(), self.address2_var.get(), self.postcode_var.get(), self.mobile_var.get(), self.bookid_var.get(), self.booktitle_var.get(), self.author_var.get(), self.dateborrowed_var.get(), self.datedue_var.get(), self.daysonbook_var.get(), self.latereturnfine_var.get(), self.dateoverdue_var.get(), self.finalprice_var.get()))
            
            conn.commit()
            self.fetch_data()
            conn.close()
            
            messagebox.showinfo("Success", "Member inserted successfully...")
            
    def update(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="srkhsrkh", database="project")
        my_cursor = conn.cursor()
        my_cursor.execute("update libproj set member = %s, id = %s, firstname = %s, lastname = %s, address1 = %s, address2 = %s, postcode = %s, mobile = %s, bookid = %s, booktitle = %s, author = %s, dateburrowed = %s, datedue = %s, daysonbook = %s, latereturnfine = %s, dateoverdue = %s, finalprice = %s where prn_no = %s", (self.member_var.get(), self.id_var.get(),self.firstname_var.get(),self.lastname_var.get(), self.address1_var.get(), self.address2_var.get(), self.postcode_var.get(), self.mobile_var.get(), self.bookid_var.get(), self.booktitle_var.get(), self.author_var.get(), self.dateborrowed_var.get(), self.datedue_var.get(), self.daysonbook_var.get(), self.latereturnfine_var.get(), self.dateoverdue_var.get(), self.finalprice_var.get(),self.prn_var.get())) 
        
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()
        
        messagebox.showinfo("Success", "Member updated Successfully...")
    
    def fetch_data(self):
            conn = mysql.connector.connect(host="localhost", user="root", password="srkhsrkh", database="project")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from libproj")
            rows = my_cursor.fetchall()
            
            if len(rows) != 0:
                self.library_table.delete(*self.library_table.get_children())
                for i in rows:
                    self.library_table.insert("",END, values = i)
                conn.commit()
            conn.close()
    
    def get_cursor(self, event = ""):
        cursor_row = self.library_table.focus()
        content = self.library_table.item(cursor_row)
        row = content['values']
        
        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.author_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])
        
    def showData(self):
        self.txtBox.insert(END, "Member Type: \t\t" + self.member_var.get() + "\n")
        self.txtBox.insert(END, "PRN No.: \t\t" + self.prn_var.get() + "\n")
        self.txtBox.insert(END, "ID No.: \t\t" + self.id_var.get() + "\n")
        self.txtBox.insert(END, "FirstName: \t\t" + self.firstname_var.get() + "\n")
        self.txtBox.insert(END, "LastName: \t\t" + self.lastname_var.get() + "\n")
        self.txtBox.insert(END, "Address1: \t\t" + self.address1_var.get() + "\n")
        self.txtBox.insert(END, "Address2: \t\t" + self.address2_var.get() + "\n")
        self.txtBox.insert(END, "Post Code: \t\t" + self.postcode_var.get() + "\n")
        self.txtBox.insert(END, "Mobile No.: \t\t" + self.mobile_var.get() + "\n")
        self.txtBox.insert(END, "Book ID: \t\t" + self.bookid_var.get() + "\n")
        self.txtBox.insert(END, "Book Title: \t\t" + self.booktitle_var.get() + "\n")
        self.txtBox.insert(END, "Author: \t\t" + self.author_var.get() + "\n")
        self.txtBox.insert(END, "Date Burrowed: \t\t" + self.dateborrowed_var.get() + "\n")
        self.txtBox.insert(END, "Date Due: \t\t" + self.datedue_var.get() + "\n")
        self.txtBox.insert(END, ":Days on Book \t\t" + self.daysonbook_var.get() + "\n")
        self.txtBox.insert(END, "Late Return Fine: \t\t" + self.latereturnfine_var.get() + "\n")
        self.txtBox.insert(END, "Date Over Due: \t\t" + self.dateoverdue_var.get() + "\n")
        self.txtBox.insert(END, "Final Price: \t\t" + self.finalprice_var.get() + "\n")

    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.author_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set("")
        self.txtBox.delete("1.0", END)
        
        
    def iExit(self):
        iExit = tkinter.messagebox.askyesno("Library Management System", "Do yo want to Exit?")
        if iExit > 0:
            self.root.destroy()
            return
    
    def delete(self):
        if self.prn_var.get() == "" or self.id_var.get() == "":
            messagebox.showerror("Error", "Select the a valid member!")
            
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="srkhsrkh", database="project")
            my_cursor = conn.cursor()
            q = "delete from libproj where prn_no = %s"
            v = (self.prn_var.get(),)
            my_cursor.execute(q,v)
            
            conn.commit()
            self.fetch_data()
            self.reset()
            conn.close()
            
            messagebox.showinfo("Success", "Member deleted successfully...")
    
if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    img = PhotoImage(file = 'logo.gif')
    root.iconphoto(False,img)
    root.mainloop()
    
    
    