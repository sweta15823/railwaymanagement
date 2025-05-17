from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
from PIL import ImageTk, Image
import time
from tkinter.ttk import Combobox
from datetime import datetime
import mysql.connector
import uuid

def tick(time1=''):
    # get the current local time from the PC
    time2 = time.strftime('%I:%M:%S %p\n%A, %B %d, %Y')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    clock.after(200, tick)

class Passenger:
    def __init__(self,root,From=None,To=None,Train_Number=None,Date=None,Class=None,Day=None,total_price=None):
        self.root = root
        self.root.title("Indian Railways")
        self.root.geometry("1432x950+0+0")

        self.First_Name = StringVar()
        self.Last_Name = StringVar()
        self.DOB = DateEntry()
        self.Gender = StringVar 
        self.Address = StringVar()
        self.Email = StringVar()
        self.Phone = IntVar()
        self.Passenger_ID = StringVar()

        logo_image = Image.open("Railway Management System\\IRCTC-logo.png")
        self.logo_photo = ImageTk.PhotoImage(logo_image)

        self.root.iconphoto(False, self.logo_photo)

        bg_image = Image.open("Railway Management System\\42839304.jpg")
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        navbar = Frame(root, bg="white", height=120, width=root.winfo_screenwidth())
        navbar.place(x=0, y=0)

        box_frame = Frame(root, bg="white", height=500, width=720)
        box_frame.place(x=100, y=140)

        # navbar1 = Frame(root, bg="blue", height=10, width=root.winfo_screenwidth())
        # navbar1.place(x=0, y=120)

        image1 = Image.open("Railway Management System\\IR logo Blue color.jpg")
        image2 = Image.open("Railway Management System\\IRCTC-logo.png")

        image1 = image1.resize((100, 100))
        image2 = image2.resize((100, 100))

        self.photo1 = ImageTk.PhotoImage(image1)
        self.photo2 = ImageTk.PhotoImage(image2)

        left_frame = Frame(navbar, bg="white", width=200, height=110)
        left_frame.place(x=10, y=10)

        label1 = Label(left_frame, image=self.photo1,borderwidth=0)
        label1.place(x=0, y=0)

        center_frame = Frame(navbar, bg="white", width=1100, height=110)
        center_frame.place(x=220, y=10)

        self.Class = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "Class",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Class.place(x=250,y=50)
        

        self.Price = Label(box_frame, font = ('New Times Roman',12,'bold'),text = f"Rs:{total_price}",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Price.place(x=350,y=50)

        self.FirstName = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "First Name :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.FirstName.place(x=130,y=80)
        self.FirstName = Entry(box_frame, font = ('New Times Roman',12,'bold'),textvariable=self.First_Name,width=20)
        self.FirstName.place(x=130,y=110)

        self.LastName = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "Last Name :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.LastName.place(x=400,y=80)
        self.LastName = Entry(box_frame, font = ('New Times Roman',12,'bold'),textvariable=self.Last_Name,width=20)
        self.LastName.place(x=400,y=110)

        self.Address = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "Address :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Address.place(x=130,y=140)
        self.Address = Entry(box_frame, font = ('New Times Roman',12,'bold'),textvariable=self.Address,width=50)
        self.Address.place(x=130,y=170)

        self.Email = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "Email :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Email.place(x=130,y=260)
        self.Email = Entry(box_frame, font = ('New Times Roman',12,'bold'),textvariable=self.Email,width=20)
        self.Email.place(x=130,y=290)

        self.Phone = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "Phone :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Phone.place(x=130,y=200)
        self.Phone = Entry(box_frame, font = ('New Times Roman',12,'bold'),textvariable=self.Phone,width=20)
        self.Phone.place(x=130,y=230)

        self.Passenger_ID = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "Aadhar No :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Passenger_ID.place(x=130,y=310)
        self.Passenger_ID = Entry(box_frame, font = ('New Times Roman',12,'bold'),textvariable=self.Phone,width=50)
        self.Passenger_ID.place(x=130,y=340)

        self.Gender = ["Male","Female","Other"]
        self.Gender_label = Label(box_frame, font=('New Times Roman', 12, 'bold'), text="Gender:", padx=2, pady=2, bg="white", fg="navy blue")
        self.Gender_label.place(x=400, y=200)
        self.Gender_combobox = Combobox(box_frame, values=self.Gender, width=25)
        self.Gender_combobox.place(x=400, y=230)

        self.dob_label = Label(box_frame, font=('New Times Roman', 12, 'bold'), text="DOB:", padx=2, pady=2, bg="white", fg="navy blue")
        self.dob_label.place(x=400, y=260)
        self.dob_entry = DateEntry(box_frame, width=20, background='darkblue', foreground='white', borderwidth=2)
        self.dob_entry.place(x=400, y=290)

        pnr_heading = Label(box_frame, text="Passenger Details", font=('Helvetica', 20, 'bold'), bg="white", fg="navy blue")
        pnr_heading.place(x=250, y=10)

        # center_frame2 = Frame(center_frame1, bg="white", width=200, height=100)
        # center_frame2.place(x=0, y=0)

        title_label = Label(center_frame, text="INDIAN RAILWAYS", font = ('Helvetica',30,'bold'), fg='navy blue',bg="white")
        title_label.place(x=315, y=0)

        tagline_label = Label(center_frame, text="Safety | Security | Punctuality", font = ('Helvetica',15), fg='navy blue',bg="white")
        tagline_label.place(x=356, y=50)

        right_frame = Frame(navbar, bg="white", width=200, height=110)
        right_frame.place(x=1222, y=10)

        label2 = Label(right_frame, image=self.photo2,borderwidth=0)
        label2.place(x=100, y=0)

        button2 = Button(box_frame, text="Back",font = ('Helvetica',10,'normal'),
                                 padx = 10,width = 8,bd = 2,bg = 'navy blue',fg = 'white',relief= 'flat',command=lambda:self.open_page(From,To,Train_Number,Date,Day))
        button2.place(x=30, y=20)

        button3 = Button(box_frame, text="Submit", font=('Helvetica', 10, 'bold'),
                 padx=10, width=8, bd=2, bg='orange', fg='white', relief='flat',
                 command=lambda: self.add_passenger_to_database(Class, Train_Number, Date,From,To,total_price))
        button3.place(x=300, y=380)


    def open_page(self,From,To,Train_Number,Date,Day):
        from Train_Details import TrainDetails
        self.root.withdraw()  # Hide the current window
        page2_window = Toplevel(self.root)  # Create a new window
        page2 = TrainDetails(page2_window,From,To,Train_Number,Date,Day)  # Initialize Page2 in the new

    def add_passenger_to_database(self,Class,Train_Number,Date,From,To,total_price):
    # Retrieve values from entry widgets
        first_name = self.First_Name.get()
        last_name = self.Last_Name.get()
        dob = self.dob_entry.get_date().strftime("%Y-%m-%d")  # Corrected line
        gender = self.Gender_combobox.get()
        address = self.Address.get()
        email = self.Email.get()
        phone = self.Phone.get()
        aadhar = self.Passenger_ID.get()

        try:
            # Establish connection to MySQL
            mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                password='roshni',
                database='railway'
            )

            # Create a cursor object to execute SQL queries
            cursor = mydb.cursor()

            # Check if the Driver table exists
            cursor.execute("SHOW TABLES LIKE 'passenger'")
            table_exists = cursor.fetchone()
            if table_exists:
            # Fetch the maximum existing passenger_id
                sql_query = "INSERT INTO passenger (Passenger_ID,FirstName, LastName, DOB, Gender, Address, Email,Phone,Class) VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s)"
                values = (aadhar ,first_name, last_name, dob,gender,address, email,phone,Class)
                cursor.execute(sql_query, values)
                sql_query1 = "INSERT INTO train_passenger_details (Passenger_ID,Train_Number,Class,Train_date,Source_city,Dest_city,Paid_value) VALUES (%s, %s, %s,%s,%s,%s,%s)"
                values1 = (aadhar,Train_Number,Class,Date,From,To,total_price)
                cursor.execute(sql_query1, values1)
                # Commit the changes
                mydb.commit()
                # Close the cursor and connection
                cursor.close()
                mydb.close()

                # Show success message
                messagebox.showinfo(f"Success Booking Request added successfully!")
            else:
                # Show error message if the table does not exist
                messagebox.showerror("Error!")
        except mysql.connector.Error as error:
            # Show error message
            messagebox.showerror("Error", f"Error adding driver details: {error}") 

        


if __name__=='__main__':
    root = Tk()
    application = Passenger(root)
    clock = Label(root, font=('calibri', 15, 'bold'), bg='black', fg='red', bd=10, relief='groove',highlightbackground='black', highlightthickness=2)
    clock.place(x=1000, y=120)
    tick()
    root.mainloop()
