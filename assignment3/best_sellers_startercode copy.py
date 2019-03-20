'''
Name:
Date created:
Purpose:




Sample run(s):




'''


def find_books_by_title(thistitle, booklist):
    '''
    For each book in the book list determine if the book's title is identical to
    this title or this title matches a substring of the book's title.  If so, 
    display the book's title, author and publication date (see the example output).
    This function does not return anything to the caller. 
    '''

    for book in booklist:
        
        ### your code goes here
        
        pass        ### remove line this after placing your code above
            
   
            

def find_books_by_author(thisauthor, booklist):
    '''
    For each book in the book list determine if the book's author is identical to 
    this author or this author matches a substring of the book's author. If so, 
    display the book's title, author and publication date (see the example output).
    This function does not return anything to the caller. 
    '''

    ### your code goes here
            
            



def find_books_between(beginyear, endyear, booklist):
    '''
    For each book in the book list determine if the book's publication year falls in
    the range begin year through end year. If so, display the book's title, author and
    publication date (see the example output). This function does not return anything
    to the caller.
    '''
    
    ### your code goes here
    



def find_books_in_month(pubmonth, pubyear, booklist):
    '''
    For each book in the book list determine if the book's publication month and year
    are identical to the pubmonth and the pubyear. If so, display the book's title, 
    author and publication date (see the example output). This function does not return 
    anything to the caller.
    '''
    
    ### your code goes here
            
            


def read_best_sellers(filename):
    '''
    Read the best seller data by converting each line of data such as (see below) 
    
         "1876	Gore Vidal	Random House	4/11/1976	Fiction\n"
         
    into the list using the split() function (see below)
    
         ['1876', 'Gore Vidal', 'Random House',	'4/11/1976', 'Fiction']
         
    then place it inside the list of all lines (see below)
    
        [ ['1876', 'Gore Vidal', 'Random House', '4/11/1976', 'Fiction'], ... , ['Doctor Sleep', 'Stephen King, 'Scribner', '10/13/2013', 'Fiction']]
    '''
    books = []
    file_in = open(filename, 'r')
    
    ### your code goes here
    
    
    
    ### your code goes here
    
    file_in.close()   
    return books


        
        
    
    
    
    
    
    
def display_menu():
    '''
    Displays a menu of choices to the users (see below). Returns either '1', '2',
    '3', '4', 'q', or 'Q' to the caller. If any other item is entered by the
    user, the user is prompted to re-enter another item. Once a legit value is entered
    that value is returned to the caller.
    
    What would you like to do?
    1: Look up year range
    2: Look up month/year
    3: Search for author
    4: Search for title
    Q: Quit
    > 5   <- ignored
    > -1  <- ignored
    > 3   <- valid input (return to caller)
    
    '''
    
    ### your code goes here





def main():
    book_data = read_best_sellers('bestsellers.txt')
    
    choice = display_menu()
    while choice != 'q' and choice != 'Q':

        ### your code goes here  
        
        
        ### your code goes here
            
        choice = display_menu()
        
    print("\nProgram Execution Complete")     
        

    
    
main()