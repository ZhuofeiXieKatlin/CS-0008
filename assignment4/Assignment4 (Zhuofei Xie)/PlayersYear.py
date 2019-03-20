'''
Name: Zhuofei Xie

Date created: 2017/11/1

Purpose: Using class method to execute the information found in the file and using driver to print the information you want with the correct format
Sample run(s):
Hank Aaron's stats: [162, 22, 3, 47, 495]
Barry Bonds' stats: [149, 31, 2, 46, 403]
Babe Ruth's stats: [172, 36, 9, 54, 457]

Hank Aaron            1971     495      90      22       3      47    0.327    0.669
Barry Bonds           2002     403      70      31       2      46    0.370    0.799
Babe Ruth             1920     457      73      36       9      54    0.376    0.849


Hank Aaron has 90 singles
Barry Bonds has 70 singles
Babe Ruth has 73 singles

Hank Aaron has 0.32727 average
Barry Bonds has 0.36973 average
Babe Ruth has 0.37637 average

Hank Aaron has 0.66869 slugging percentage
Barry Bonds has 0.79901 slugging percentage
Babe Ruth has 0.84902 slugging percentage

Hank Aaron has a lower slugging percentage than Barry Bonds?  True
Barry Bonds has a lower slugging percentage than Hank Aaron?  False
Babe Ruth has a lower slugging percentage than Hank Aaron?  False

Hank Aaron          0.669           1971
Barry Bonds         0.799           2002
Babe Ruth           0.849           1920


-------------------------------------------------------------------------------------
Player                Year      AB      S        D       T      HR     BA      SLG     
-------------------------------------------------------------------------------------



---------------------------------------------
   Player           Slugging %      Year
---------------------------------------------

What would you like to do?

1971      Hank Aaron        [162,22,3,47,495]
2002      Barry Bonds       [149,31,2,46,403]
1920      Babe Ruth         [172,36,9,54,457]
'''
class PlayersYear: ###using class method at the beginning
    def __init__(self, year, player, stats): ### define a founction called init to grab initial information with four peremiters 
        '''
        self.__year = the year (an int) this player register these stats
        self.__player = the players name (a string)
        self.__stats = this player's statistics (a list of ints)
        '''
        self.__year = int(year) ### self.__year gets the information of year and transfer the year into integer 
        self.__player = player ### the second information is name (second position)
        self.__stats = stats ### the thrid information is status(a list)
    
    def get_stats(self): ### define a funciton called get-stats with peremiter self
        '''
        Returns the value of self.__stats to the caller.
        Don't forget to return a list of integers!
        '''
        return self.__stats ### return the information of status
    
    def __str__(self): ### define a information called __str__ (get the format of the information)
        '''
        Returns a player's stats for a given the year as specified in heading1().
        Note this corresponds to a line like:
        Babe Ruth             1920     457      73      36       9      54    0.376    0.849
        '''
        return '%-20s%6d%7d%7d%7d%7d%7d%11.3f%9.3f' % (self.__player, self.__year,self.__stats[-1],self.singles(), self.__stats[1],self.__stats[2],self.__stats[3],self.batting_average(),self.slugging_percentage()) ### returning the format the information 
    
    def singles(self): ###get the information of singles
        '''
        Returns the number of singles this player has in self.__year.
        '''
        singles=self.__stats[0]-self.__stats[1]-self.__stats[2]-self.__stats[3] ### get the information of singles in stats 
        
        return singles ### return the information get in singles
    
    
    def batting_average(self): ### define a funciton called batting-average with a peremiter self
        '''
        Returns the batting average of the self.__player in self__year.
        '''
        batting_average = self.__stats[0]/self.__stats[4] ### get the information in batting-average in stats
        return batting_average ### return the information get in batting-average

    
    def slugging_percentage(self): ### define a function called slugging_percentage with a peremiter called self
        '''
        Returns the slugging percentage of self.__player in self.__year.
        The slugging percentage is the total number of bases / at bats. For example, 
        a triple = 3 bases, a single = 1 base, ...
        '''
        slugging_average = (self.__stats[1]*2 + self.__stats[2]*3 + self.__stats[3]*4 + self.singles())/self.__stats[4] ### using information in stats to calculate slugging-percentage
        return slugging_average ### return the information got in slugging-average
        
        
    def __lt__(self, other): ### define a function called __It__ with two peremiter (self and other)
        '''
        Returns True is self's slugging percentage is smaller than the other's slugging percentage,
        otherwise, return False. You are allowed to call the slugging_percentage() function here.
        '''
        return self.slugging_percentage() < other.slugging_percentage()  ### return the information got in self.slugging_percentage and other.slugging_percentage and compare the information get


    def print_player(self): ### define a function called print-player with a peremiter called self
        '''
        Displays a player's stats for a given the year as specified in heading2().
        This corresponds to a line like:
        Babe Ruth           0.849           1920
        '''
        return ('%-20s%.3f%20d'%(self.__player,self.slugging_percentage(),self.__year)) ### format the information of print-player 

    def heading1(): ### create the information of format1
        '''
        Displays the heading1 shown in the drive.py.
        The heading is:
        -------------------------------------------------------------------------------------
        Player                Year      AB      S        D       T      HR     BA      SLG     
        -------------------------------------------------------------------------------------
        '''
        print(82*"-") 
        print('%-20s%6s%7s%7s%7s%7s%7s%9s%9s'%("Player","Year","AB","S","D","T","HR","BA","SLG")) ### print format 1
        print(82*"-")
    
    
    def heading2(): ### define a function called heading 2  
        '''
        Displays the heading2 shown in the drive.py.
        The heading is:
        ---------------------------------------------
        Player           Slugging %      Year
        ---------------------------------------------
        '''
             ### your code goes here, print exactly as shown in driver.py!         
        
        print(50*"-")
        print("%-10s%18s%17s"%("Player","Slugging %","Year")) ###print information of format 2
        print(50*"-")
     
        