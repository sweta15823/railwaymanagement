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

class TRAIN_LIST:
    def __init__(self,root,From=None,To=None,Day_Value=None,Date=None):
        self.root = root
        self.root.title("Indian Railways")
        self.root.geometry("1432x950+0+0")

        PNR = StringVar()

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

        box_frame = Frame(root, bg="white", height=600, width=800)
        box_frame.place(x=150, y=180)

        self.create_table(box_frame,From,To,Day_Value,Date)


        # ------------------
        pnr_heading = Label(box_frame, text="TRAINS AVAILABLE ON ROUTE", font=('Helvetica', 20, 'bold'), bg="white", fg="navy blue")
        pnr_heading.place(x=200, y=20)

        # Instruction text
        # pnr_instruction = Label(box_frame, text="Enter your Train Number to check the Vacancy", font=('Helvetica', 16), bg="white", fg="navy blue")
        # pnr_instruction.place(x=170, y=120)
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
        label2.place(x=370, y=70)
        self.From = Label(box_frame, font = ('New Times Roman',18,'bold'),text = From,padx = 2,pady = 2,bg="white",fg="navy blue")
        self.From.place(x=180,y=87)

        self.To = Label(box_frame, font = ('New Times Roman',18,'bold'),text = To,padx = 2,pady = 2,bg="white",fg="navy blue")
        self.To.place(x=560,y=87)

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


    def open_page(self):
        from Railway import Railway
        self.root.withdraw()  # Hide the current window
        page2_window = Toplevel(self.root)  # Create a new window
        page2 = Railway(page2_window)  # Initialize Page2 in the new window
    

    def create_table(self, box_frame, From, To, Day_Value,Date):
    # Establish connection to MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='roshni',
            database='railway'
        )
        cursor = connection.cursor()

        From = str(From).upper()
        To = str(To).upper()

        # Query to find train numbers from TrainRoute table where both 'From' and 'To' are present and 'From' index is smaller than 'To' index
        query_route = "SELECT Train_Number, City, Time FROM trainroute WHERE City LIKE %s AND City LIKE %s"
        cursor.execute(query_route, ('%' + From + '%', '%' + To + '%'))
        train_routes = cursor.fetchall()
        

        self.tree = ttk.Treeview(box_frame, columns=("1", "2", "3", "4"), show="headings")
        self.tree.heading("1", text="Train Number")
        self.tree.heading("2", text="Train Name")
        self.tree.heading("3", text="Start Time")
        self.tree.heading("4", text="End Time")

        self.tree.column("1", width=105, anchor='center')
        self.tree.column("2", width=275, anchor='center')
        self.tree.column("3", width=100, anchor='center')
        self.tree.column("4", width=100, anchor='center')

        if not train_routes:
            # If no train number is found, display "None" in each column of the display table
            self.tree.insert("", "end", values=("None", "None", "None", "None"))
        else:
            for train_route in train_routes:
                train_number = train_route[0]
                cities = train_route[1].split(',')  # Split the cities by comma
                times = train_route[2].split(',')  # Split the times by comma
                
                # Query Train table to get the days associated with the train
                query_days = "SELECT Days FROM train WHERE Train_Number = %s"
                cursor.execute(query_days, (train_number,))
                train_days = cursor.fetchone()[0]  # Fetch the days associated with the train
                
                if train_days and str(Day_Value).upper() in train_days.split(','):
                    from_index = cities.index(From)
                    to_index = cities.index(To)
                    start_time = times[from_index]  # Get the time corresponding to the 'From' city index
                    end_time = times[to_index]  # Get the time corresponding to the 'To' city index
                    
                    # Query Train table to get Train Name based on train number
                    query_train = "SELECT Train_Name_value FROM train WHERE Train_Number = %s"
                    cursor.execute(query_train, (train_number,))
                    train_name = cursor.fetchone()[0]  # Fetch the train name
                    self.tree.insert("", "end", values=(train_number, train_name, start_time, end_time))
 
            self.tree.place(x=50, y=150, width=700, height=400) 

            vsb = ttk.Scrollbar(box_frame, orient="vertical", command=self.tree.yview)
            vsb.place(x=750, y=150, height=400)
            self.tree.configure(yscrollcommand=vsb.set)
            
            

            self.tree.bind("<<TreeviewSelect>>", lambda event, From=From, To=To: self.open_selected_row(event, From, To,Date,Day_Value))
 

 
        def open_selected_row(self, event, From, To,Date,Day):
            selected_item = self.tree.selection()[0]
            train_number = self.tree.item(selected_item, "values")[0]
            # Open new page or perform action based on selected train number and additional parameters
    
            from Train_Details import TrainDetails   # Import the class of the new page
            self.root.withdraw()  # Hide the current window
            page2_window = Toplevel(self.root)  # Create a new window
            page2 = TrainDetails(page2_window, From, To, train_number,Date,Day)
 
 
 
 
if __name__=='__main__':
    root = Tk()
    application = TRAIN_LIST(root)
    clock = Label(root, font=('calibri', 15, 'bold'), bg='black', fg='red', bd=10, relief='groove',highlightbackground='black', highlightthickness=2)
    clock.place(x=1000, y=120)
    tick()
