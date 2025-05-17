from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tkcalendar import *
from PIL import ImageTk, Image
import time
import datetime

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

class VACANCY:
    def __init__(self,root):
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

        box_frame = Frame(root, bg="white", height=500, width=800)
        box_frame.place(x=150, y=130)

        pnr_heading = Label(box_frame, text="VACANCY", font=('Helvetica', 20, 'bold'), bg="white", fg="navy blue")
        pnr_heading.place(x=300, y=40)

        # Instruction text
        pnr_instruction = Label(box_frame, text="Enter your Train Number to check the Vacancy", font=('Helvetica', 16), bg="white", fg="navy blue")
        pnr_instruction.place(x=170, y=120)
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
        self.PNR.place(x=150,y=200)
        self.PNR = Entry(box_frame, font = ('New Times Roman',16,'normal'),textvariable=PNR,width=20)
        self.PNR.place(x=250,y=200)

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

        button1 = Button(box_frame, text="Check",font = ('Helvetica',10,'normal'),
                                 padx = 10,width = 8,bd = 2,bg = 'navy blue',fg = 'white',relief= 'flat')
        button1.place(x=320, y=280)

    def open_page(self):
        from Railway import Railway
        self.root.withdraw()  # Hide the current window
        page2_window = Toplevel(self.root)  # Create a new window
        page2 = Railway(page2_window)  # Initialize Page2 in the new window
    

if __name__=='__main__':
    root = Tk()
    application = VACANCY(root)
    clock = Label(root, font=('calibri', 15, 'bold'), bg='black', fg='red', bd=10, relief='groove',highlightbackground='black', highlightthickness=2)
    clock.place(x=1000, y=120)
    tick()
    root.mainloop()
