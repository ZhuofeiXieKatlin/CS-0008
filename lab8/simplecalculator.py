from tkinter import *
import math

class Calculator:
    def __init__(self):
        # Create the main window
        self.window = Tk()
        
        # Assign a title for this window
        self.window.title('Simple Calculator')
        
        # Place an Entry widget in the window to accept input
        self.display = StringVar()
        entrybox = Entry(self.window, relief=SUNKEN, textvariable = self.display)
        entrybox.pack(side=TOP, expand=YES, fill=BOTH)
        
        frameA=Frame(self.window)
        frameA.pack(side=TOP, expand=YES, fill=BOTH)
        self.firstbutton = Button(frameA, text='1', command=self.func1)   ### command tells which method is executed
        self.firstbutton.pack(side=LEFT, expand=YES, fill=BOTH)          
        self.secondbutton = Button(frameA, text='2', command=self.func2)  ### text tells what is displayed on this button
        self.secondbutton.pack(side=LEFT, expand=YES, fill=BOTH) 
        self.thirdbutton = Button(frameA, text='3', command=self.func3)  ### text tells what is displayed on this button
        self.thirdbutton.pack(side=LEFT, expand=YES, fill=BOTH)         
        
        frameB=Frame(self.window)
        frameB.pack(side=TOP, expand=YES, fill=BOTH)
        self.firstbutton = Button(frameB, text='4', command=self.func4)   ### command tells which method is executed
        self.firstbutton.pack(side=LEFT, expand=YES, fill=BOTH)          
        self.secondbutton = Button(frameB, text='5', command=self.func5)  ### text tells what is displayed on this button
        self.secondbutton.pack(side=LEFT, expand=YES, fill=BOTH) 
        self.thirdbutton = Button(frameB, text='6', command=self.func6)  ### text tells what is displayed on this button
        self.thirdbutton.pack(side=LEFT, expand=YES, fill=BOTH)  
        
        frameC=Frame(self.window)
        frameC.pack(side=TOP, expand=YES, fill=BOTH)
        self.firstbutton = Button(frameC, text='7', command=self.func7)   ### command tells which method is executed
        self.firstbutton.pack(side=LEFT, expand=YES, fill=BOTH)          
        self.secondbutton = Button(frameC, text='8', command=self.func8)  ### text tells what is displayed on this button
        self.secondbutton.pack(side=LEFT, expand=YES, fill=BOTH) 
        self.thirdbutton = Button(frameC, text='9', command=self.func9)  ### text tells what is displayed on this button
        self.thirdbutton.pack(side=LEFT, expand=YES, fill=BOTH)                 
        # Enter tkinter main loop
        
        frameD=Frame(self.window)
        frameD.pack(side=TOP, expand=YES, fill=BOTH)
        self.firstbutton = Button(frameD, text='-', command=self.func10)   ### command tells which method is executed
        self.firstbutton.pack(side=LEFT, expand=YES, fill=BOTH)          
        self.secondbutton = Button(frameD, text='0', command=self.func11)  ### text tells what is displayed on this button
        self.secondbutton.pack(side=LEFT, expand=YES, fill=BOTH) 
        self.thirdbutton = Button(frameD, text='.', command=self.func12)  ### text tells what is displayed on this button
        self.thirdbutton.pack(side=LEFT, expand=YES, fill=BOTH)
        
        frameD=Frame(self.window)
        frameD.pack(side=TOP, expand=YES, fill=BOTH)
        self.firstbutton = Button(frameD, text='+', command=self.func13)   ### command tells which method is executed
        self.firstbutton.pack(side=LEFT, expand=YES, fill=BOTH)          
        self.secondbutton = Button(frameD, text='-', command=self.func14)  ### text tells what is displayed on this button
        self.secondbutton.pack(side=LEFT, expand=YES, fill=BOTH) 
        self.thirdbutton = Button(frameD, text='*', command=self.func15)  ### text tells what is displayed on this button
        self.thirdbutton.pack(side=LEFT, expand=YES, fill=BOTH)     
        self.thirdbutton = Button(frameD, text='/', command=self.func16)  ### text tells what is displayed on this button
        self.thirdbutton.pack(side=LEFT, expand=YES, fill=BOTH)   
        self.thirdbutton = Button(frameD, text='=', command=self.func17)  ### text tells what is displayed on this button
        self.thirdbutton.pack(side=LEFT, expand=YES, fill=BOTH)  
        
        frameE=Frame(self.window)
        frameE.pack(side=TOP, expand=YES, fill=BOTH)
        self.firstbutton = Button(frameE, text='Clr', command=self.func18)   ### command tells which method is executed
        self.firstbutton.pack(side=LEFT, expand=YES, fill=BOTH)          
            
        mainloop()
    def func1(self):
        self.display.set(self.display.get()+'1')   
    def func2(self):
        self.display.set(self.display.get()+'2')   
    def func3(self):
        self.display.set(self.display.get()+'3')   
    def func4(self):
        self.display.set(self.display.get()+'4')   
    def func5(self):
        self.display.set(self.display.get()+'5')   
    def func6(self):
        self.display.set(self.display.get()+'6')      
    def func7(self):
        self.display.set(self.display.get()+'7')   
    def func8(self):
        self.display.set(self.display.get()+'8')   
    def func9(self):
        self.display.set(self.display.get()+'9')        
    def func10(self):
        self.display.set('-'+self.display.get())     
    def func11(self):
        self.display.set(self.display.get()+'0')        
    def func12(self):
        self.display.set(self.display.get()+'.')        
    def func13(self):
        self.display.set(self.display.get()+'+')   
    def func14(self):
        self.display.set(self.display.get()+'-')   
    def func15(self):
        self.display.set(self.display.get()+'*')   
    def func16(self):
        self.display.set(self.display.get()+'/') 
    def func17(self):
        try:
            result= eval(self.display.get())
            self.display.set(self.display.get()+'='+str(result))
        except:
            self.display.set("Error")  
        
    def func18(self):
        self.display.set(" ")  
    
def main():        
    gui = Calculator()
    
    
main()