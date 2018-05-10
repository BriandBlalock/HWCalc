from tkinter import *
#from tkinter import ttk
import tkinter.font
import numpy as np

root = Tk()
class GUI:

    displayString = StringVar()

    grid = []

    input_row_offset = 5
    input_column_offset = 5

    is_writing = True

    def create_display(self):

        display = Entry(root, text=self.displayString,  borderwidth=1, relief="solid")
        display.grid(row=1, rowspan=3, column=0, columnspan=15, padx=1, pady=5)


    def fill(self,Event):
        if( self.is_writing ):

            but = Event.widget
            but.configure(bg='black')

            index = np.where(self.grid == but )
            x = index[0][0]

            y = index[1][0]

            color = "#cccccc"


            if( y-1>=0 and self.grid[x][y-1]['bg']=='white'):
                self.grid[x][y - 1]['bg'] = color

            if (y+1<16 and self.grid[x][y+1]['bg'] == 'white' ):
                self.grid[x][y + 1]['bg'] = color

            if (x-1>=0 and self.grid[x-1][y]['bg'] == 'white' ):
                self.grid[x-1][y]['bg'] = color

            if (x+1 <16 and self.grid[x+1][y]['bg'] == 'white'):
                self.grid[x+1][y]['bg'] = color



    def toggle_writing_on(self, Event=None):
        is_writing = True

    def toggle_writing_off(self, Event=None):
        is_writing = False

    def create_grid(self):

        # frame.bind  ``("<Button-1>", self.toggle_writing_on)
        # frame.bind("<ButtonRelease-1>", self.toggle_writing_off)

        for x in range(16):

            list = []

            for y in range(16):

                list.append( Button(root, bd = 1, text="   ", bg='white') )

                list[y].bind("<Motion>", self.fill)
                list[y].grid( row=x+self.input_row_offset, column=y+self.input_column_offset, padx=0, pady=0 )

            self.grid.append(list)

        self.grid = np.array(self.grid)

    def clear_grid(self, Event):

        for x in range(16):

            for y in range(16):

                self.grid[x][y].configure(bg= 'white')

    def create_buttons(self):

        clear = Button (root, text = "clear")
        clear.grid( row = 6, column = 24)
        clear.bind("<Button-1>", self.clear_grid)


    def __init__(self, root):

        root.geometry('400x450')
        root.resizable(width=False, height=False)
        root.bind_all("<ButtonPress-1>",self.toggle_writing_on() )
        root.bind_all("<ButtonRelease-1>", self.toggle_writing_off())
        self.create_display()
        self.create_grid()
        self.create_buttons()








def main ():


    gui = GUI(root)
    root.mainloop()


main()