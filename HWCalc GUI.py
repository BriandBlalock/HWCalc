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
    grid_size = 20
    button_size = 1

    is_writing =  False

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

            """
            if( y-1>=0 and self.grid[x][y-1]['bg']=='white'):
                self.grid[x][y - 1]['bg'] = color

            if (y+1<self.grid_size and self.grid[x][y+1]['bg'] == 'white' ):
                self.grid[x][y + 1]['bg'] = color

            if (x-1>=0 and self.grid[x-1][y]['bg'] == 'white' ):
                self.grid[x-1][y]['bg'] = color

            if (x+1 <self.grid_size and self.grid[x+1][y]['bg'] == 'white'):
                self.grid[x+1][y]['bg'] = color
            """



    def toggle_writing(self, Event):
        self.is_writing = not(self.is_writing)




    def create_grid(self):  ##### Depricated, replaced by create Canvas #####

        # frame.bind  ``("<Button-1>", self.toggle_writing_on)
        # frame.bind("<ButtonRelease-1>", self.toggle_writing_off)

        for x in range(self.grid_size):

            list = []

            for y in range(self.grid_size):

                list.append( Button(root, bd = 1, text="", bg='white', height=self.button_size, width=self.button_size) )

                list[y].bind("<Motion>", self.fill)
                list[y].bind("<ButtonPress-1>", self.toggle_writing)
                list[y].grid( row=x+self.input_row_offset, column=y+self.input_column_offset, padx=0, pady=0 )

            self.grid.append(list)

        self.grid = np.array(self.grid)

    def create_canvas(self):

        draw_area = Canvas(root, width=20,height = 20  )
        draw_area.grid( row = self.input_row_offset, column=self.input_column_offset)



    def clear_grid(self, Event):

        for x in range(self.grid_size):

            for y in range(self.grid_size):

                self.grid[x][y].configure(bg= 'white')

    def create_buttons(self):

        clear = Button (root, text = "clear")
        clear.grid( row = 6, column = self.grid_size+7)
        clear.bind("<Button-1>", self.clear_grid)

        getV = Button(root, text="get Vals")
        getV.grid(row=8, column=self.grid_size + 7)
        getV.bind("<Button-1>", self.get_grid_values)


    def __init__(self, root):

        root.geometry('400x500')
        root.resizable(width=False, height=False)

        self.create_display()
        self.create_canvas()
        self.create_buttons()

    def get_grid_values(self, Event):

        returnList = []

        for xVal in self.grid:
            temp = []
            for yVal in xVal:

                if yVal['bg'] == "black":

                    temp.append(255)
                else:
                    temp.append(0)

            returnList.append(temp)

        for xVal in returnList:
            print(xVal)




def main ():

    gui = GUI(root)

    root.mainloop()


main()