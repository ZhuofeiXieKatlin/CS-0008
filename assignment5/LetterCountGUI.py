from tkinter import *

class LetterCountGUI:
    def __init__(self):
        # create main window
        self.window=Tk()
        self.window.title("Letter count Aanlyzer")
    
        frametop = Frame(self.window, bg="yellow")
        frametop.pack(side=TOP,expand=YES,fill=BOTH)
    
        framemid = Frame(self.window, bg="green")
        framemid.pack(side=TOP,expand=YES,fill=BOTH)    
    
        framebot = Frame(self.window, bg="blue")
        framebot.pack(side=TOP,expand=YES,fill=BOTH)  
    
        label=Label(frametop,text='file name',bg='cyan')
        label.pack(side=LEFT)
    ### create entry widget
    
        self.display = StringVar()  
        filename_entry = Entry(frametop, width = 20, textvariable = self.display)    
    
        
        self.text = Text(frame2, height=20, width=50)          ### define Text widget
        scroll = Scrollbar(frame2, command=self.text.yview)    ### companion scroll bar
        self.text.configure(yscrollcommand=scroll.set)  
        self.text.pack(side=LEFT)
        scroll.pack(side=RIGHT, fill=Y)
        
        ### create buttoms
        clear_button = Button(framebot, text = 'Clear', command = self.clear)
        
        ### create exit 
        exit_button = Button(framebot, text = 'Clear', command = self.exit)
        
        process_button=
        
        label.pack(side=LEFT)
        filename_entry.pack(side=LEFT)
        process_button.pack(side=TOP)
        clear_button.pack(side=TOP)
        exit_button.pack(side=TOP)
        
        # Enter tkintermain loop
        mainloop()
    def clear(self):
        self.display.set('')
        self.text.delete('1.0',END)
    
    def exit(self):
        self.window.destroy()
        
    def process(self):
        file = self.display.get()
        dictionary=LetterCountGUI.read_txt(file)
        output=''
        for key,val in dictionary.items():
            output=output + '%-10s%d\n' % (key,val)
        self.txt.insert(END,str(dictionary))
    def read_txt(filename):
        filein = open(filename,'r')
        dictionary={}
        line = filein.readline()
        
        while line!="":
            
def main():
    gui = LetterCountGUI()

main()