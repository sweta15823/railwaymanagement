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

class EP:
    def __init__(self,root):
        self.root = root
        self.root.title("Indian Railways")
        self.root.geometry("1432x950+0+0")

        self.Train_number = IntVar()
        
        self.Train_name = StringVar()
        self.Driver = StringVar()
        self.Source_City = StringVar()
        self.Source_State = StringVar()
        self.Destination_City = StringVar()
        self.Destination_State = StringVar()
        self.StartTime = StringVar()
        self.EndTime = StringVar()
        self.Days = StringVar()
        # Define variables to store driver details
        self.first_name_var = StringVar()
        self.last_name_var = StringVar()
        self.dob_var = StringVar()
        self.address_var = StringVar()
        self.state_var = StringVar()
        self.city_var = StringVar()
        self.year_of_join_var = StringVar()
        self.driver_irctc_entry = StringVar()

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

        box_frame = Frame(root, bg="white", height=500, width=800)
        box_frame.place(x=150, y=130)

        pnr_heading = Label(box_frame, text="TRAIN DETAILS", font=('Helvetica', 20, 'bold'), bg="white", fg="navy blue")
        pnr_heading.place(x=300, y=10)

        # Instruction text
        pnr_instruction = Label(box_frame, text="Enter your Train Number to Check/Modify the train", font=('Helvetica', 16), bg="white", fg="navy blue")
        pnr_instruction.place(x=170, y=50)
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

        self.PNR = Label(box_frame, font = ('New Times Roman',16,'normal'),text = "Train No :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.PNR.place(x=50,y=100)
        self.PNR = Entry(box_frame, font = ('New Times Roman',16,'normal'),textvariable=self.Train_number,width=27)
        self.PNR.place(x=170,y=100)

        self.PNR = Label(box_frame, font = ('New Times Roman',16,'normal'),text = "Driver IRCTC ID :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.PNR.place(x=50,y=150)
        self.PNR = Entry(box_frame, font = ('New Times Roman',16,'normal'),textvariable=self.driver_irctc_entry,width=20)
        self.PNR.place(x=250,y=150)

        title_label = Label(center_frame, text="INDIAN RAILWAYS", font = ('Helvetica',30,'bold'), fg='navy blue',bg="white")
        title_label.place(x=315, y=0)

        self.PNR = Label(box_frame, font = ('New Times Roman',16,'normal'),text = "-----------------------------------------------------------------------------------------------------------------",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.PNR.place(x=0,y=200)

        tagline_label = Label(center_frame, text="Safety | Security | Punctuality", font = ('Helvetica',15), fg='navy blue',bg="white")
        tagline_label.place(x=356, y=50)

        right_frame = Frame(navbar, bg="white", width=200, height=110)
        right_frame.place(x=1222, y=10)

        label2 = Label(right_frame, image=self.photo2,borderwidth=0)
        label2.place(x=100, y=0)

        button1 = Button(box_frame, text="Add New Train",font = ('Helvetica',15,'normal'),
                                 padx = 10,width = 15,bd = 2,bg = 'navy blue',fg = 'white',relief= 'flat',command=self.open_page3)
        button1.place(x=300, y=400)

        self.PNR = Label(box_frame, font = ('New Times Roman',16,'normal'),text = "-----------------------------------------------------------------------------------------------------------------",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.PNR.place(x=0,y=350)

        button4 = Button(box_frame, text="Search",font = ('Helvetica',10,'normal'),
                                 padx = 10,width = 8,bd = 2,bg = 'navy blue',fg = 'white',relief= 'flat',command=self.search_train_details)
        button4.place(x=530, y=100)

        button5 = Button(box_frame, text="Search",font = ('Helvetica',10,'normal'),
                                 padx = 10,width = 8,bd = 2,bg = 'navy blue',fg = 'white',relief= 'flat',command=self.search_driver_details)
        button5.place(x=530, y=150)

        button6 = Button(box_frame, text="Edit",font = ('Helvetica',10,'normal'),
                                 padx = 10,width = 8,bd = 2,bg = 'navy blue',fg = 'white',relief= 'flat',command=lambda: self.open_page4(self.Train_number.get()))
        button6.place(x=650, y=100)

        button7 = Button(box_frame, text="Edit",font = ('Helvetica',10,'normal'),
                                 padx = 10,width = 8,bd = 2,bg = 'navy blue',fg = 'white',relief= 'flat',command=lambda: self.open_page2(self.driver_irctc_entry.get()))
        button7.place(x=650, y=150)

        button7 = Button(box_frame, text="Add Cities",font = ('Helvetica',15,'normal'),
                                 padx = 10,width = 15,bd = 2,bg = 'navy blue',fg = 'white',relief= 'flat',command=self.open_page5)
        button7.place(x=50, y=400)

        button3 = Button(box_frame, text="Add New Driver",font = ('Helvetica',15,'normal'),
                                 padx = 10,width = 15,bd = 2,bg = 'navy blue',fg = 'white',relief= 'flat',command=self.open_page1)
        button3.place(x=550, y=400)

        button2 = Button(box_frame, text="Back",font = ('Helvetica',10,'normal'),
                                 padx = 10,width = 8,bd = 2,bg = 'navy blue',fg = 'white',relief= 'flat',command=self.open_page)
        button2.place(x=30, y=20)

        self.train_name_label = Label(box_frame, font=('New Times Roman', 15, 'normal'), text="Train Name:", padx=2, pady=2, bg="white", fg="navy blue")
        self.train_name_label.place(x=10, y=220)
        self.train_name_label.place_forget()

        self.source_station_label = Label(box_frame, font=('New Times Roman', 15, 'normal'), text="Source Station:", padx=2, pady=2, bg="white", fg="navy blue")
        self.source_station_label.place(x=200, y=220)
        self.source_station_label.place_forget()

        self.source_state_label = Label(box_frame, font=('New Times Roman', 15, 'normal'), text="Source State: ", padx=2, pady=2, bg="white", fg="navy blue")
        self.source_state_label.place(x=400, y=220)
        self.source_state_label.place_forget()
        

        self.destination_station_label = Label(box_frame, font=('New Times Roman', 15, 'normal'), text="Dest Station:", padx=2, pady=2, bg="white", fg="navy blue")
        self.destination_station_label.place(x=130, y=260)
        self.destination_station_label.place_forget()

        self.destination_state_label = Label(box_frame, font=('New Times Roman', 15, 'normal'), text="Dest State:", padx=2, pady=2, bg="white", fg="navy blue")
        self.destination_state_label.place(x=130, y=260)
        self.destination_state_label.place_forget()

        self.startTime_label = Label(box_frame, font=('New Times Roman', 15, 'normal'), text="Start Time:", padx=2, pady=2, bg="white", fg="navy blue")
        self.startTime_label.place(x=400, y=260)
        self.startTime_label.place_forget()

        self.endTime_label = Label(box_frame, font=('New Times Roman', 15, 'normal'), text="End Time:", padx=2, pady=2, bg="white", fg="navy blue")
        self.endTime_label.place(x=130, y=290)
        self.endTime_label.place_forget()

        # -------------------------------------------------------------------------
        self.first_name_label = Label(box_frame, font=('New Times Roman', 15, 'normal'), text="First Name:", padx=2, pady=2, bg="white", fg="navy blue")
        self.first_name_label.place(x=160, y=220)
        self.first_name_label.place_forget()

        self.last_name_label = Label(box_frame, font=('New Times Roman', 15, 'normal'), text="Last Name:", padx=2, pady=2, bg="white", fg="navy blue")
        self.last_name_label.place(x=200, y=220)
        self.last_name_label.place_forget()

        self.dob_label = Label(box_frame, font=('New Times Roman', 15, 'normal'), text="DOB:", padx=2, pady=2, bg="white", fg="navy blue")
        self.dob_label.place(x=400, y=220)
        self.dob_label.place_forget()
        

        self.address_label = Label(box_frame, font=('New Times Roman', 15, 'normal'), text="Address:", padx=2, pady=2, bg="white", fg="navy blue")
        self.address_label.place(x=130, y=240)
        self.address_label.place_forget()

        self.city_label = Label(box_frame, font=('New Times Roman', 15, 'normal'), text="City:", padx=2, pady=2, bg="white", fg="navy blue")
        self.city_label.place(x=130, y=260)
        self.city_label.place_forget()

        self.state_label = Label(box_frame, font=('New Times Roman', 15, 'normal'), text="State:", padx=2, pady=2, bg="white", fg="navy blue")
        self.state_label.place(x=400, y=260)
        self.state_label.place_forget()

        self.year_of_join_label = Label(box_frame, font=('New Times Roman', 15, 'normal'), text="Year of Join:", padx=2, pady=2, bg="white", fg="navy blue")
        self.year_of_join_label.place(x=130, y=290)
        self.year_of_join_label.place_forget()


    def open_page(self):
        from Railway import Railway
        self.root.withdraw()  # Hide the current window
        page2_window = Toplevel(self.root)  # Create a new window
        page2 = Railway(page2_window)  # Initialize Page2 in the new window

    def open_page5(self):
        from Stations import ADD_STATIONS
        self.root.withdraw()  # Hide the current window
        page2_window = Toplevel(self.root)  # Create a new window
        page2 = ADD_STATIONS(page2_window)  # Initialize Page2 in the new window

    def open_page1(self):
        from add_driver import ADD_DRIVER
        self.root.withdraw()  # Hide the current window
        page2_window = Toplevel(self.root)  # Create a new window
        page2 = ADD_DRIVER(page2_window)  # Initialize Page2 in the new window

    def open_page3(self):
        from add_train import ADD_TRAIN
        self.root.withdraw()  # Hide the current window
        page2_window = Toplevel(self.root)  # Create a new window
        page2 = ADD_TRAIN(page2_window)  # Initialize Page2 in the new window

    def open_page2(self, irctc_id):
        try:
            # Establish connection to MySQL
            mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='roshni',
                database='railway'
            )

            # Create a cursor object to execute SQL queries
            cursor = mydb.cursor()

            # Define SQL query to fetch train details based on IRCTC ID
            sql_query = "SELECT * FROM driver WHERE IRCTC_ID = %s"

            # Execute the SQL query
            cursor.execute(sql_query, (irctc_id,))

            # Fetch train details
            driver_details = cursor.fetchone()

            # Close the cursor and connection
            cursor.close()
            mydb.close()

            # If driver details are found, open the ADD_DRIVER page with initial values
            if driver_details:
                # Open the ADD_DRIVER page and pass initial values
                from add_driver import ADD_DRIVER
                self.root.withdraw()  # Hide the current window
                page2_window = Toplevel(self.root)  # Create a new window
                page2 = ADD_DRIVER(page2_window, driver_details)  # Pass initial values to ADD_DRIVER
            else:
                tkinter.messagebox.showerror("Error", "No driver details found for the given IRCTC ID")

        except mysql.connector.Error as error:
            # Show error message
            tkinter.messagebox.showerror("Error", f"Error fetching driver details: {error}")

    def open_page4(self, Train_Number):
        try:
            # Establish connection to MySQL
            mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                passwd='roshni',
                database='railway'
            )

            # Create a cursor object to execute SQL queries
            cursor = mydb.cursor()

            # Define SQL query to fetch train details based on IRCTC ID
            sql_query = "SELECT * FROM train WHERE Train_Number = %s"

            # Execute the SQL query
            cursor.execute(sql_query, (Train_Number,))

            # Fetch train details
            train_details = cursor.fetchone()

            # Close the cursor and connection
            cursor.close()
            mydb.close()

            # If driver details are found, open the ADD_DRIVER page with initial values
            if train_details:
                # Open the ADD_DRIVER page and pass initial values
                from add_train import ADD_TRAIN
                self.root.withdraw()  # Hide the current window
                page2_window = Toplevel(self.root)  # Create a new window
                page2 = ADD_TRAIN(page2_window, train_details)  # Pass initial values to ADD_DRIVER
            else:
                tkinter.messagebox.showerror("Error", "No driver details found for the given IRCTC ID")

        except mysql.connector.Error as error:
            # Show error message
            tkinter.messagebox.showerror("Error", f"Error fetching driver details: {error}")
    
    def search_driver_details(self):
    # Retrieve the IRCTC ID entered by the user
        irctc_id = self.driver_irctc_entry.get()

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

            # Define the SELECT query
            sql_query = "SELECT * FROM driver WHERE IRCTC_ID = %s"

            # Execute the SELECT query with the IRCTC ID parameter
            cursor.execute(sql_query, (irctc_id,))

            # Fetch the result
            driver_details = cursor.fetchone()

            # Close the cursor and connection
            cursor.close()
            mydb.close()

            # If driver details are found, display them on the interface
            if driver_details:
                # Assuming you have Label widgets to display the details
                # For example:
                self.clear_train_details()
                self.first_name_label.config(text=driver_details[1])
                self.first_name_label.place(x=70, y=220)
                self.last_name_label.config(text=(driver_details[2]))   # Last Name
                self.last_name_label.place(x=130, y=220)
                self.dob_label.config(text= driver_details[3])         # DOB
                self.dob_label.place(x=300, y=220)
                self.address_label.config(text=driver_details[4])
                self.address_label.place(x=70,y =250)
                self.city_label.config(text=driver_details[5])
                self.city_label.place(x=70,y=280)
                self.state_label.config(text=driver_details[6])
                self.state_label.place(x=250,y=280)
                self.year_of_join_label.config(text=driver_details[7])
                self.year_of_join_label.place(x=70,y=330)
                
                # Similarly for other details

            else:
                # If no driver details are found, show a message
                tkinter.messagebox.showinfo("Driver Not Found", "No driver details found for the provided IRCTC ID.")
        except mysql.connector.Error as error:
            # Show error message if any error occurs
            tkinter.messagebox.showerror("Error", f"Error searching driver details: {error}")

    def search_train_details(self):
    # Retrieve the IRCTC ID entered by the user
        train_number = self.Train_number.get()

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

            # Define the SELECT query
            sql_query = "SELECT * FROM train WHERE Train_Number = %s"

            # Execute the SELECT query with the IRCTC ID parameter
            cursor.execute(sql_query, (train_number,))

            # Fetch the result
            train_details = cursor.fetchone()

            # Close the cursor and connection
            cursor.close()
            mydb.close()

            # If driver details are found, display them on the interface
            if train_details:
                # Assuming you have Label widgets to display the details
                # For example:
                self.clear_driver_details()
                self.train_name_label.config(text=train_details[1])
                self.train_name_label.place(x=120, y=220)
                self.source_station_label.config(text=(train_details[2]))   # Last Name
                self.source_station_label.place(x=130, y=250)
                self.source_state_label.config(text= train_details[3])         # DOB
                self.source_state_label.place(x=130, y=280)
                self.destination_station_label.config(text=train_details[4])
                self.destination_station_label.place(x=300,y = 250)
                self.destination_state_label.config(text=train_details[5])
                self.destination_state_label.place(x=300,y=280)
                self.startTime_label.config(text=train_details[6])
                self.startTime_label.place(x=130,y=330)
                self.endTime_label.config(text=train_details[7])
                self.endTime_label.place(x=300,y=330)
                
                # Similarly for other details

            else:
                # If no driver details are found, show a message
                tkinter.messagebox.showinfo("Train Not Found", "No Train details found for the provided Train Number.")
        except mysql.connector.Error as error:
            # Show error message if any error occurs
            tkinter.messagebox.showerror("Error", f"Error searching driver details: {error}")

    def clear_driver_details(self):
    # Clear the labels for driver details
        self.first_name_label.config(text="",bg='white')
        self.last_name_label.config(text="",bg='white')
        self.dob_label.config(text="",bg='white')
        self.address_label.config(text="",bg='white')
        self.city_label.config(text="",bg='white')
        self.state_label.config(text="",bg='white')
        self.year_of_join_label.config(text="",bg='white')
        # Clear other labels for driver details

    def clear_train_details(self):
    # Clear the labels for train details
        self.train_name_label.config(text="",bg='white')
        self.source_station_label.config(text="",bg='white')
        self.source_state_label.config(text="",bg='white')
        self.destination_station_label.config(text="",bg='white')
        self.destination_state_label.config(text="",bg='white')
        self.startTime_label.config(text="",bg='white')
        self.endTime_label.config(text="",bg='white')
    # Clear other labels for train details


if __name__=='__main__':
    root = Tk()
    application = EP(root)
    clock = Label(root, font=('calibri', 15, 'bold'), bg='black', fg='red', bd=10, relief='groove',highlightbackground='black', highlightthickness=2)
    clock.place(x=1000, y=120)
    tick()
    root.mainloop()
