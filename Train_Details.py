from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
from PIL import ImageTk, Image
import time
from datetime import datetime
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

class TrainDetails:
    def __init__(self,root,From=None,To=None,Train_Number=None,Date=None,Day=None):
        self.root = root
        self.root.title("Indian Railways")
        self.root.geometry("1432x950+0+0")

        self.Train_Number = IntVar()
        self.Train_name = StringVar()
        self.Source_City = StringVar()
        self.Source_State = StringVar()
        self.Destination_City = StringVar()
        self.Destination_State = StringVar()
        self.StartTime = StringVar()
        self.EndTime = StringVar()
       

        logo_image = Image.open("Railway Management System\\IRCTC-logo.png")
        self.logo_photo = ImageTk.PhotoImage(logo_image)

        self.root.iconphoto(False, self.logo_photo)

        bg_image = Image.open("Railway Management System\\42839304.jpg")
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        navbar = Frame(root, bg="white", height=120, width=root.winfo_screenwidth())
        navbar.place(x=0, y=0)

        box_frame = Frame(root, bg="white", height=500, width=1100)
        box_frame.place(x=100, y=140)

        # navbar1 = Frame(root, bg="blue", height=10, width=root.winfo_screenwidth())
        # navbar1.place(x=0, y=120)

        image1 = Image.open("Railway Management System\\IR logo Blue color.jpg")
        image2 = Image.open("Railway Management System\\IRCTC-logo.png")
        gif_image = Image.open("Railway Management System\\ix.jpg")

        image1 = image1.resize((100, 100))
        image2 = image2.resize((100, 100))
        image3 = gif_image.resize((100,80))

        self.photo1 = ImageTk.PhotoImage(image1)
        self.photo2 = ImageTk.PhotoImage(image2)
        self.photo3 = ImageTk.PhotoImage(image3)

        left_frame = Frame(navbar, bg="white", width=200, height=110)
        left_frame.place(x=10, y=10)

        label1 = Label(left_frame, image=self.photo1,borderwidth=0)
        label1.place(x=0, y=0)

        center_frame = Frame(navbar, bg="white", width=1100, height=110)
        center_frame.place(x=220, y=10)

        label2 = Label(box_frame, image=self.photo3,borderwidth=0)
        label2.place(x=345, y=170)
 
        self.train_number_label = Label(box_frame, font = ('New Times Roman',18,'bold'),text = "Train_Number",padx = 2,pady = 2,bg="white",fg="orange")
        self.train_number_label.place(x=350,y=40)

        self.train_name_label = Label(box_frame, font = ('New Times Roman',18,'bold'),text = "Train_Name",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.train_name_label.place(x=150,y=87)

        self.source_city_label = Label(box_frame, font = ('New Times Roman',18,'bold'),text = "From",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.source_city_label.place(x=130,y=220)

        self.destination_city_label = Label(box_frame, font = ('New Times Roman',18,'bold'),text = "To",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.destination_city_label.place(x=560,y=220)

        self.source_state_label = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "State1",padx = 2,pady = 2,bg="white",fg="orange")
        self.source_state_label.place(x=120,y=270)

        self.destination_state_label = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "State2",padx = 2,pady = 2,bg="white",fg="orange")
        self.destination_state_label.place(x=540,y=270)

        self.startTime_label = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "00:00:00",padx = 2,pady = 2,bg="white",fg="black")
        self.startTime_label.place(x=150,y=180)

        self.endTime_label = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "00:00:00",padx = 2,pady = 2,bg="white",fg="black")
        self.endTime_label.place(x=570,y=180)


    
        self.search_train_details(From,To,Train_Number,box_frame)
        self.populate_classes_and_prices(box_frame,Train_Number,Date,From,To,Day)

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
                                 padx = 10,width = 8,bd = 2,bg = 'navy blue',fg = 'white',relief= 'flat',command=lambda:self.open_page(From,To,Day))
        button2.place(x=30, y=20)
        # ------------------------------------------------------------------------------------
    def search_train_details(self,From,To,train_number,box_frame):
    # Retrieve the IRCTC ID entered by the user
        # train_number = self.Train_Number.get()
        train_name = self.Train_name.get()
        start_time = self.StartTime.get()
        end_time = self.EndTime.get()
        source_city = self.Source_City.get()
        source_state = self.Source_State.get()
        dest_city = self.Destination_City.get()
        dest_state = self.Destination_State.get()

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
            sql_query = "SELECT Train_Name_value FROM train WHERE Train_Number = %s"

            # Execute the SELECT query with the IRCTC ID parameter
            cursor.execute(sql_query, (train_number,))

            # Fetch the result
            train_name = cursor.fetchone()

            query_route = "SELECT City,State,Time FROM trainroute WHERE City LIKE %s AND City LIKE %s AND Train_Number = %s"

            cursor.execute(query_route, ('%' +' From '+ '%', '%' + 'To'+ '%', train_number))
            train_routes = cursor.fetchall()

            
            # Execute the SELECT query with the IRCTC ID parameter
            cursor.close()
            mydb.close()

            # If driver details are found, display them on the interface
            if (train_routes):
                for train_route in train_routes:
                    cities = train_route[0].split(',')  # Split the cities by comma
                    print(cities)
                    states = train_route[1].split(',')
                    times = train_route[2].split(',')  # Split the times by comma
                    # Find the index of 'From' and 'To' in the cities list
                    from_index = cities.index(From)
                    to_index = cities.index(To)
                    start_time = times[from_index]  # Get the time corresponding to the 'From' city index
                    end_time = times[to_index]  # Get the time corresponding to the 'To' city index
                    # Query Train table to get Train Name based on train number
                    source_state = states[from_index]
                    dest_state = states[to_index]

            # Assuming you have Label widgets to display the details
                # For example:
                
                self.train_number_label.config(text=train_number)
                self.train_number_label.place(x=350,y=40)
                self.train_name_label.config(text=train_name)   # Last Name
                self.train_name_label.place(x=150,y=87)
                self.source_city_label.config(text=From)         # DOB
                self.source_city_label.place(x=130,y=220)
                self.destination_city_label.config(text=To)
                self.destination_city_label.place(x=560,y=220)
                self.source_state_label.config(text=source_state)         # DOB
                self.source_state_label.place(x=120,y=270)
                self.destination_state_label.config(text=dest_state)
                self.destination_state_label.place(x=540,y=270)
                self.startTime_label.config(text=start_time)
                self.startTime_label.place(x=150,y=180)
                self.endTime_label.config(text=end_time)
                self.endTime_label.place(x=570,y=180)

               # Initialize previous_state variable to None
                previous_state = None

                for i, (city, state, time) in enumerate(zip(cities, states, times)):
                    # Check if the state has changed compared to the previous iteration
                    if state != previous_state:
                        # If the state has changed, create a label to display the state name
                        state_label = Label(box_frame, text=f"{state}",
                                            font=('New Times Roman', 12, 'bold'), padx=2, pady=2, bg="white", fg="orange")
                        state_label.place(x=850, y=80 + i * 60)  # Adjust y position based on index
                        previous_state = state  # Update previous_state variable
                        
                    # Create a label to display the city and time
                    city_label = Label(box_frame, text=f"{city}: {time}",
                                    font=('New Times Roman', 12, 'bold'), padx=2, pady=2, bg="white", fg="navy blue")
                    city_label.place(x=950, y=100 + i *60)  # Adjust y position based on index


            else:
                # If no driver details are found, show a message
                messagebox.showinfo("Train Not Found", "No Train details found for the provided Train Number.")
        except mysql.connector.Error as error:
            # Show error message if any error occurs
            messagebox.showerror("Error", f"Error searching driver details: {error}")
        # -----------------------------------------------------------------------------------
    def check_passenger_limit(self,train_number):
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

            # Define the SQL query to count passengers for each class in the train
            sql_query = """
                SELECT Class, COUNT(*) AS PassengerCount
                FROM train_passenger_details
                WHERE train_number = %s
                GROUP BY Class
            """

            # Execute the query with the train number as parameter
            cursor.execute(sql_query, (train_number,))

            # Fetch all rows
            passenger_counts = cursor.fetchall()

            # Close the cursor and connection
            cursor.close()
            mydb.close()

            # Check if any class exceeds the limit
            for class_name, count in passenger_counts:
                if count >= 30:
                    return False  # Passenger limit exceeded
            return True  # Passenger limit not exceeded
        except mysql.connector.Error as error:
            # Show error message
            messagebox.showerror("Error", f"Error checking passenger limit: {error}")
            return False

    def fetch_classes_and_prices(self,train_number):
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

            # Define the SELECT query to fetch classes and prices from the Train table
            sql_query = "SELECT Class, BasePrice,Per_Km_Price FROM trainroute WHERE Train_Number=%s"

            # Execute the query
            cursor.execute(sql_query,(train_number,))

            # Fetch all rows
            train_data = cursor.fetchall()
            print(train_data)

            # Close the cursor and connection
            cursor.close()
            mydb.close()

            # Return the fetched data
            return train_data
        except mysql.connector.Error as error:
            # Show error message
            messagebox.showerror("Error", f"Error fetching classes and prices: {error}")
            return []
        
    def populate_classes_and_prices(self, box_frame, Train_Number, Date, From, To, Day):
    # Fetch classes and prices from the database
        train_data = self.fetch_classes_and_prices(Train_Number)
        print(train_data)

        from_city = str(self.get_distance(From))
        to_city = str(self.get_distance(To))
        km =str(from_city + to_city)
        if train_data:
            for i, data in enumerate(train_data):
                # Extract class names, base prices, and per kilometer prices from the data
                class_names, baseprices, perkms = data[0].split(','), data[1].split(','), data[2].split(',')
                print("Class names:", class_names)
                print("Prices:", baseprices)
                print("PerKm:", perkms)

                x_position = 150  # Initial x position for the labels

                for class_name, baseprice, perkm in zip(class_names, baseprices, perkms):
                    print("Class name:", class_name)
                    print("Price:", baseprice)
                    print("PerKm", perkm)
                    # Create label for class name
                    class_label = Label(box_frame, font=('New Times Roman', 18, 'bold'), text=class_name,
                                        padx=2, pady=2, bg="white", fg="navy blue")
                    class_label.place(x=x_position, y=350)  # Adjust x position based on index

                    # Calculate the price including per kilometer charge
                    total_price = float(baseprice) + (float(perkm) * float(km))

                    # Create label for price
                    price_label = Label(box_frame, font=('New Times Roman', 12, 'bold'),
                                        text=f"Rs {total_price}", padx=2, pady=2, bg="white", fg="black")
                    price_label.place(x=x_position + 10, y=390)  # Adjust x position based on index

                    # Create button
                    button = Button(box_frame, text="Checking...", font=('Helvetica', 10, 'normal'),
                                    padx=10, width=8, bd=2, bg='orange', fg='white', relief='flat', state="disabled",
                                    command=lambda class_name=class_name,total_price=total_price: self.open_page2(class_name, Date, Train_Number, From, To, Day,total_price))

                    button.place(x=x_position, y=430)  # Adjust x position based on index

                    # Increment x position for the next label and button
                    x_position += 200  # Adjust this value as needed for the desired spacing

                    self.root.after(0, self.update_button_status, Train_Number, button)


    
        # ------------------------------------------------------------------------------------
    def update_button_status(self, train_number, button):
        # Check passenger limit for the given train number
        if self.check_passenger_limit(train_number):
            button.config(state="normal", text="Book")
        else:
            button.config(state="disabled", text="Full")

    def get_distance(self, city):
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

            # Define the SELECT query to fetch classes and prices from the Train table
            sql_query = "SELECT Distance_to_Next_Station FROM station WHERE Station_Name = %s"

            # Execute the query
            cursor.execute(sql_query, (city,))

            # Fetch the first row
            distance_record = cursor.fetchone()

            # Close the cursor and connection
            cursor.close()
            mydb.close()

            # If a distance record is found, return the distance value as a string
            if distance_record:
                distance = str(distance_record[0])
                return distance
            else:
                # If no record is found, return None or an appropriate default value
                return None
        except mysql.connector.Error as error:
            # Show error message
            messagebox.showerror("Error", f"Error fetching distance: {error}")
            return None


    def open_page(self,From,To,Day):
        from Train_List import TRAIN_LIST
        self.root.withdraw()  # Hide the current window
        page2_window = Toplevel(self.root)  # Create a new window
        page2 = TRAIN_LIST(page2_window,From,To,Day)  # Initialize Page2 in the new 

    def open_page2(self,class_name,Date,Train_Number,From,To,Day,total_price):
        from Passenger import Passenger
        self.root.withdraw()  # Hide the current window
        page2_window = Toplevel(self.root)  # Create a new window
        page2 = Passenger(page2_window,From,To,Train_Number,Date,class_name,Day,total_price)  # Initialize Page2 in the new  


if __name__=='__main__':
    root = Tk()
    application = TrainDetails(root)
    clock = Label(root, font=('calibri', 15, 'bold'), bg='black', fg='red', bd=10, relief='groove',highlightbackground='black', highlightthickness=2)
    clock.place(x=1000, y=120)
    tick()
    root.mainloop()
