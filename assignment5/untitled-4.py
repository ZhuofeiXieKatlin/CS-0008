from tkinter import *

class TextGUI:
    def __init__(self):
        # Create the main window
        self.window = Tk()
        
        # Assign a title for this window
        self.window.title('Text Widget Example')
        
        frame1 = Frame(self.window, bg = 'white')
        frame1.pack(side=TOP, expand=YES, fill=Y)
       
        frame2 = Frame(self.window, bg = 'yellow')
        frame2.pack(side=TOP, expand=YES, fill=BOTH) 
        
        frame3 = Frame(self.window, bg= 'green')
        frame3.pack(side=TOP, expand=YES, fill=BOTH) 
        
        label = Label(frame1, text = "Text Widget Below")
        label.pack(side=LEFT)        
        
        self.text = Text(frame2, height=20, width=50)          ### define Text widget
        scroll = Scrollbar(frame2, command=self.text.yview)    ### companion scroll bar
        self.text.configure(yscrollcommand=scroll.set)  
        self.text.pack(side=LEFT)
        scroll.pack(side=RIGHT, fill=Y)           
        
        clearbutton = Button(frame3, text = 'Clear', command = self.clear)
        clearbutton.pack(side=TOP)
        
        writebutton = Button(frame3, text = 'Write', command = self.write)
        writebutton.pack(side=TOP)
        
        # Enter tkinter main loop
        mainloop()
        
        
    def clear(self):    ### to be implemented later
        pass
    
    
    def write(self):    ### to be implemented later
        pass
    
        
def main():        
    gui = TextGUI()
            
            
main()