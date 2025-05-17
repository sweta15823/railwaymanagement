from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkcalendar import *
from PIL import ImageTk, Image
import time
import datetime
from tkinter.ttk import Combobox
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

class ADD_TRAIN:
    def __init__(self,root,initial_values=None):
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
        self.Middle_Cities = StringVar()
        self.Middle_States = StringVar()
        self.Middle_Time = StringVar()
        self.Class = StringVar()
        self.Base_Price = StringVar()
        self.PerKm = StringVar()
        
        if initial_values:
            self.Train_name.set(initial_values[1])
            self.Driver.set(initial_values[2])
            self.Source_City.set(initial_values[3])
            self.Source_State.set(initial_values[4])
            self.Destination_City.set(initial_values[5])
            self.Destination_State.set(initial_values[6])
            self.StartTime.set(initial_values[7])
            self.End_Time.set(initial_values[8])
            self.Days.set(initial_values[9])

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

        box_frame = Frame(root, bg="white", height=500, width=915)
        box_frame.place(x=80, y=130)

        pnr_heading = Label(box_frame, text="ADD TRAIN DETAILS", font=('Helvetica', 20, 'bold'), bg="white", fg="navy blue")
        pnr_heading.place(x=280, y=10)

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

        self.Train_number = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "Train Number :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Train_number.place(x=130,y=50)
        self.Train_number = Entry(box_frame, font = ('New Times Roman',12,'bold'),textvariable=self.Train_number,width=36)
        self.Train_number.place(x=130,y=80)

        self.Train_name = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "Train Name :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Train_name.place(x=500,y=50)
        self.Train_name = Entry(box_frame, font = ('New Times Roman',12,'bold'),textvariable=self.Train_name,width=36)
        self.Train_name.place(x=500,y=80)

        self.Source_City = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "Source City :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Source_City.place(x=130,y=110)
        self.Source_City = Entry(box_frame, font = ('New Times Roman',12,'bold'),textvariable=self.Source_City,width=20)
        self.Source_City.place(x=130,y=140)

        self.Source_State = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "Source State :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Source_State.place(x=130,y=180)
        self.Source_State = Entry(box_frame, font = ('New Times Roman',12,'bold'),textvariable=self.Source_State,width=20)
        self.Source_State.place(x=130,y=210)

        self.Dest_City = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "Destination City :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Dest_City.place(x=670,y=110)
        self.Dest_City = Entry(box_frame, font = ('New Times Roman',12,'bold'),textvariable=self.Destination_City,width=20)
        self.Dest_City.place(x=670,y=140)

        self.Dest_State = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "Destination State :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Dest_State.place(x=670,y=180)
        self.Dest_State = Entry(box_frame, font = ('New Times Roman',12,'bold'),textvariable=self.Destination_State,width=20)
        self.Dest_State.place(x=670,y=210)

        self.Days = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "Days :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Days.place(x=130,y=240)
        self.Days = Entry(box_frame, font = ('New Times Roman',12,'bold'),textvariable=self.Days,width=50)
        self.Days.place(x=130,y=270)

        self.Start_Time = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "Start Time :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Start_Time.place(x=130,y=300)
        self.Start_Time = Entry(box_frame, font = ('New Times Roman',12,'bold'),textvariable=self.StartTime,width=20)
        self.Start_Time.place(x=130,y=330)

        self.End_Time = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "End Time :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.End_Time.place(x=670,y=300)
        self.End_Time = Entry(box_frame, font = ('New Times Roman',12,'bold'),textvariable=self.EndTime,width=20)
        self.End_Time.place(x=670,y=330)

        self.Middle_Time = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "Middle Time :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Middle_Time.place(x=400,y=300)
        self.Middle_Time = Entry(box_frame, font = ('New Times Roman',12,'bold'),textvariable=self.Middle_Time,width=20)
        self.Middle_Time.place(x=400,y=330)

        self.driver_names = self.get_driver_names()  # Fetch available driver names
        self.driver_name_label = Label(box_frame, font=('New Times Roman', 12, 'bold'), text="Driver Name:", padx=2, pady=2, bg="white", fg="navy blue")
        self.driver_name_label.place(x=670, y=240)
        self.driver_name_combobox = Combobox(box_frame, values=self.driver_names, width=25)
        self.driver_name_combobox.place(x=670, y=270)

        self.Middle_Cities = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "Middle Cities :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Middle_Cities.place(x=400,y=110)
        self.Middle_Cities = Entry(box_frame, font = ('New Times Roman',12,'bold'),textvariable=self.Middle_Cities,width=20)
        self.Middle_Cities.place(x=400,y=140)

        self.Middle_States = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "Middle States :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Middle_States.place(x=400,y=180)
        self.Middle_States = Entry(box_frame, font = ('New Times Roman',12,'bold'),textvariable=self.Middle_States,width=20)
        self.Middle_States.place(x=400,y=210)

        self.Class = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "Class :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Class.place(x=130,y=360)
        self.Class = Entry(box_frame, font = ('New Times Roman',12,'bold'),textvariable=self.Class,width=20)
        self.Class.place(x=130,y=390)

        self.Base_Price = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "Base Price :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Base_Price.place(x=400,y=360)
        self.Base_Price = Entry(box_frame, font = ('New Times Roman',12,'bold'),textvariable=self.Base_Price,width=20)
        self.Base_Price.place(x=400,y=390)

        self.PerKm = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "Per Km :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.PerKm.place(x=670,y=360)
        self.PerKm = Entry(box_frame, font = ('New Times Roman',12,'bold'),textvariable=self.PerKm,width=20)
        self.PerKm.place(x=670,y=390)

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
                                 padx = 10,width = 8,bd = 2,bg = 'navy blue',fg = 'white',relief= 'flat',command=self.add_train_to_database)
        button1.place(x=400, y=430)

    def get_driver_names(self):
        try:
            # Establish connection to MySQL
            mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                password='roshni',
                database='Railway'
            )

            # Create a cursor object to execute SQL queries
            cursor = mydb.cursor()

            # Fetch driver names and IRCTC IDs from the database
            cursor.execute("SELECT IRCTC_ID, First_name, Last_Name FROM driver")
            driver_data = cursor.fetchall()

            # Create a list of tuples containing both IRCTC_ID and concatenated first name and last name
            driver_info = [(driver[0], ' '.join(driver[1:])) for driver in driver_data]

            return driver_info
        except mysql.connector.Error as error:
            # Handle errors gracefully
            print(f"Error fetching driver names: {error}")
            return []
        finally:
            # Close the cursor and connection
            cursor.close()
            mydb.close()


    def add_train_to_database(self):
        # Retrieve values from entry widgets
        Train_Number_value = self.Train_number.get()
        Train_Name_value = self.Train_name.get()
        # Get the selected value from the Combobox
        selected_value = self.driver_name_combobox.get()

        # Split the selected value to extract IRCTC_ID
        irctc_id = selected_value.split()[0]  # Assuming IRCTC_ID is the first part of the selected value

        # Now irctc_id holds the IRCTC_ID from the selected value

        Source_City_value = self.Source_City.get()
        Source_State_value = self.Source_State.get()
        Destination_City_value = self.Dest_City.get()
        Destination_State_value = self.Dest_State.get()
        StartTime_value = self.Start_Time.get()
        EndTime_value = self.End_Time.get()
        Days_value = self.Days.get()
        middle_cities = self.Middle_Cities.get()
        middle_states = self.Middle_States.get()
        middle_time = self.Middle_Time.get()
        class_available = self.Class.get()
        base_fare = self.Base_Price.get()
        per_km = self.PerKm.get()

        try:
            # Establish connection to MySQL
            mydb = mysql.connector.connect(
                host='localhost',
                user = 'root',
                passwd = 'roshni',
                database="railway"
            )

            # Create a cursor object to execute SQL queries
            cursor = mydb.cursor()

            cursor.execute("SHOW TABLES LIKE 'train'")
            table_exists = cursor.fetchone()
            if table_exists:
                # Check if the driver already exists by IRCTC ID
                cursor.execute("SELECT * FROM train WHERE Train_Number = %s", (Train_Number_value,))
                existing_train = cursor.fetchone()
                if existing_train:
                # If driver exists, update the entry
                    sql_query = "UPDATE train SET Train_Name_value=%s, Source_Station=%s, Source_State=%s, Destination_Station=%s, Destination_State=%s, StartTime=%s, EndTime=%s, Days=%s WHERE Train_Number=%s"
                    values = (Train_Name_value.upper(), Source_City_value.upper(), Source_State_value.upper(), Destination_City_value.upper(), Destination_State_value.upper(), StartTime_value, EndTime_value, Days_value.upper(), Train_Number_value)

            
                else:
                    # If driver does not exist, insert a new entry
                    sql_query = "INSERT INTO train (Train_Number,Train_Name_value, Source_Station, Source_State, Destination_Station, Destination_State, StartTime, EndTime,Days) VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s)"
                    values = (Train_Number_value,Train_Name_value.upper(), Source_City_value.upper(),Source_State_value.upper(),Destination_City_value.upper(),Destination_State_value.upper(),StartTime_value,EndTime_value,Days_value.upper())
            cursor.execute(sql_query, values)


            cursor.execute("SELECT * FROM train_driver_assignment WHERE Train_Number = %s AND IRCTC_ID = %s", (Train_Number_value, irctc_id))
            existing_assignment = cursor.fetchone()
            if existing_assignment:
            # If the assignment exists, update the entry
                sql_update_assignment = "UPDATE train_driver_assignment SET IRCTC_ID = %s WHERE Train_Number = %s"
                values_update_assignment = (irctc_id, Train_Number_value)
                cursor.execute(sql_update_assignment, values_update_assignment)
            else:
            # If the assignment does not exist, insert a new entry
                sql_insert_assignment = "INSERT INTO train_driver_assignment (Train_Number, IRCTC_ID) VALUES (%s, %s)"
                values_assignment = (Train_Number_value, irctc_id)
                cursor.execute(sql_insert_assignment, values_assignment)

            # -------------------------------------
            cursor.execute("SELECT * FROM trainroute WHERE Train_Number = %s", (Train_Number_value,))
            existing_assignment = cursor.fetchone()
            if existing_assignment:
            #If the assignment exists, update the entry
                sql_update_assignment = "UPDATE trainroute SET City = %s, State = %s,Time = %s, Class = %s,BasePrice=%s,Per_Km_Price=%s WHERE Train_Number = %s"
                values_update_assignment = (Source_City_value.upper()+","+middle_cities.upper()+","+Destination_City_value.upper(),Source_State_value.upper()+","+middle_states.upper()+","+Destination_State_value.upper(),StartTime_value+","+middle_time+","+EndTime_value,class_available.upper(),base_fare,per_km,Train_Number_value)
                cursor.execute(sql_update_assignment, values_update_assignment)
            else:
            # If the assignment does not exist, insert a new entry
                sql_insert_assignment = "INSERT INTO trainroute (Train_Number,City,State,Time,Class,BasePrice,Per_Km_Price) VALUES (%s, %s, %s,%s,%s,%s,%s)"
                values_assignment = (Train_Number_value, Source_City_value.upper()+","+middle_cities.upper()+","+Destination_City_value.upper(),Source_State_value.upper()+","+middle_states.upper()+","+Destination_State_value.upper(),StartTime_value+","+middle_time+","+EndTime_value,class_available,base_fare,per_km)
                cursor.execute(sql_insert_assignment, values_assignment)
            # -----------------------------
            # Commit the changes
            mydb.commit()
            # Close the cursor and connection
            cursor.close()
            mydb.close()
            # Show success message
            tkinter.messagebox.showinfo("Success", "Train details added successfully!")
            self.clear_entry_boxes()
        except mysql.connector.Error as error:
            # Show error message
            tkinter.messagebox.showerror("Error", f"Error adding train details: {error}")

    def open_page(self):
        from Employee_Management import EP
        self.root.withdraw()  # Hide the current window
        page2_window = Toplevel(self.root)  # Create a new window
        page2 = EP(page2_window)  # Initialize Page2 in the new window

    def clear_entry_boxes(self):
        # Clear all the entry boxes
        self.Train_number.delete(0, 'end')
        self.Train_name.delete(0, 'end')
        self.Source_City.delete(0, 'end')
        self.Source_State.delete(0, 'end')
        self.Dest_City.delete(0, 'end')
        self.Dest_State.delete(0, 'end')
        self.Days.delete(0, 'end')
        self.Start_Time.delete(0, 'end')
        self.End_Time.delete(0, 'end')
        self.Middle_Cities.delete(0, 'end')
        self.Middle_States.delete(0, 'end')
        self.Middle_Time.delete(0, 'end')
        self.driver_name_combobox.set('')  # Clear the Combobox selection
        self.Class.delete(0,'end')
        self.Base_Price.delete(0,'end')
        self.PerKm.delete(0,'end')

if __name__=='__main__':
    root = Tk()
    application = ADD_TRAIN(root)
    clock = Label(root, font=('calibri', 15, 'bold'), bg='black', fg='red', bd=10, relief='groove',highlightbackground='black', highlightthickness=2)
    clock.place(x=1000, y=120)
    tick()
    root.mainloop()
