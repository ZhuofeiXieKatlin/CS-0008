###import pylab as py

def open_file(filename):
    while True:
        try: 
            filename  = input("Enter the name of the file you want to read: ")
            file = open(filename,"r")
        
        except: 
            print("erro")
    
    
        
        
    '''Remember to put a docstring here'''
    #input("Input a file name: ")
    #print("Unable to open file. Please try again.")
    pass
'''
def update_dictionary(dictionary, year, hurricane_name, data):
    ###Remember to put a docstring here
    file = (filename,"r")
    D = {}
    line = file.readline()
    
    while line != " ":
        line = line.rstrip("\n")
        year = int(line)
        D(year) = {}
        while True:
            movie=file.readline().rstrip("\n")
            if movie == '-':  break
            actors=file.readline().rstrip("\n").split(",")
            D[year][movie]=actors
        line = file.readline()
    file.close
    pass
'''    
def create_dictionary():
    '''Remember to put a docstring here'''
    pass

def display_table(dictionary, year):
    '''Remember to put a docstring here'''
    pass

def get_years(dictionary):
    '''Remember to put a docstring here'''
    pass    
        
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
    

def main():
    '''Remember to put a docstring here'''
    
    pass
  
    
if __name__ == "__main__":
    main()