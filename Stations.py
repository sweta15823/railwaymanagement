from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkcalendar import *
from PIL import ImageTk, Image
import time
import datetime
import mysql.connector
from tkinter.ttk import Combobox

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

class ADD_STATIONS:
    selected_date = None  # Initialize with None

    def __init__(self,root,initial_values=None):
        self.root = root
        self.root.title("Indian Railways")
        self.root.geometry("1432x950+0+0")

        self.Station = StringVar()
        self.Distance = StringVar()
        self.State = StringVar()
    
            

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

        box_frame = Frame(root, bg="white", height=500, width=500)
        box_frame.place(x=150, y=140)

        pnr_heading = Label(box_frame, text="ADD STATION DETAILS", font=('Helvetica', 20, 'bold'), bg="white", fg="navy blue")
        pnr_heading.place(x=100, y=50)

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

        

        self.Name_label = Label(box_frame, font=('New Times Roman', 15, 'bold'), text="Station: ", padx=2, pady=2, bg="white", fg="navy blue")
        self.Name_label.place(x=100, y=120)
        self.Name_label = Entry(box_frame, font=('New Times Roman', 15, 'bold'), textvariable=self.Station, width=30)
        self.Name_label.place(x=100, y=150)
        
        # Instead of overwriting the StringVar and DateEntry objects, create separate variables for labels and entry widgets
        self.distance_label = Label(box_frame, font=('New Times Roman', 15, 'bold'), text="Distance:", padx=2, pady=2, bg="white", fg="navy blue")
        self.distance_label.place(x=100, y=190)
        self.distance_label = Entry(box_frame, font=('New Times Roman', 15, 'bold'), textvariable=self.Distance, width=30)
        self.distance_label.place(x=100, y=220)

        self.State = Label(box_frame, font=('New Times Roman', 15, 'bold'), text="State:", padx=2, pady=2, bg="white", fg="navy blue")
        self.State.place(x=100, y=260)
        self.State = Entry(box_frame, font=('New Times Roman', 15, 'bold'), textvariable=self.State, width=30)
        self.State.place(x=100, y=300)


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
                                 padx = 10,width = 8,bd = 2,bg = 'navy blue',fg = 'white',relief= 'flat',command=self.add_station_to_database)
        button1.place(x=150, y=380)
    

    def open_page(self):
        from Employee_Management import EP
        self.root.withdraw()  # Hide the current window
        page2_window = Toplevel(self.root)  # Create a new window
        page2 = EP(page2_window)  # Initialize Page2 in the new window

    def add_station_to_database(self):
    # Retrieve values from entry widgets
        Station = self.Station.get()
        distance = self.Distance.get()
        state= self.State.get()

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

            # Check if the table exists
            # Check if the table exists
            cursor.execute("SHOW TABLES LIKE 'station'")
            table_exists = cursor.fetchone()

            if table_exists:
                # Check if the station already exists
                cursor.execute("SELECT * FROM station WHERE Station_Name = %s", (Station.upper(),))
                existing_station = cursor.fetchone()
                
                if existing_station:
                    # If station exists, update the entry
                    sql_query = "UPDATE station SET Distance_to_Next_Station = %s, State = %s WHERE Station_Name = %s"
                    values = (distance, state.upper(), Station.upper())
                else:
                    # If station does not exist, insert a new entry
                    sql_query = "INSERT INTO station (Station_Name, Distance_to_Next_Station, State) VALUES (%s, %s, %s)"
                    values = (Station.upper(), distance, state.upper())

                # Execute the SQL query with the appropriate values
                cursor.execute(sql_query, values)


                # Commit the changes
                mydb.commit()

                # Close the cursor and connection
                cursor.close()
                mydb.close()

                # Show success message
                tkinter.messagebox.showinfo("Success", "Station added successfully!")
                self.clear_entry_boxes()
            else:
                # Show error message if the table does not exist
                tkinter.messagebox.showerror("Error", "Station table does not exist!")
        except mysql.connector.Error as error:
            # Show error message
            tkinter.messagebox.showerror("Error", f"Error adding station details: {error}")

    def clear_entry_boxes(self):
        # Clear all the entry boxes
        self.Name_label.delete(0, 'end')
        self.distance_label.delete(0, 'end')
        self.State.delete(0, 'end')
        


if __name__=='__main__':
    root = Tk()
    application = ADD_STATIONS(root)
    clock = Label(root, font=('calibri', 15, 'bold'), bg='black', fg='red', bd=10, relief='groove',highlightbackground='black', highlightthickness=2)
    clock.place(x=1000, y=120)
    tick()
    root.mainloop()
