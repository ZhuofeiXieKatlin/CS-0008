'''
Name: Zhuofei Xie

Date created: 2017/10/17

Purpose: The New York Times newspaper has "published seller" lists since 1942. 
Book sales are tracked nationwide, leading to a list of those books that have recently
sold the most copies. 
Implement and test a program which allows the user to search a subset of the books
which have appeared in the New York Times best sellers lists. 
After constrcuting the list of books, the program will display a menu of options and 
allow the user to search for books that meet certain criteria. 
This program can let users to find books by using different ways, such as find books wich 
pubilished in same range and by same authors. 

Sample run(s):
What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
>3
    
Enters an author's name (or part of a name): trump
    
Trump: Surviving at the Top, by Donald Trump (9/9/1990)
Trump: The Art of the Deal, by Donald Trump (1/17/1988)

What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
>3
    
Enters an author's name (or part of a name): tol
    
Silmarillion, by J. R. R. Tolkein (10/2/1977)
The Children of the Hurin, by J.R.R. Tolkein (5/6/2007)


What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
>1
    
Enter beginning year: 1960
Enter ending year: 1962

All titles between 1960 and 1962:
    
A Shade of Difference, by Allen Drury (10/28/1962)
Franny and Zooey, by J. D. Sallinger (10/29/1961)
Hawaii, by James Michener (1/17/1960)
Seven Days in May, by Fletcher Knebel (11/18/1962)
Ship of Fools, by Katherine Anne Porter (4/29/1962)
The Agony and the Ecstasy, by Irving Stone (4/23/1961)
The Last of the Just, by Andre Schwarz-Bart (3/26/1961)
Born Free, by Joy Adamson (8/7/1960)
Calories Don't Count, by Herman Taller (3/25/1962)
May This House Be Safe from Tigers, by Alexander King (3/13/1960)
Silent Spring, by Rachel Carson (10/28/1962)
The Making of the President - 1960, by Theodore H. White (9/10/1961)
The New English Bible, by Oxford University Press (Editor) (5/28/1961)
The Rise and Fall of the Third Reich, by William Shirer (12/4/1960)
The Rothchilds, by Frederic Morton (6/24/1962)
The Waste Makers, by Vance Packard (11/6/1960)
Travels with Charley, by John Steinbeck (10/21/1962)

What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
>4
    
Enter a title(or part of a title): secret
    
Harry Potter and the Chamber of Secrets byJ. K. Rowling (6/20/1999)
The Secret of Santa Vittoria byRobert Crichton (11/20/1966)
The Secret Pilgrim byJohn le Carre (1/20/1991)

What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
>2
    
Enter a month (as a number 1-12): 9
Enter year: 1990

All Titles in month 9 of 1990 :

Four Past Midnight, by Stephen King (9/16/1990)
Memories of Midnight, by Sidney Sheldon (9/2/1990)
Darkness Visible, by William Styron (9/16/1990)
Millie's Book, by Barbara Bush (9/30/1990)
Trump: Surviving at the Top, by Donald Trump (9/9/1990)

What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
>5
>8
>-1
>w
>Q

Program Execution Complete

What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
>1
    
Enter beginning year: 1890
Enter ending year: 1891
    
All Titles between 1890 and 1891 :
     
No book were found between 1890 and 1891 !

What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
>3
Enters an author's name (or part of a name): novacky
    
the author " novacky " wasn't found
    
What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
>2
Enter a month (as a number 1-12): 5
Enter year: 1904
    
All Titles in month 5 of 1904 :
     
No book found in May 1904
    
What would you like to do?
1: Look up year range
2: Look up month/year
3: Search for author
4: Search for title
Q: Quit
>4
Enter a title(or part of a title): zombie
    
The title " zombie " wasn't found
'''
def find_books_by_title(thistitle, booklist): ###define a function called find_books_by_title
    '''
    For each book in the book list determine if the book's title is identical to
    this title or this title matches a substring of the book's title.  If so, 
    display the book's title, author and publication date (see the example output).
    This function does not return anything to the caller. 
    '''
    number=0                           ###let number =0
    for book in booklist:              ###using for function to let every book can found in booklist
        this_title=thistitle.lower()   ###let this_title = input(thistitle)[lower words]
        title=book[0]                  ### title is in the first place of a list
        title_lower=title.lower()      ###let title also equals to all words with lower input
        if this_title in title_lower:  ### using if function to find in booklist which title has same string as input
            number+=1                  ### when find a book add "1" to number until reach all books in booklist
            print("%s by%s (%s)"% (book[0],book[1],book[3]))  ### format to print out the books that find in booklist
    if number ==0:                     ### when do not find any books in booklist using if number = 0
        print("The title","\"",thistitle,"\"","wasn't found")   ### format to print out when do not find any books

            

def find_books_by_author(thisauthor, booklist):  ###define a function called find_books_by_author
    '''
    For each book in the book list determine if the book's author is identical to 
    this author or this author matches a substring of the book's author. If so, 
    display the book's title, author and publication date (see the example output).
    This function does not return anything to the caller. 
    '''
    number=0 ###let number =0
    for book in booklist: ###using for function to let every book can found in booklist
        this_author=thisauthor.lower() ###let this_author = input(author)[lower words]
        author=book[1] ### author is in the second place of a list
        author1=author.lower() ###let author also equals to all authors of the booklist with lower input
        if this_author in author1: ### using if function to find in booklist which author has same string as input
            number += 1 ### when find a book add "1" to number until reach all books in booklist
            print("%s, by %s (%s)"%(book[0],author,book[3])) ### format to print out the books that find in booklist
    if number == 0: ### when do not find any books in booklist using if number = 0
        print("the author" ,"\"",thisauthor,"\"", "wasn't found")### format to print out when do not find any books


def find_books_between(beginyear, endyear, booklist): ###define a function called find_books_between(year range)
    '''
    For each book in the book list determine if the book's publication year falls in
    the range begin year through end year. If so, display the book's title, author and
    publication date (see the example output). This function does not return anything
    to the caller.
    '''
    print("All Titles between",beginyear,"and",endyear,":") ###print the work of this function
    print("     ") ### print an empty line between these two lines
    number=0 ###et number =0
    for year in booklist:###using for function to let every book can found in booklist
        booklist_year=year[3] ### time is in the third place of a list
        booklist_year_1=booklist_year.split('/') ###using list.split to split a string of a list with special symbols
        booklist_actual_year=booklist_year_1[2] ### after split a list such as ["2/9/1999"] to [["2"],["9"],["1999"]]
                                                ### year is the third place of a list after split it
        if int(beginyear) <= int(booklist_actual_year) and int(booklist_actual_year)<=int(endyear): ###using if-function to find out if the book year range in the range of input(beginyear and endyear) 
            number=number+1 ### when find a book add "1" in the number 
            print("%s, by %s (%s)"%(year[0],year[1],year[3])) ###format to print out a book
    if number==0:### when do not find any books in booklist using if number = 0
        print("No book were found between",beginyear, "and", endyear,"!")### format to print out when do not find any books
        
    
    
def find_books_in_month(pubmonth, pubyear, booklist):###define a function called find_books_in_month
    '''
    For each book in the book list determine if the book's publication month and year
    are identical to the pubmonth and the pubyear. If so, display the book's title, 
    author and publication date (see the example output). This function does not return 
    anything to the caller.
    '''
    print("All Titles in month", pubmonth,"of",pubyear,":")###print the work of this function
    print("     ") ### print an empty line between these two lines
    number=0 ###et number =0
    Month=["January","February","March","April","May","June","July","August","September","October","November","December"] ###creat a list called Month in order to translate a input(month)[number] to [word]
    for month in booklist:###using for function to let every book can found in booklist
        book_month=month[3]### time is in the third place of a list
        book_month_year=book_month.split("/")###using list.split to split a string of a list with special symbols
        book_actual_month=book_month_year[0]### after split a list such as ["2/9/1999"] to [["2"],["9"],["1999"]]
                                                ### month is the third place of a list after split it
        book_actual_year=book_month_year[2]### after split a list such as ["2/9/1999"] to [["2"],["9"],["1999"]]
                                                ### year is the third place of a list after split it
        if int(pubmonth)==int(book_actual_month) and int(pubyear)==int(book_actual_year): ###using if-function to find out if the book confirm with the requirement
            number=number+1  ### when find a book add "1" in the number 
            print("%s, by %s (%s)"%(month[0],month[1],month[3])) ###format to print out a book
    if number == 0: ### when do not find any books in booklist using if number = 0
        print("No book found in",Month[int(pubmonth)-1], pubyear) ### format to print out when do not find any books
        

def read_best_sellers(filename): ### def a function
    '''
    Read the best seller data by converting each line of data such as (see below) 
    
         "1876	Gore Vidal	Random House	4/11/1976	Fiction\n"
         
    into the list using the split() function (see below)
    
         ['1876', 'Gore Vidal', 'Random House',	'4/11/1976', 'Fiction']
         
    then place it inside the list of all lines (see below)
    
        [ ['1876', 'Gore Vidal', 'Random House', '4/11/1976', 'Fiction'], ... , ['Doctor Sleep', 'Stephen King, 'Scribner', '10/13/2013', 'Fiction']]
    '''
    
    best_sellers=open("bestsellers.txt","r") ###read the txt file called bestsellers
    line=best_sellers.readline().rstrip('\n') ### format the line of the file 
    
    booklist=[] ### creat a list for booklist
    for line in best_sellers: ### let line in the booklist
        line = line.rstrip('\n') ###rstrip a line with each new line
        booklist.append(line.split('\t')) ###split a list with long space
    return booklist ###return booklist
                    
            
def display_menu(): ### creat a function called display_menu
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
    print("What would you like to do?")  ###print menu
    print("1: Look up year range")
    print("2: Look up month/year")
    print("3: Search for author")
    print("4: Search for title")
    print("Q: Quit")
    choice=input(">")
    return choice
    
def main(): ###define main function
    booklist = read_best_sellers('bestsellers.txt') ###let booklist equals to read txt file
    choice=display_menu()  
    while choice != 'q' and choice != 'Q': ###using while function; while input equals to q or Q
                                           ### when they equal to q or Q, go out of while loop
        while choice !="1" and choice != "2" and choice !="3" and choice != "4":
            choice =input (">")   
            if choice == 'q' or choice == 'Q':
                print ("\nProgram Execution Complete")                
        if choice=='1': ###if the input equals to "1"
            beginyear=input("Enter beginning year: ") ###call each functions during the call
            endyear=input("Enter ending year: ")###let users to input information
            print("    ")
            find_books_between(beginyear, endyear, booklist) ###call function
            print("    ")
        elif choice=='2': ###call function 2
            pubmonth=input("Enter a month (as a number 1-12): ")
            pubyear=input("Enter year: ")
            booklist
            print("    ")
            find_books_in_month(pubmonth, pubyear, booklist)
            print("    ")
        elif choice=='3': ### call function three
            thisauthor=input("Enters an author's name (or part of a name): ")
            booklist
            print("    ")
            find_books_by_author(thisauthor, booklist)
            print("    ")
        elif choice=='4': ###call function 4
            thistitle=input("Enter a title(or part of a title): ")
            booklist
            print("    ")
            find_books_by_title(thistitle, booklist) 
            print("    ")
     
        
        choice = display_menu()   
    print("\nProgram Execution Complete")
                
main() ### call main function