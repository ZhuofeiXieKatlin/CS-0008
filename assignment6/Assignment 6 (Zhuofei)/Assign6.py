'''
Name: Zhuofei Xie

Date created: 2017/12/10

Purpose: Using Gui to create a project that can run the txt file in the text box. We need to how to create different button
Sample run(s):

Hank                  1971    495     90     22      3     47      0.327    0.669

<dimaggio.txt>
Joe DiMaggio          1936    637    118     44     15     29      0.323    0.576
Joe DiMaggio          1937    621    119     35     15     46      0.346    0.673
Joe DiMaggio          1938    660    117     32     13     32      0.294    0.527
Joe DiMaggio          1939    524    108     32      6     30      0.336    0.592
Joe DiMaggio          1940    572    111     28      9     31      0.313    0.556
Joe DiMaggio          1941    622    109     43     11     30      0.310    0.559
Joe DiMaggio          1942    680    123     29     13     21      0.274    0.447
Joe DiMaggio          1946    567     93     20      8     25      0.257    0.453
Joe DiMaggio          1947    601    107     31     10     20      0.280    0.464
Joe DiMaggio          1948    669    114     26     11     39      0.284    0.531
Joe DiMaggio          1949    329     60     14      6     14      0.286    0.492
Joe DiMaggio          1950    606     83     33     10     32      0.261    0.507
Joe DiMaggio          1951    482     71     22      4     12      0.226    0.363

>sort on home runs<
Joe DiMaggio          1937    621    119     35     15     46      0.346    0.673
Joe DiMaggio          1948    669    114     26     11     39      0.284    0.531
Joe DiMaggio          1938    660    117     32     13     32      0.294    0.527
Joe DiMaggio          1950    606     83     33     10     32      0.261    0.507
Joe DiMaggio          1940    572    111     28      9     31      0.313    0.556
Joe DiMaggio          1939    524    108     32      6     30      0.336    0.592
Joe DiMaggio          1941    622    109     43     11     30      0.310    0.559
Joe DiMaggio          1936    637    118     44     15     29      0.323    0.576
Joe DiMaggio          1946    567     93     20      8     25      0.257    0.453
Joe DiMaggio          1942    680    123     29     13     21      0.274    0.447
Joe DiMaggio          1947    601    107     31     10     20      0.280    0.464
Joe DiMaggio          1949    329     60     14      6     14      0.286    0.492
Joe DiMaggio          1951    482     71     22      4     12      0.226    0.363

>sort on at bats<
Joe DiMaggio          1942    680    123     29     13     21      0.274    0.447
Joe DiMaggio          1948    669    114     26     11     39      0.284    0.531
Joe DiMaggio          1938    660    117     32     13     32      0.294    0.527
Joe DiMaggio          1936    637    118     44     15     29      0.323    0.576
Joe DiMaggio          1941    622    109     43     11     30      0.310    0.559
Joe DiMaggio          1937    621    119     35     15     46      0.346    0.673
Joe DiMaggio          1950    606     83     33     10     32      0.261    0.507
Joe DiMaggio          1947    601    107     31     10     20      0.280    0.464
Joe DiMaggio          1940    572    111     28      9     31      0.313    0.556
Joe DiMaggio          1946    567     93     20      8     25      0.257    0.453
Joe DiMaggio          1939    524    108     32      6     30      0.336    0.592
Joe DiMaggio          1951    482     71     22      4     12      0.226    0.363
Joe DiMaggio          1949    329     60     14      6     14      0.286    0.492

>sort on slugging percentage<
Joe DiMaggio          1937    621    119     35     15     46      0.346    0.673
Joe DiMaggio          1939    524    108     32      6     30      0.336    0.592
Joe DiMaggio          1936    637    118     44     15     29      0.323    0.576
Joe DiMaggio          1941    622    109     43     11     30      0.310    0.559
Joe DiMaggio          1940    572    111     28      9     31      0.313    0.556
Joe DiMaggio          1948    669    114     26     11     39      0.284    0.531
Joe DiMaggio          1938    660    117     32     13     32      0.294    0.527
Joe DiMaggio          1950    606     83     33     10     32      0.261    0.507
Joe DiMaggio          1949    329     60     14      6     14      0.286    0.492
Joe DiMaggio          1947    601    107     31     10     20      0.280    0.464
Joe DiMaggio          1946    567     93     20      8     25      0.257    0.453
Joe DiMaggio          1942    680    123     29     13     21      0.274    0.447
Joe DiMaggio          1951    482     71     22      4     12      0.226    0.363

>sort on batting average <
Joe DiMaggio          1937    621    119     35     15     46      0.346    0.673
Joe DiMaggio          1939    524    108     32      6     30      0.336    0.592
Joe DiMaggio          1936    637    118     44     15     29      0.323    0.576
Joe DiMaggio          1940    572    111     28      9     31      0.313    0.556
Joe DiMaggio          1941    622    109     43     11     30      0.310    0.559
Joe DiMaggio          1938    660    117     32     13     32      0.294    0.527
Joe DiMaggio          1949    329     60     14      6     14      0.286    0.492
Joe DiMaggio          1948    669    114     26     11     39      0.284    0.531
Joe DiMaggio          1947    601    107     31     10     20      0.280    0.464
Joe DiMaggio          1942    680    123     29     13     21      0.274    0.447
Joe DiMaggio          1950    606     83     33     10     32      0.261    0.507
Joe DiMaggio          1946    567     93     20      8     25      0.257    0.453
Joe DiMaggio          1951    482     71     22      4     12      0.226    0.363

<ruth.txt>
Babe Ruth             1914     10      1      1      0      0      0.200    0.300
Babe Ruth             1915     92     14     10      1      4      0.315    0.576
Babe Ruth             1916    136     26      5      3      3      0.272    0.419
Babe Ruth             1917    123     29      6      3      2      0.325    0.472
Babe Ruth             1918    317     47     26     11     11      0.300    0.555
Babe Ruth             1919    432     64     34     12     29      0.322    0.657
Babe Ruth             1920    458     73     36      9     54      0.376    0.847
Babe Ruth             1921    540     85     44     16     59      0.378    0.846
Babe Ruth             1922    406     61     24      8     35      0.315    0.672
Babe Ruth             1923    522    106     45     13     41      0.393    0.764
Babe Ruth             1924    529    108     39      7     46      0.378    0.739
Babe Ruth             1925    359     65     12      2     25      0.290    0.543
Babe Ruth             1926    495    102     30      5     47      0.372    0.737
Babe Ruth             1927    540     95     29      8     60      0.356    0.772
Babe Ruth             1928    536     82     29      8     54      0.323    0.709
Babe Ruth             1929    499     94     26      6     46      0.345    0.697
Babe Ruth             1930    518    100     28      9     49      0.359    0.732
Babe Ruth             1931    534    119     31      3     46      0.373    0.700
Babe Ruth             1932    457     97     13      5     41      0.341    0.661
Babe Ruth             1933    459     80     21      3     34      0.301    0.582
Babe Ruth             1934    365     62     17      4     22      0.288    0.537
Babe Ruth             1935     72      7      0      0      6      0.181    0.431

>sort on home runs<
Babe Ruth             1927    540     95     29      8     60      0.356    0.772
Babe Ruth             1921    540     85     44     16     59      0.378    0.846
Babe Ruth             1920    458     73     36      9     54      0.376    0.847
Babe Ruth             1928    536     82     29      8     54      0.323    0.709
Babe Ruth             1930    518    100     28      9     49      0.359    0.732
Babe Ruth             1926    495    102     30      5     47      0.372    0.737
Babe Ruth             1924    529    108     39      7     46      0.378    0.739
Babe Ruth             1929    499     94     26      6     46      0.345    0.697
Babe Ruth             1931    534    119     31      3     46      0.373    0.700
Babe Ruth             1923    522    106     45     13     41      0.393    0.764
Babe Ruth             1932    457     97     13      5     41      0.341    0.661
Babe Ruth             1922    406     61     24      8     35      0.315    0.672
Babe Ruth             1933    459     80     21      3     34      0.301    0.582
Babe Ruth             1919    432     64     34     12     29      0.322    0.657
Babe Ruth             1925    359     65     12      2     25      0.290    0.543
Babe Ruth             1934    365     62     17      4     22      0.288    0.537
Babe Ruth             1918    317     47     26     11     11      0.300    0.555
Babe Ruth             1935     72      7      0      0      6      0.181    0.431
Babe Ruth             1915     92     14     10      1      4      0.315    0.576
Babe Ruth             1916    136     26      5      3      3      0.272    0.419
Babe Ruth             1917    123     29      6      3      2      0.325    0.472
Babe Ruth             1914     10      1      1      0      0      0.200    0.300

>sort on at bats<
Babe Ruth             1927    540     95     29      8     60      0.356    0.772
Babe Ruth             1921    540     85     44     16     59      0.378    0.846
Babe Ruth             1928    536     82     29      8     54      0.323    0.709
Babe Ruth             1931    534    119     31      3     46      0.373    0.700
Babe Ruth             1924    529    108     39      7     46      0.378    0.739
Babe Ruth             1923    522    106     45     13     41      0.393    0.764
Babe Ruth             1930    518    100     28      9     49      0.359    0.732
Babe Ruth             1929    499     94     26      6     46      0.345    0.697
Babe Ruth             1926    495    102     30      5     47      0.372    0.737
Babe Ruth             1933    459     80     21      3     34      0.301    0.582
Babe Ruth             1920    458     73     36      9     54      0.376    0.847
Babe Ruth             1932    457     97     13      5     41      0.341    0.661
Babe Ruth             1919    432     64     34     12     29      0.322    0.657
Babe Ruth             1922    406     61     24      8     35      0.315    0.672
Babe Ruth             1934    365     62     17      4     22      0.288    0.537
Babe Ruth             1925    359     65     12      2     25      0.290    0.543
Babe Ruth             1918    317     47     26     11     11      0.300    0.555
Babe Ruth             1916    136     26      5      3      3      0.272    0.419
Babe Ruth             1917    123     29      6      3      2      0.325    0.472
Babe Ruth             1915     92     14     10      1      4      0.315    0.576
Babe Ruth             1935     72      7      0      0      6      0.181    0.431
Babe Ruth             1914     10      1      1      0      0      0.200    0.300

>sort on slugging percentage<
Babe Ruth             1920    458     73     36      9     54      0.376    0.847
Babe Ruth             1921    540     85     44     16     59      0.378    0.846
Babe Ruth             1927    540     95     29      8     60      0.356    0.772
Babe Ruth             1923    522    106     45     13     41      0.393    0.764
Babe Ruth             1924    529    108     39      7     46      0.378    0.739
Babe Ruth             1926    495    102     30      5     47      0.372    0.737
Babe Ruth             1930    518    100     28      9     49      0.359    0.732
Babe Ruth             1928    536     82     29      8     54      0.323    0.709
Babe Ruth             1931    534    119     31      3     46      0.373    0.700
Babe Ruth             1929    499     94     26      6     46      0.345    0.697
Babe Ruth             1922    406     61     24      8     35      0.315    0.672
Babe Ruth             1932    457     97     13      5     41      0.341    0.661
Babe Ruth             1919    432     64     34     12     29      0.322    0.657
Babe Ruth             1933    459     80     21      3     34      0.301    0.582
Babe Ruth             1915     92     14     10      1      4      0.315    0.576
Babe Ruth             1918    317     47     26     11     11      0.300    0.555
Babe Ruth             1925    359     65     12      2     25      0.290    0.543
Babe Ruth             1934    365     62     17      4     22      0.288    0.537
Babe Ruth             1917    123     29      6      3      2      0.325    0.472
Babe Ruth             1935     72      7      0      0      6      0.181    0.431
Babe Ruth             1916    136     26      5      3      3      0.272    0.419
Babe Ruth             1914     10      1      1      0      0      0.200    0.300

>sort on batting average <
Babe Ruth             1923    522    106     45     13     41      0.393    0.764
Babe Ruth             1924    529    108     39      7     46      0.378    0.739
Babe Ruth             1921    540     85     44     16     59      0.378    0.846
Babe Ruth             1920    458     73     36      9     54      0.376    0.847
Babe Ruth             1931    534    119     31      3     46      0.373    0.700
Babe Ruth             1926    495    102     30      5     47      0.372    0.737
Babe Ruth             1930    518    100     28      9     49      0.359    0.732
Babe Ruth             1927    540     95     29      8     60      0.356    0.772
Babe Ruth             1929    499     94     26      6     46      0.345    0.697
Babe Ruth             1932    457     97     13      5     41      0.341    0.661
Babe Ruth             1917    123     29      6      3      2      0.325    0.472
Babe Ruth             1928    536     82     29      8     54      0.323    0.709
Babe Ruth             1919    432     64     34     12     29      0.322    0.657
Babe Ruth             1922    406     61     24      8     35      0.315    0.672
Babe Ruth             1915     92     14     10      1      4      0.315    0.576
Babe Ruth             1933    459     80     21      3     34      0.301    0.582
Babe Ruth             1918    317     47     26     11     11      0.300    0.555
Babe Ruth             1925    359     65     12      2     25      0.290    0.543
Babe Ruth             1934    365     62     17      4     22      0.288    0.537
Babe Ruth             1916    136     26      5      3      3      0.272    0.419
Babe Ruth             1914     10      1      1      0      0      0.200    0.300
Babe Ruth             1935     72      7      0      0      6      0.181    0.431
'''
from tkinter import * ### import tkinter into the code
from PlayersYear import * ### import PlayersYear to the code
from tkinter import messagebox ### import messagebox into in order to build the help button
class GUI: ### Class Gui
    def __init__(self): ### define the initial function 
        self.window = Tk() ### let self.window = Tk()
        self.window.title("Major League Baseball Analyzer") ### Build the name for the window 
        self.playerslist=[] ### build a list for players
    ###--------------- frmae 1
        ###----------build frame 1
        frame1=Frame(self.window) 
        frame1.pack(side=TOP,expand=YES,fill=BOTH)
        
        ###----------build frame 2
        frame2=Frame(self.window,bg='light yellow')
        frame2.pack(side=TOP,expand=YES,fill=BOTH)
        
        ###----------build frame 3
        frame3=Frame(self.window,bg='light yellow')
        frame3.pack(side=TOP,expand=YES,fill=BOTH)
        
        ###----------build frame 4 
        frame4=Frame(self.window,bg='light yellow')
        frame4.pack(side=TOP,expand=YES,fill=BOTH)
        
        ###----------build frame 5 
        frame5=Frame(self.window)
        frame5.pack(side=TOP,expand=YES,fill=BOTH)
        
    ###------------------frame 1
        Players_name_lable = Label(frame1, text="Player's Name",bg="cyan") ### using the function to build frame 1
        self.playersname = StringVar()
        name = Entry(frame1, width=10,textvariable=self.playersname) ### create enter button
        Players_name_lable.pack(side=LEFT)
        name.pack(side=LEFT)
              
        ### second button in the first frame
        year_lable = Label(frame1, text="Year",bg="cyan")
        self.year = StringVar()
        year = Entry(frame1, width=10,textvariable=self.year)
        year_lable.pack(side=LEFT)
        year.pack(side=LEFT)
        
        ### third button in the first frame
        hits_lable = Label(frame1, text="Hits",bg="cyan")
        self.hits = StringVar()
        hits = Entry(frame1, width=10,textvariable=self.hits)
        hits_lable.pack(side=LEFT)
        hits.pack(side=LEFT)        
        
        ### forth button in the first frame 
        doubles_lable = Label(frame1, text="Doubles",bg="cyan")
        self.doubles = StringVar()
        doubles = Entry(frame1, width=10,textvariable=self.doubles)
        doubles_lable.pack(side=LEFT)
        doubles.pack(side=LEFT)        
        
        ### fifth button in the first frame
        triples_lable = Label(frame1, text="Triples",bg="cyan")
        self.triples = StringVar()
        triples = Entry(frame1, width=10,textvariable=self.triples)
        triples_lable.pack(side=LEFT)
        triples.pack(side=LEFT)        
        
        ### sixth button in the first frame 
        homeruns_lable = Label(frame1, text="Home Runs",bg="cyan")
        self.homeruns = StringVar()
        homeruns= Entry(frame1, width=10,textvariable=self.homeruns)
        homeruns_lable.pack(side=LEFT)
        homeruns.pack(side=LEFT)
        
        ### seventh button in the first frmae
        atbats_lable = Label(frame1, text="At Bats",bg="cyan")
        self.bats = StringVar()
        atbats= Entry(frame1, width=10,textvariable=self.bats)
        atbats_lable.pack(side=LEFT)
        atbats.pack(side=LEFT)      
        
    ###---------------frame 2
        filename_lable=Label(frame2,text="File Name",bg="cyan")
        self.filename = StringVar()
        filename=Entry(frame2,width=43,textvariable=self.filename)
        filename_lable.pack(side=LEFT)
        filename.pack(side=LEFT)
        
    ###----------------frame 3
        filelabels=Label(frame3,text=('%-28s%12s%9s%11s%10s%11s%12s%13s%14s'%("Player","Year","AB","S","D","T","HR","BA","SLG")),bg='light yellow',fg='blue')
        filelabels.pack(side=LEFT)
        
    ###----------------frame 4
        self.text=Text(frame4,height=20,width=150,bg='light yellow')
        scroll = Scrollbar(frame4, command=self.text.yview)
        self.text.configure(yscrollcommand=scroll.set)  
        self.text.pack(side=LEFT)
        scroll.pack(side=RIGHT, fill=Y)  
        
    ###----------------frame 5
        self.firstbutton = Button(frame5, text="Compute a Player's Statistics",command=self.compute)   
        self.firstbutton.pack(side=LEFT, expand=YES, fill=BOTH)        
        
        self.secondbutton = Button(frame5, text="Process Players File",command=self.readfile)   
        self.secondbutton.pack(side=LEFT, expand=YES, fill=BOTH)  
        
        self.thirdbutton = Button(frame5, text="Save Log",command=self.save_log)   
        self.thirdbutton.pack(side=LEFT, expand=YES, fill=BOTH) 
        
        self.forthbutton = Button(frame5, text="Clear Player's Statistics",command=self.clear)   
        self.forthbutton.pack(side=LEFT, expand=YES, fill=BOTH)  
        
        self.fifthbutton = Button(frame5, text="Quit Baseball Analyzer",command=self.quit)
        self.fifthbutton.pack(side=LEFT, expand=YES, fill=BOTH)        
    
    ###----------------display menu
        menu = Menu(self.window)
        self.window.config(menu=menu) 
        
        submenu = Menu(menu)
        menu.add_cascade(label='Sort', menu=submenu)        
        
        submenu.add_command(label='Sort on home runs',command=self.sort_by_homeruns)
        submenu.add_command(label='Sort on at bats',command=self.sort_by_bats)
        submenu.add_separator()
        submenu.add_command(label='Sort on slugging percentage',command=self.sort_by_sp)
        submenu.add_command(label='Sort on batting average',command=self.sort_by_batting_Average)
        
    ###-----------------display menu
        
        
        submenu2=Menu(menu)
        menu.add_cascade(label='About Analyzer', menu=submenu2)
        submenu2.add_command(label='Help',command= self.help)
        
        mainloop()
        
    ###--------------Compute a Player's Statistics
    def compute(self):
        stats=[int(self.hits.get()),int(self.doubles.get()),int(self.triples.get()),int(self.homeruns.get()),int(self.bats.get())]
        
        player=PlayersYear(self.year.get(),self.playersname.get(),stats)
        self.playerslist.append(player)
        self.text.insert(END,player.__str__()+"\n")
    
    ###--------------Process Player File
    def readfile(self):
        filename=self.filename.get()
        file = []   ### creat a list for file
        the_file = open(filename, "r")   ### open the file and read the information inside the file
        line=the_file.readline()   ### create line in the file
        while line !='':    ### if file not equal to an empty list 
            line = line.rstrip("\n")   ### create a single sting for a file
            file.append(line.split(":"))   ###split the string which has ":" and add each line to the file
            line=the_file.readline()   ### let file readline
        Players = []  ### creating a list for the players
        for i in range(0,len(file)):  ### for all information in side the file let i equals to the length of the file list
            year = file[i][0][0:4]   ### because the format of the file is ["yearname","#1","#2","#3","#4","#5"], the information of the year should be the first   
                                         ### 4 stings in the list position 1
            player = file[i][0][4:]  ### the information of players should be in the firsting string of each list and the information of the following information
            stats= [int(file[i][1]), ### grab the first number of the list
                    int(file[i][2]), ###grab the second number of the list
                    int(file[i][3]),  ### grab the third number of the list
                    int(file[i][4]),  ###grab the forth number of the list
                    int(file[i][5])] ###grab the fifth number of the list
            temp = PlayersYear(year,player,stats) ### call the information on the PlayersYear.py (formationt the information we got)
            Players.append(temp)  ### adding the information of the temp to the list Players 
        self.playerslist=self.playerslist+Players
        for x in Players:
            self.text.insert(END,x.__str__()+"\n") 
                 
       
    ###---------------Save Log
     
    ###---------------Clear Player's Statistics 
    def clear(self):
        self.text.delete(1.0,END) 
        self.playerslist=[]
    
    ###--------------Quit Baseball Analyzer
    def quit(self):
        self.window.destroy()
    
    ###-------------Sort functions
    def getKeyOnHR(y):     ### def a function that you want to find as a sort mood
        return y.get_stats()[3]   ### the way to get the key of sort mood ()  in this one we want to let home run as a sort method    
    
    def getKeyOnBats(y):   ## def a function that you want to find as a sort mood
        return y.get_stats()[-1]  ### the way to get the key of sort mood ()   in this one we want to the Bats as a sort-method 
    
    def slugging_percentage(self): ### define a function called slugging_percentage with a peremiter called self
        '''
        Returns the slugging percentage of self.__player in self.__year.
        The slugging percentage is the total number of bases / at bats. For example, 
        a triple = 3 bases, a single = 1 base, ...
        '''
        slugging_average = (self.__stats[1]*2 + self.__stats[2]*3 + self.__stats[3]*4 + self.singles())/self.__stats[4] ### using information in stats to calculate slugging-percentage
        return slugging_average ### return the information got in slugging-average    
    
    def getKeyOnSP(y):    ### def a function that you want to find as a sort mood
        return y.slugging_percentage()   ### the way to get the key of sort mood ()   in this one we want to let slugging-percentage as a sort method
    
    def getKeyOnBA(y):
        return y.batting_average()
    
    def batting_average(self): ### define a funciton called batting-average with a peremiter self
        '''
        Returns the batting average of the self.__player in self__year.
        '''
        batting_average = self.__stats[0]/self.__stats[4] ### get the information in batting-average in stats
        return batting_average ### return the information get in batting-average
    
    
    def sort_by_homeruns(self): 
        self.playerslist.sort(key = GUI.getKeyOnHR,reverse=True)  ### sort all information in the file with the order of home run from sallest to biggest
        self.text.insert(END,"\n")
        for x in self.playerslist:  ### for all information inside the list
            self.text.insert(END,x.__str__()+"\n") ### print out the information 
            
    def sort_by_bats(self):
        self.playerslist.sort(key = GUI.getKeyOnBats,reverse=True)  ### sort all information in the file with the order of home run from sallest to biggest
        self.text.insert(END,"\n")
        for x in self.playerslist:  ### for all information inside the list
            self.text.insert(END,x.__str__()+"\n") ### print out the information     
    
    def sort_by_sp(self):
        self.playerslist.sort(key = GUI.getKeyOnSP,reverse=True)  ### sort all information in the file with the order of home run from sallest to biggest
        self.text.insert(END,"\n")
        for x in self.playerslist:  ### for all information inside the list
            self.text.insert(END,x.__str__()+"\n") ### print out the information  
            
    def sort_by_batting_Average(self): 
        self.playerslist.sort(key = GUI.getKeyOnBA,reverse=True)  ### sort all information in the file with the order of home run from sallest to biggest
        self.text.insert(END,"\n")
        for x in self.playerslist:  ### for all information inside the list
            self.text.insert(END,x.__str__()+"\n") ### print out the information 
    
    
    ###----------- save log
    def save_log(self):
        log=open("session_log.txt","w+")
        log.write(self.text.get("1.0",END))
        log.close()
    
    ###----------- help 
    def help(self):
        info="1.Enter information for a player(name,\n year, ...) into the boxes, click the \"Compute a players's Statistics\" button displays this player's statistics in the Text box. \n \n 2.Enter a file name in the box provided and \n click \"Progress a Player File\" displays the statistics of all players in the Text box. \n \n 3. Information in the Text box is saved to \n disk when this \"Save Log\" button is clicked. \n\n 4. By choosing from the Sort menu, the data \n in the file will be sorted based on the choice \n made (home runs, at bats,...) \n \n 5. Click \"Clear Player's Statistics\" to \n erase all information displayed in the GUI. \n \n 6.Click \"Quit Baseball Analyzer\" to quit \n this program."
        messagebox.showinfo("Help",info)
        
     
def main():
    gui=GUI() 
main()