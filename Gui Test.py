from tkinter import *
from tkinter import ttk


# this file is just a test file for learning how to use the tkinter module. each commented out portion is a different test


root = Tk()
"""
commented out portions are past commands
root.title ("First Gui")

ttk.Button(root, text = "Hello There").grid()
"""
"""
frame = Frame(root)

labelText = StringVar()

label = Label( frame, textvariable=labelText )

button = Button (frame, text = "click")

labelText.set("I am a label")

label.pack()
button.pack()
frame.pack()

"""
"""
frame = Frame(root)

Label(frame, text="A Bunch of Buttons").pack()

Button(frame, text='B1').pack(side=LEFT, fill = Y) 
Button(frame, text='B2').pack(side=TOP, fill = X)
Button(frame, text='B3').pack(side=RIGHT, fill = X)
Button(frame, text='B4').pack(side=LEFT, fill = X) 

frame.pack()
"""
"""
Label(root, text = 'first name').grid(row=0, sticky=W,padx=4)
Entry (root).grid(row=0, column = 1, sticky=E, pady=4)

Label(root, text = 'last name').grid(row=1, sticky=W,padx=4)
Entry (root).grid(row=1, column = 1, sticky=E, pady=4)


Button (root, text ='submit').grid(row=3)

"""
"""
Label(root, text ='description').grid(row=0, column =0 , sticky=W)
Entry(root, width=50).grid(row=0,column=1)
Button(root, text ='submit').grid(row=0,column=8)

Label (root,text="quality").grid(row=1, column=0,sticky=W)
Radiobutton(root, text = 'New', value = 1).grid(row = 2, column = 0 , sticky=W)
Radiobutton(root, text = 'good', value =2).grid(row = 3, column = 0 , sticky=W)
Radiobutton(root, text = 'Poor', value = 3).grid(row = 4, column = 0 , sticky=W)
Radiobutton(root, text = 'Damaged', value= 4).grid(row = 5, column = 0 , sticky=W)

Label(root, text= 'Benefits').grid(row=1,column = 1, sticky = W)
Checkbutton(root, text = 'free Shipping').grid(row= 2 ,column =1 , sticky = W)
Checkbutton(root, text = 'is a gift').grid(row= 3 ,column =1 , sticky = W) 
"""
"""
def get_sum(event):
    num1 = int (num1Entry.get())
    num2 = int (num2Entry.get())
    sum = num1 + num2

    sumEntry.delete(0, "end")
    sumEntry.insert(0,sum)

num1Entry = Entry(root)
num1Entry.pack(side=LEFT)

Label(root, text = "+").pack(side = LEFT)

num2Entry = Entry(root)
num2Entry.pack(side=LEFT)

equalButton = Button(root, text = "=")
equalButton.bind( "<Button-1>", get_sum)
equalButton.pack(side= LEFT)

sumEntry = Entry(root)
sumEntry.pack(side=LEFT)
"""

from tkinter import messagebox
"""
def get_data(event=None):

    print('String :', strVar.get())
    print('Integer :', intVar.get())
    print('Double :', dblVar.get())
    print('Boolean :', boolVar.get())

def bind_button(event=None):

    if ( boolVar.get()):
         getDataButton.unbind('<Button-1>')
    else:
        getDataButton.bind('<Button-1>', get_data)
    
strVar = StringVar()
intVar = IntVar()
dblVar = DoubleVar()
boolVar = BooleanVar()

strVar.set("Enter String")
intVar.set('Enter Integer')
dblVar.set('Enter Double')
boolVar.set(True)

strEntry = Entry(root, textvariable = strVar)
strEntry.pack(side=LEFT)

intEntry = Entry(root, textvariable = intVar)
intEntry.pack(side=LEFT)

dblEntry = Entry(root, textvariable = dblVar)
dblEntry.pack(side=LEFT)

theCheckBut = Checkbutton(root, text='Switch', variable = boolVar)
theCheckBut.bind('<Button-1>', bind_button)
theCheckBut.pack(side=LEFT)

getDataButton = Button(root, text = 'get data')
getDataButton.bind('<Button-1>', get_data) 
getDataButton.pack(side=LEFT)

"""
"""
def open_msg_box():
    messagebox.showwarning(
        'Event Triggered',
        'Button Clicked'
    )

root.geometry('400x400+300+300')
root.resizable(width=False, height=False)
frame = Frame(root)
style = tkk.Style()

style.configure('TButton',
                foreground= 'midnight blue',
                font = 'Times 20 bold italic',
                padding = 20)
"""

"""

#menu testing
 
def quit_app():
    root.quit()

def show_about(event=None):
    
    messagebox.showwarning(
        'About',
        'This Awesome Program was Made in 2016'
    )



the_menu=Menu(root)
#menu

file_menu = Menu(the_menu, tearoff=0)

file_menu.add_command(label="Open")
file_menu.add_command( label = 'Save')
file_menu.add_separator()
file_menu.add_command( label = 'Quit', command = quit_app)

the_menu.add_cascade( label = 'File', menu= file_menu)
#fonts

text_font = StringVar()
text_font.set("Times")

def change_font(event=None):
    print("Font Picked :", text_font.get())

font_menu = Menu(the_menu, tearoff = 0)

font_menu.add_radiobutton(label="Times",
                         variable = text_font,
                         command=change_font)
font_menu.add_radiobutton(label="Courier",
                         variable = text_font,
                         command=change_font)
font_menu.add_radiobutton(label="Ariel",
                         variable = text_font,
                         command=change_font)
    
# view

view_menu = Menu( the_menu, tearoff = 0)

line_numbers = IntVar()
line_numbers.set(1)

view_menu.add_checkbutton(label = 'Line Numbers',
                          variable = line_numbers)

the_menu.add_cascade(label = "Fonts", menu= font_menu)

the_menu.add_cascade(label = 'View', menu=view_menu)

#help

help_menu = Menu(the_menu, tearoff=0)

help_menu. add_command(label='About',
                       accelerator = 'command-A',
                       command=show_about)

the_menu.add_cascade(label='Help', menu=help_menu)



root.bind('<Command-A>', show_about)


root.config(menu =the_menu)
"""

#canvas testing
import tkinter.font

#define class
class PaintApp:

#define class variables
    drawing_tool = 'line'

    left_but = 'up'

    x_pos, y_pos = None, None

    x1_line_pt, y1_line_pt, x2_line_pt , y2_line_pt= None, None, None, None
    

#Catch mouse up
    def left_but_down(self, event = None):
        self .left_but= 'down'

        self.x1_line_pt = event.x
        self.y1_line_pt = event.y

#catch mouse down
    def left_but_up(self, event=None):

        self.left_but= "up"

        self.x_pos = None
        self.y_pos=  None

        self.x2_line_pt = event.x
        self.y2_line_pt = event.y

        if(self.drawing_tool == "line"):
            self.line_draw(event)

# catch mouse Move
    def motion( self, event=None):
        if( self.drawing_tool == "pencil" :
            self.pencil_draw(event) 
            
           
    

# draw pencil

    def pencil_draw(self, event = None):
        
        if self.left_but == "down":
            if self.x_pos is not None and self.y_pos is not None:
            
                event.widget.create_line( self.x_pos, self.y_pos, event.x, event.y, smooth = TRUE)

            self.x_pos = event_x
            self.y_pos = event_y 
#draw line

    def line_draw(self,event = None):

        if None not in ( self.x1_line_pt, self.y1_line_pt, self x2_line_pt, self.y2_line_pt):
            event.widget. create_line( self.x1_line_pt, self.y1_line_pt, self x2_line_pt, self.y2_line_pt, smooth = TRUE, fill = 'green')
# draw arc

#draw Oval

# draw rectangle

# draw test

#initialize

    def __init__ ( self, root) :
        drawing_area = Canvas(root)
        drawing_area.pack()


        drawing_area.bind("<Motion>". self.motion )
        drawing_area.bind("<ButtonPress-1>". self.left_but_down )
        drawing_area.bind("<ButtonRelease-1>". self.left_but_up )

        





paint_app = PaintApp(root)
root.mainloop()













    







