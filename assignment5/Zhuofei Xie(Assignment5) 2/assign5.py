'''
Name: Zhuofei Xie

Date created: 2017/11/20

Purpose: 
Hurricane season is back and it came with a vengeance. Over five hurricanes have passed so
far and two of them have done massive damage to the Caribbean, including Puerto Rico. In
order to prepare countermeasures against the destruction these atmospheric phenomena leave
on their way, it is imperative to gather information about their wind speeds and trajectory for
the creation of better predictive models. The National Hurricane Center is responsible to
record these disasters and create these predictive models (http://www.nhc.noaa.gov/).
For this project, you are tasked to create a program that stores a record of all the
hurricanes that occurred within a range of years into a dictionary of dictionaries. Using
this dictionary, it is required to extract all the hurricanes that occurred in a year and
print the peak wind speed of each hurricane with their coordinates and dates, plot the
trajectory of each hurricane, and plot a line chart with the peak wind speeds and show
the category each hurricane reached.

Sample run(s):
Test Case 1:
Input a file name: storm_track.txt
Hurricane Record Software
Records from 2007 to 2017

Enter the year to show hurricane data or 'quit': 2017
             Peak Wind Speed for the Hurricanes in 2017
Name             Coordinates Wind Speed (knots)             Date
ARLENE         ( 40.00,-48.00)             45.00         04/21/06Z
BRET           ( 11.60,-64.40)             40.00         06/20/12Z
CINDY          ( 27.30,-91.90)             50.00         06/21/06Z
DON            ( 11.50,-56.20)             45.00         07/18/06Z
FOUR           ( 15.60,-50.90)             25.00         07/07/12Z
FRANKLIN       ( 20.20,-96.10)             75.00         08/10/00Z
GERT           ( 40.10,-58.40)             90.00         08/17/00Z
HARVEY         ( 28.00,-97.00)            115.00         08/26/00Z
IRMA           ( 19.40,-66.80)            160.00         09/07/00Z
JOSE           ( 16.90,-59.30)            135.00         09/09/11Z
KATIA          ( 21.00,-96.50)             90.00         09/08/18Z
LEE            ( 31.20,-57.10)            100.00         09/27/18Z
MARIA          ( 17.30,-64.70)            150.00         09/20/00Z
NATE           ( 28.40,-89.10)             80.00         10/07/18Z
OPHELIA        ( 37.30,-21.50)            100.00         10/15/00Z
SIX            ( 27.70,-83.20)             40.00         07/31/06Z

Test Case 2:
Input a file name: storm_track.txt
Hurricane Record Software
Records from 2007 to 2017

Enter the year to show hurricane data or 'quit': abc
Error with the year key! Try another year
Enter the year to show hurricane data or 'quit': 2000
Error with the year key! Try another year
Enter the year to show hurricane data or 'quit': 2010
             Peak Wind Speed for the Hurricanes in 2010
Name             Coordinates Wind Speed (knots)             Date
ALEX           ( 24.20,-97.70)             95.00         07/01/02Z
BONNIE         ( 23.80,-77.80)             40.00         07/23/06Z
COLIN          ( 25.60,-66.60)             50.00         08/06/00Z
DANIELLE       ( 27.10,-60.10)            115.00         08/27/18Z
EARL           ( 28.60,-74.30)            125.00         09/02/06Z
FIONA          ( 19.50,-62.50)             55.00         09/01/18Z
FIVE           ( 26.50,-85.00)             30.00         08/11/06Z
GASTON         ( 12.90,-36.10)             35.00         09/01/18Z
HERMINE        ( 25.30,-97.40)             60.00         09/07/02Z
IGOR           ( 18.90,-53.50)            135.00         09/15/00Z
JULIA          ( 17.70,-32.20)            120.00         09/15/12Z
KARL           ( 19.60,-95.60)            110.00         09/17/12Z
LISA           ( 20.40,-27.80)             75.00         09/25/00Z
MATTHEW        ( 15.20,-84.60)             50.00         09/25/00Z
NICOLE         ( 27.40,-78.50)             40.00         09/30/12Z
OTTO           ( 28.50,-59.70)             75.00         10/09/06Z
PAULA          ( 19.60,-86.00)             90.00         10/13/00Z
RICHARD        ( 17.20,-88.20)             85.00         10/25/00Z
SHARY          ( 35.10,-57.20)             65.00         10/30/12Z
TOMAS          ( 13.80,-62.40)             85.00         10/31/06Z
TWO            ( 26.10,-96.60)             30.00         07/08/12Z
'''
import pylab as py
import operator ### import operator in order to sort information 
def open_file(): ### create a function to open file
    '''Remember to put a docstring here'''
    #input("Input a file name: ")
    #print("Unable to open file. Please try again.")
    while True: ### create a while loop until we get the true information
        try: ### inside the try loop
            filename = input("Input a file name: ") ### enter the file name by using input
            file = open(filename,"r") ### open file and read 
            break ### if we get the corret information break the loop
        except IOError: ### except IOError 
            print("Unable to open file. Please try again.") ### print out "Unable to open file. Please try again."
    return file ### return the file in order to call in the main function

def update_dictionary(dictionary, year, hurricane_name, data):  ### def a function with 4 peremiter 
    '''Remember to put a docstring here'''
    if dictionary.get(year)==None: ### if dictionary.get(year) is not exist
        dictionary[year]={} ### create a dictionary for dictionary[year] as a dictionary{}
    if dictionary[year].get(hurricane_name)==None: ### if dictionary[year].get(hurricane_name) is not exist
        dictionary[year][hurricane_name]=[] ###create a list for dictionary[year][hurricane_name] 
    dictionary[year][hurricane_name].append(data) ### then added all information into the list called dictionary[year][hurricane_name]
          
def create_dictionary(fp): ### def a function with a peremiter called fp(the file name)
    '''Remember to put a docstring here'''
    line=fp.readline().rstrip("\n").split(" ") ### readline in the fp
    dictionary={} ### create a dictionary for the whole information
    while line !=[""]: ### we have already converted each line to a list, if we read an empty list, the while loop while stop
        year=line[0] ### year = line[0]
        hurricane_name=line[1] ### hurricane_name = line[1]
        lat=float(line[3]) ### convert information of lat into float and lat = float(line[3])
        long=float(line[4]) ### long= float(line[4])
        date=line[5] ###data=line[5]
        try:
            wind=float(line[6]) ### if the information wind is not a string of number let wind = float(line[6])
            pressure=float(line[7]) ### if the information pressure is not a string of number let pressure = float(linr[7])
            
        except ValueError: ### except the value error
            wind=0 ### let wind equals to 0
            pressure=0 ### let pressure equals to 0
           
                
        line=fp.readline().rstrip("\n").split(" ") ### read file in line and usign rstrip and split methods to convert the information into correct format 
        data=(lat,long,date,wind,pressure) ### creating a tuple for data and the information inside should be lat,long,date,wind,pressure 
        update_dictionary(dictionary, year, hurricane_name, data) ### update the information into def function
    return dictionary ### return the dictionary that created 
    
        

def display_table(dictionary, year): ### def a function and let dictionary and year be the variables
    '''Remember to put a docstring here'''
    print("             Peak Wind Speed for the Hurricanes in", year)  ### print out the format
    print("Name             Coordinates Wind Speed (knots)             Date")   ### print out the format
    keys=[]  ### create a list for information key 
    for key in sorted(dictionary[year]): ### using for loop to let each key in the dictionary can appear in sorted format
        keys.append(key) ### append each key into the list "keys "
    for item in keys: ### for each item in the keys
        information = (dictionary[year][item]) ### information should be the dictionary of year inside dictionary and with the same variables 
        information.sort(key=operator.itemgetter(3,0,1),reverse=True) ### sort the information with wind,lat,long sequences, reverse the information

        print("%-15s%s %-5.2f,%-6.2f%s%18.2f%18s"%(item,"(",information[0][0],information[0][1],")",information[0][3],information[0][2])) ### print out the information with the correct format
        
   

    
def get_years(dictionary): ### def a function with the variable dictionary
    '''Remember to put a docstring here'''
    year=[] ### create a list for year
    for key in (dictionary): ### for each year inside the dictionary
        year.append(int(key)) ### apeend each year found in the dictionary into list "year"
    min_year=min(year) ### minimum year should be min(year)
    max_year=max(year) ### maxmium year should be max(year)
    return year ### return the list of year 

      
def prepare_plot(dictionary, year):
    '''Remember to put a docstring here
       Extra credit
    '''
    pass
    
    # create everything that is required for plotting
    #return (names, max_speed)
    

def plot_wind_chart(year,size,names,max_speed):
    '''Remember to put a docstring here
    This is called in main() if you are attempting the extra credit problem.
    size is the length of list containing the hurricane names.
    '''
    
    # Set the value of the category
    cat_limit = [ [v for i in range(size)] for v in [64,83,96,113,137] ]
    
    
    # Colors for the category plots
    COLORS = ["g","b","y","m","r"]
    
    # Plot the Wind Speed of Hurricane
    for i in range(5):
        py.plot(range(size),cat_limit[i],COLORS[i],label="category-{:d}".format(i+1))
        
    # Set the legend for the categories
    py.legend(bbox_to_anchor=(1.05, 1.),loc=2,\
              borderaxespad=0., fontsize=10)
    
    py.xticks(range(size),names,rotation='vertical') # Set the x-axis to be the names
    py.ylim(0,180) # Set the limit of the wind speed
    
    # Set the axis labels and title
    py.ylabel("Wind Speed (knots)")
    py.xlabel("Hurricane Name")
    py.title("Max Hurricane Wind Speed for {}".format(year))
    py.plot(range(size),max_speed) # plot the wind speed plot
    py.show() # Show the plot
    

def main(): ### def a main function at the end of the program
    '''Remember to put a docstring here'''
    file = open_file() ### open file to read
    D = create_dictionary(file) ### D should be the dictinary that we get
    print("Hurricane Record Software")
    min_year=min(get_years(D)) ### min year should be the first year we have in list year
    max_year=max(get_years(D)) ### max year should be the last year we have in list year (because we sort the information)
    print("Records from",min_year, "to", max_year)   ### print out the max and min year
    print(  ) 
    while True: ### using try and except function to get the correct information
        year = input("Enter the year to show hurricane data or 'quit': " ) ### input the information want to find 
        try: ### try input the information
            year_test=int(year) ### year we want to test should be a integer
        except ValueError:
            print("Error with the year key! Try another year")  ### if we input a wrong infomration, error will appear
            continue ### continue the information to track
        if min_year<= year_test <=max_year: ### if the year we input inside the range of the min and max
            break ### the true information will continue
        else: ### else
            print("Error with the year key! Try another year") ### an error will appear
    display_table(D, year)
    
    
if __name__ == "__main__":
    main()