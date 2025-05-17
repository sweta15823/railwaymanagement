from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkcalendar import *
from PIL import ImageTk, Image
import time
import datetime
import mysql.connector

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

class ADD_DRIVER:
    selected_date = None  # Initialize with None

    def __init__(self,root,initial_values=None):
        self.root = root
        self.root.title("Indian Railways")
        self.root.geometry("1432x950+0+0")

        self.First_name = StringVar()
        self.Last_Name = StringVar()
        self.IRCTC_ID = StringVar()
        self.DOB = DateEntry()
        self.Address = StringVar()
        self.City = StringVar()
        self.State = StringVar()
        self.Year_of_join = DateEntry()


        if initial_values:
            self.First_name.set(initial_values[1])
            self.Last_Name.set(initial_values[2])
            self.DOB.insert(0,initial_values[3])
            self.Address.set(initial_values[4])
            self.State.set(initial_values[5])
            self.City.set(initial_values[6])
            self.Year_of_join.insert(0,initial_values[7])
            self.IRCTC_ID.set(initial_values[0])
            


        # logo_image = Image.open("IRCTC-logo.png")
        logo_image = Image.open("Railway Management System\\IRCTC-logo.png")
        self.logo_photo = ImageTk.PhotoImage(logo_image)

        self.root.iconphoto(False, self.logo_photo)

        bg_image = Image.open("Railway Management System\\42839304.jpg")
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        
        bg_label = Label(self.root,image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        navbar = Frame(root, bg="white", height=120, width=root.winfo_screenwidth())
        navbar.place(x=0, y=0)

        box_frame = Frame(root, bg="white", height=500, width=730)
        box_frame.place(x=100, y=140)

        pnr_heading = Label(box_frame, text="ADD DRIVER DETAILS", font=('Helvetica', 20, 'bold'), bg="white", fg="navy blue")
        pnr_heading.place(x=230, y=10)

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

        # Instead of overwriting the StringVar and DateEntry objects, create separate variables for labels and entry widgets
        self.first_name_label = Label(box_frame, font=('New Times Roman', 12, 'bold'), text="First Name:", padx=2, pady=2, bg="white", fg="navy blue")
        self.first_name_label.place(x=130, y=60)
        self.first_name_entry = Entry(box_frame, font=('New Times Roman', 12, 'bold'), textvariable=self.First_name, width=20)
        self.first_name_entry.place(x=130, y=85)

        self.last_name_label = Label(box_frame, font=('New Times Roman', 12, 'bold'), text="Last Name:", padx=2, pady=2, bg="white", fg="navy blue")
        self.last_name_label.place(x=400, y=60)
        self.last_name_entry = Entry(box_frame, font=('New Times Roman', 12, 'bold'), textvariable=self.Last_Name, width=20)
        self.last_name_entry.place(x=400, y=85)

        self.dob_label = Label(box_frame, font=('New Times Roman', 12, 'bold'), text="DOB:", padx=2, pady=2, bg="white", fg="navy blue")
        self.dob_label.place(x=130, y=105)
        self.dob_entry = DateEntry(box_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.dob_entry.place(x=130, y=130)

        self.year_of_join_label = Label(box_frame, font=('New Times Roman', 12, 'bold'), text="Date of Joining:", padx=2, pady=2, bg="white", fg="navy blue")
        self.year_of_join_label.place(x=400, y=105)
        self.year_of_join_entry = DateEntry(box_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.year_of_join_entry.place(x=400, y=130)

        self.address_label = Label(box_frame, font=('New Times Roman', 12, 'bold'), text="Address:", padx=2, pady=2, bg="white", fg="navy blue")
        self.address_label.place(x=130, y=150)
        self.address_entry = Entry(box_frame, font=('New Times Roman', 12, 'bold'), textvariable=self.Address, width=50)
        self.address_entry.place(x=130, y=175)

        self.city_label = Label(box_frame, font=('New Times Roman', 12, 'bold'), text="City:", padx=2, pady=2, bg="white", fg="navy blue")
        self.city_label.place(x=130, y=200)
        self.city_entry = Entry(box_frame, font=('New Times Roman', 12, 'bold'), textvariable=self.City, width=20)
        self.city_entry.place(x=130, y=225)

        self.state_label = Label(box_frame, font=('New Times Roman', 12, 'bold'), text="State:", padx=2, pady=2, bg="white", fg="navy blue")
        self.state_label.place(x=400, y=200)
        self.state_entry = Entry(box_frame, font=('New Times Roman', 12, 'bold'), textvariable=self.State, width=20)
        self.state_entry.place(x=400, y=220)

        self.irctc_id_label = Label(box_frame, font=('New Times Roman', 12, 'bold'), text="IRCTC ID:", padx=2, pady=2, bg="white", fg="navy blue")
        self.irctc_id_label.place(x=130, y=250)
        self.irctc_id_entry = Entry(box_frame, font=('New Times Roman', 12, 'bold'), textvariable=self.IRCTC_ID, width=40)
        self.irctc_id_entry.place(x=130, y=280)


        title_label = Label(center_frame, text="INDIAN RAILWAYS", font = ('Helvetica',30,'bold'), fg='navy blue',bg="white")
        title_label.place(x=315, y=0)

        tagline_label = Label(center_frame, text="Safety | Security | Punctuality", font = ('Helvetica',15), fg='navy blue',bg="white")
        tagline_label.place(x=356, y=50)

        right_frame = Frame(navbar, bg="white", width=200, height=110)
        right_frame.place(x=1222, y=10)

        label2 = Label(right_frame, image=self.photo2,borderwidth=0)
        label2.place(x=100, y=0)

        button2 = Button(box_frame, text="Back",font = ('Helvetica',10,'normal'),
                                 padx = 10,width = 8,bd = 2,bg = 'navy blue',fg = 'white',relief= 'flat',command=self.open_page)
        button2.place(x=30, y=20)

        button1 = Button(box_frame, text="Add",font = ('Helvetica',10,'normal'),
                                 padx = 10,width = 8,bd = 2,bg = 'navy blue',fg = 'white',relief= 'flat',command=self.add_driver_to_database)
        button1.place(x=300, y=330)
    

    def open_page(self):
        from Employee_Management import EP
        self.root.withdraw()  # Hide the current window
        page2_window = Toplevel(self.root)  # Create a new window
        page2 = EP(page2_window)  # Initialize Page2 in the new window

    def add_driver_to_database(self):
    # Retrieve values from entry widgets
        first_name = self.First_name.get()
        last_name = self.Last_Name.get()
        irctc_id = self.IRCTC_ID.get()
        dob = self.dob_entry.get_date().strftime("%Y-%m-%d")  # Corrected line
        address = self.Address.get()
        city = self.City.get()
        state = self.State.get()
        year_of_join = self.year_of_join_entry.get_date().strftime('%Y-%m-%d')  # Corrected line

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
            cursor.execute("SHOW TABLES LIKE 'driver'")
            table_exists = cursor.fetchone()
            if table_exists:
                # Check if the driver already exists by IRCTC ID
                cursor.execute("SELECT * FROM driver WHERE IRCTC_ID = %s", (irctc_id,))
                existing_driver = cursor.fetchone()
                if existing_driver:
                # If driver exists, update the entry
                    sql_query = "UPDATE driver SET First_name=%s, Last_Name=%s, DOB=%s, Address=%s, City=%s, State=%s, Year_of_Join=%s WHERE IRCTC_ID=%s"
                    values = (first_name, last_name, dob, address, city, state, year_of_join, irctc_id)
                else:
                    # If driver does not exist, insert a new entry
                    sql_query = "INSERT INTO driver (First_name, Last_Name, IRCTC_ID, DOB, Address, City, State, Year_of_Join) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    values = (first_name, last_name, irctc_id, dob, address, city, state, year_of_join)
                
                cursor.execute(sql_query, values)


                # Execute the SQL query

                # Commit the changes
                mydb.commit()

                # Close the cursor and connection
                cursor.close()
                mydb.close()

                # Show success message
                tkinter.messagebox.showinfo("Success", "driver details added successfully!")
            else:
                # Show error message if the table does not exist
                tkinter.messagebox.showerror("Error", "driver table does not exist!")
        except mysql.connector.Error as error:
            # Show error message
            tkinter.messagebox.showerror("Error", f"Error adding driver details: {error}")


if __name__=='__main__':
    root = Tk()
    application = ADD_DRIVER(root)
    clock = Label(root, font=('calibri', 15, 'bold'), bg='black', fg='red', bd=10, relief='groove',highlightbackground='black', highlightthickness=2)
    clock.place(x=1000, y=120)
    tick()
    root.mainloop()
