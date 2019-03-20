from tkinter import *

class GUI1:
    def __init__(self):
        # Create the main window
        self.window = Tk()
        
        # Assign a title for this window
        self.window.title('Window, You name it!')
        
        # Place an Entry widget in the window to accept input
        self.display = StringVar()
        entrybox = Entry(self.window, relief=SUNKEN, textvariable = self.display)
        entrybox.pack(side=TOP, expand=YES, fill=BOTH)
        
        # Enter tkinter main loop
        mainloop()


def main():        
    gui = GUI1()
    
    
main()