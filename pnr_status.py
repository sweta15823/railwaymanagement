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

class PNR_STATUS:
    def __init__(self,root):
        self.root = root
        self.root.title("Indian Railways")
        self.root.geometry("1432x950+0+0")

        self.Passenger_ID = StringVar()

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

        pnr_heading = Label(box_frame, text="CHECK BOOKING STATUS", font=('Helvetica', 20, 'bold'), bg="white", fg="navy blue")
        pnr_heading.place(x=200, y=10)

        # Instruction text
        pnr_instruction = Label(box_frame, text="Enter your Adhaar number below to check status", font=('Helvetica', 16), bg="white", fg="navy blue")
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

        self.PNR = Label(box_frame, font = ('New Times Roman',16,'normal'),text = "Adhaar No :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.PNR.place(x=130,y=100)
        self.PNR = Entry(box_frame, font = ('New Times Roman',16,'normal'),textvariable=self.Passenger_ID,width=20)
        self.PNR.place(x=250,y=100)

        title_label = Label(center_frame, text="INDIAN RAILWAYS", font = ('Helvetica',30,'bold'), fg='navy blue',bg="white")
        title_label.place(x=315, y=0)

        tagline_label = Label(center_frame, text="Safety | Security | Punctuality", font = ('Helvetica',15), fg='navy blue',bg="white")
        tagline_label.place(x=356, y=50)

        right_frame = Frame(navbar, bg="white", width=200, height=110)
        right_frame.place(x=1222, y=10)

        label2 = Label(right_frame, image=self.photo2,borderwidth=0)
        label2.place(x=100, y=0)

        button1 = Button(box_frame, text="Check",font = ('Helvetica',10,'normal'),
                                 padx = 10,width = 8,bd = 2,bg = 'navy blue',fg = 'white',relief= 'flat',command=self.search_passenger_details)
        button1.place(x=320, y=150)

        pnr_instruction = Label(box_frame, text="-----------------------------------------------------------------------------------------------------------------", font=('Helvetica', 16), bg="white", fg="navy blue")
        pnr_instruction.place(x=0, y=190)

        button2 = Button(box_frame, text="Back",font = ('Helvetica',10,'normal'),
                                 padx = 10,width = 8,bd = 2,bg = 'navy blue',fg = 'white',relief= 'flat',command=self.open_page)
        button2.place(x=30, y=20)

        self.First_name = Label(box_frame, font = ('New Times Roman',16,'bold'),text = "FirstName :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.First_name.place(x=50,y=280)

        self.Status = Label(box_frame, font = ('New Times Roman',16,'bold'),text = "Status:",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Status.place(x=300,y=240)

        self.Last_name = Label(box_frame, font = ('New Times Roman',16,'bold'),text = "LastName :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Last_name.place(x=50,y=320)
        
        self.Train_number = Label(box_frame, font = ('New Times Roman',16,'bold'),text = "Train No :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Train_number.place(x=300,y=350)
        

        self.Train_name = Label(box_frame, font = ('New Times Roman',16,'bold'),text = "Train Name :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Train_name.place(x=300,y=390)
        

        self.Class = Label(box_frame, font = ('New Times Roman',16,'bold'),text = "Class :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Class.place(x=500,y=280)
        

        self.Date = Label(box_frame, font = ('New Times Roman',16,'bold'),text = "Date :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Date.place(x=650,y=280)
        

        self.Amount = Label(box_frame, font = ('New Times Roman',16,'bold'),text = "Amount :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Amount.place(x=650,y=530)
        

        self.From = Label(box_frame, font = ('New Times Roman',16,'bold'),text = "From :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.From.place(x=50,y=430)
        
        self.T = Label(box_frame, font = ('New Times Roman',16,'bold'),text = "<==========>",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.T.place(x=250,y=430)

        self.To = Label(box_frame, font = ('New Times Roman',16,'bold'),text = "To :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.To.place(x=450,y=430)


    def open_page(self):
        from Railway import Railway
        self.root.withdraw()  # Hide the current window
        page2_window = Toplevel(self.root)  # Create a new window
        page2 = Railway(page2_window)  # Initialize Page2 in the new window

    def search_passenger_details(self):
    # Retrieve the IRCTC ID entered by the user
        passenger_id = self.Passenger_ID.get()

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
            sql_query = "SELECT * FROM train_passenger_details WHERE Passenger_ID = %s"
            sql_query1 = "SELECT FirstName,LastName FROM passenger WHERE Passenger_ID = %s"

            # Execute the SELECT query with the IRCTC ID parameter
            cursor.execute(sql_query, (passenger_id,))

            # Fetch the result
            passenger_details = cursor.fetchone()

            cursor.execute(sql_query1,(passenger_id,))
            passenger_name = cursor.fetchone()

            train_number = passenger_details[0]
            sql_query2 = "SELECT Train_Name_value FROM train WHERE Train_Number = %s"
            cursor.execute(sql_query2,(train_number,))
            train_name = cursor.fetchone()

            # Close the cursor and connection
            cursor.close()
            mydb.close()

            # If driver details are found, display them on the interface
            if (train_name and passenger_name and passenger_details):
                # Assuming you have Label widgets to display the details
                # For example:
                self.clear_driver_details()
                self.First_name.config(text=passenger_name[0])
                self.First_name.place(x=50,y=280)
                self.Last_name.config(text=passenger_name[1])   # Last Name
                self.Last_name.place(x=50,y=320)
                self.Train_number.config(text= passenger_details[0])         # DOB
                self.Train_number.place(x=300,y=350)
                self.Train_name.config(text=train_name)
                self.Train_name.place(x=300,y=390)
                self.Class.config(text=passenger_details[2])
                self.Class.place(x=500,y=280)
                self.Date.config(text=passenger_details[3])
                self.Date.place(x=650,y=280)
                self.Amount.config(text=f"Rs:{passenger_details[6]}")
                self.Amount.place(x=650,y=530)
                self.From.config(text=passenger_details[4])
                self.From.place(x=50,y=430)
                self.To.config(text=passenger_details[5])
                self.To.place(x=450,y=430)
                self.Status.config(text="Status: Payment Received")
                self.Status.place(x=300,y=240)


                
                # Similarly for other details

            else:
                # If no driver details are found, show a message
                tkinter.messagebox.showinfo("Train Not Found", "No Train details found for the provided Train Number.")
        except mysql.connector.Error as error:
            # Show error message if any error occurs
            tkinter.messagebox.showerror("Error", f"Error searching driver details: {error}")

    def clear_driver_details(self):
    # Clear the labels for driver details
        self.First_name.config(text="",bg='white')
        self.Last_name.config(text="",bg='white')
        self.Train_number.config(text="",bg='white')
        self.Train_name.config(text="",bg='white')
        self.Class.config(text="",bg='white')
        self.Date.config(text="",bg='white')
        self.Amount.config(text="",bg='white')
        self.From.config(text="",bg='white')
        self.To.config(text="",bg='white')
        self.Status.config(text="",bg='white')
        # Clear other labels for driver details

if __name__=='__main__':
    root = Tk()
    application = PNR_STATUS(root)
    clock = Label(root, font=('calibri', 15, 'bold'), bg='black', fg='red', bd=10, relief='groove',highlightbackground='black', highlightthickness=2)
    clock.place(x=1000, y=120)
    tick()
    root.mainloop()
