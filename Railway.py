from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import *
from PIL import ImageTk, Image
import time
from datetime import datetime
from pnr_status import PNR_STATUS
from Vacancy import VACANCY
from Employee_Management import EP
from datetime import datetime


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

def login(UserName,Password,self):
    # Check if the username and password are correct
        if UserName.get() == "admin" and Password.get() == "ras":
            # Call the function if the username and password are correct
            self.root.withdraw()  # Hide the current window
            page2_window = Toplevel(self.root)  # Create a new window
            page2 = EP(page2_window)  # Initialize Page2 in the new window

        else:
            # Display an error message if the username and password are incorrect
            messagebox.showerror("Error", "Invalid username or password")


class Railway:
    def __init__(self,root):
        self.root = root
        self.root.title("Indian Railways")
        self.root.geometry("1432x950+0+0")

        From = StringVar()
        To = StringVar()
        UserName = StringVar()
        Password = StringVar()

        logo_image = Image.open("Railway Management System\\IRCTC-logo.png")
        self.logo_photo = ImageTk.PhotoImage(logo_image)

        self.root.iconphoto(False, self.logo_photo)

        bg_image = Image.open("Railway Management System\\42839304.jpg")
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = Label(self.root, image=self.bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        navbar = Frame(root, bg="white", height=120, width=root.winfo_screenwidth())
        navbar.place(x=0, y=0)

        box_frame = Frame(root, bg="white", height=500, width=600)
        box_frame.place(x=100, y=130)

        # navbar1 = Frame(root, bg="blue", height=10, width=root.winfo_screenwidth())
        # navbar1.place(x=0, y=120)

        image1 = Image.open("Railway Management System\\IR logo Blue color.jpg")
        image2 = Image.open("Railway Management System\\IRCTC-logo.png")
        image3 = Image.open("Railway Management System\\a.jpg")

        image1 = image1.resize((100, 100))
        image2 = image2.resize((100, 100))
        #image3 = image3.resize((60, 60))

        self.photo1 = ImageTk.PhotoImage(image1)
        self.photo2 = ImageTk.PhotoImage(image2)
       # self.photo3 = ImageTk.PhotoImage(image3)

        left_frame = Frame(navbar, bg="white", width=200, height=110)
        left_frame.place(x=10, y=10)

        label1 = Label(left_frame, image=self.photo1,borderwidth=0)
        label1.place(x=0, y=0)

        center_frame = Frame(navbar, bg="white", width=1100, height=110)
        center_frame.place(x=220, y=10)

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

        #label3 = Label(box_frame,image=self.photo3,borderwidth=0)
        #label3.place(x=160,y=190)

        button1 = Button(box_frame, text="Check Booking Status",font = ('Helvetica',16,'normal'),
                                 padx = 10,width = 29,bd = 4,bg = 'navy blue',fg = 'white',relief= 'flat',command=self.open_page2)
        button1.place(x=100, y=10)


        #button2 = Button(box_frame, text="Charts/Vacancy", font=('Helvetica', 16, 'normal'),
        #          padx=4, width=13, height=1, bd=4, bg='navy blue', fg='white', relief='flat',command=self.open_page3)
        # button2.place(x=210, y=10)


        Box_Framelabel = LabelFrame(box_frame, bd=0, width=350, height=30, relief=RIDGE, fg='navy blue',
                            bg='white', font=('arial', 20, 'bold'), text="SEARCH TRAINS")
        Box_Framelabel.place(x=100, y=80)

        self.From = Label(box_frame, font = ('New Times Roman',12,'normal'),text = "From :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.From.place(x=40,y=140)
        self.From = Entry(box_frame, font = ('New Times Roman',12,'normal'),textvariable=From,width=20)
        self.From.place(x=120,y=140)

        self.To = Label(box_frame, font = ('New Times Roman',12,'normal'),text = "To :",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.To.place(x=56,y=200)
        self.To = Entry(box_frame, font = ('New Times Roman',12,'normal'),textvariable=To,width=20)
        self.To.place(x=120,y=200)

        self.lblDate = Label(box_frame, font = ('New Times Roman',12,'normal'),text = "Date:",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.lblDate.place(x=40,y=250)

        current_date = datetime.now().date()
        self.date_entry = DateEntry(box_frame, width=12, background='darkblue', foreground='white', borderwidth=2,mindate=current_date)
        self.date_entry.place(x=130, y=250)


        button3 = Button(box_frame, text="Submit",font = ('arial',13,'bold'),
                                 padx = 10,width = 7,height=1,bd = 4,bg = 'orange',fg = 'white',relief= 'flat',command=lambda:self.open_page4(self.From,self.To))
        button3.place(x=150, y=280)

        self.lblDate = Label(box_frame, font = ('New Times Roman',12,'normal'),text = "------------------------------------------------------------------------------",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.lblDate.place(x=0,y=320)

        self.lblDate = Label(box_frame, font = ('New Times Roman',12,'bold'),text = "For Admin Login",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.lblDate.place(x=40,y=350)


        self.User = Label(box_frame, font = ('New Times Roman',12,'normal'),text = "Username:",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.User.place(x=40,y=380)
        self.User = Entry(box_frame, font = ('New Times Roman',12,'normal'),textvariable=UserName,width=15)
        self.User.place(x=150,y=380)

        self.Pass = Label(box_frame, font = ('New Times Roman',12,'normal'),text = "Password:",padx = 2,pady = 2,bg="white",fg="navy blue")
        self.Pass.place(x=40,y=420)
        self.Pass = Entry(box_frame, font = ('New Times Roman',12,'normal'),textvariable=Password,width=15,show="*")
        self.Pass.place(x=150,y=420)

        button3 = Button(box_frame, text="Admin",font = ('arial',13,'bold'),
                                 padx = 10,width = 7,height=1,bd = 4,bg = 'darkblue',fg = 'white',relief= 'flat',command=lambda:login(UserName, Password,self))
        button3.place(x=150, y=460)

    def open_page2(self):
            self.root.withdraw()  # Hide the current window
            page2_window = Toplevel(self.root)  # Create a new window
            page2 = PNR_STATUS(page2_window)  # Initialize Page2 in the new window

    def open_page3(self):
            self.root.withdraw()  # Hide the current window
            page2_window = Toplevel(self.root)  # Create a new window
            page2 = VACANCY(page2_window)  # Initialize Page2 in the new window


    def open_page4(self,From,To):
            from Train_List import TRAIN_LIST
            self.root.withdraw()  # Hide the current window
            selected_date = self.date_entry.get_date()
            if selected_date is not None:
                day_of_week_number = selected_date.weekday()
                day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                day_name = day_names[day_of_week_number]
                print("Selected day of the week:", day_name)
            else:
                print("No date selected.")
            from_value = From.get()
            to_value = To.get()
            page2_window = Toplevel(self.root)  # Create a new window
            page2 = TRAIN_LIST(page2_window,from_value,to_value,day_name,selected_date)  # Initialize Page2 in the new window

    


if __name__=='__main__':
    root = Tk()
    application = Railway(root)
    clock = Label(root, font=('calibri', 15, 'bold'), bg='black', fg='red', bd=10, relief='groove',highlightbackground='black', highlightthickness=2)
    clock.place(x=1000, y=120)
    tick()
    root.mainloop()
