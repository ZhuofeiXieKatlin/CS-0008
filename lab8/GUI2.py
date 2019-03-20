from tkinter import *

class GUI2:
    def __init__(self):
        # Create the main window
        self.window = Tk()
        
        # Assign a title for this window
        self.window.title('Window, You name it!')
        
        # Create a Frame in which to place the Buttons
        frame = Frame(self.window)
        frame.pack(side=TOP, expand=YES, fill=BOTH)
        
        
        # Place first Button widget into frame
        self.firstbutton = Button(frame, text='1st', command=self.func1)   ### command tells which method is executed
        self.firstbutton.pack(side=LEFT, expand=YES, fill=BOTH)            ### when this button is pressed
        
        # Place second Button widget into frame
        self.secondbutton = Button(frame, text='2nd', command=self.func2)  ### text tells what is displayed on this button
        self.secondbutton.pack(side=LEFT, expand=YES, fill=BOTH)        
        
        # Enter tkinter main loop
        mainloop()
        
        
    def func1(self):
        print('The 1st button has been pressed!')
        
        
    def func2(self):
        print('The 2nd button has been pressed!')
        
        
gui = GUI2()