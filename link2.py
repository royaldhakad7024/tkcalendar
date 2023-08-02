from tkinter import *
from tkcalendar import *

root = Tk()
root.title('Codemy.com')
#root.iconbitmap('c:/gui/codemy.ico')
root.geometry("600x600")

cal=Calendar(root, selectmode="day",date_pattern='dd-mm-yyyy')
cal.pack(pady=20,fill='both',expand=True)
def grab_date():
    my_label.config(text="Today`s Date Is=" + cal.get_date())

my_button = Button(root, text="Get Date", command=grab_date)
my_button.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()