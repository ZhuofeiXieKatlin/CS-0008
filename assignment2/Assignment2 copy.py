''' 
student: Zhuofei Xie
purpose: Using the knowledge of list and file to build a program that can read 
         the information of a wordlist file called sowpods.txt
Date:10/10/2017
sample run: 
       10 quextions on the assignment sheet
'''
def main():       ###the main dunctions for the whole program              
    x=readwordlist()     
    words_of_wordlist(x)       ### function for question(a) 
    words_with_four_letters(x) ### function for question(b) 
    longest_word_q_x(x)        ### function for question(c) 
    last_15_words(x)           ### function for question(d) 
    six_occurences_a(x)        ### function for question(e) 
    maximum_occurences_o(x)    ### function for question(f) 
    parlindrome(x)             ### function for question(g) 
    frequency_table(x)         ### function for question(h) 
    double_contain_words(x)    ### function for question(i) 
    contain_vowels(x)          ### function for question(j) 
def readwordlist():            ### function for reading information from the txt file   
    wordlist=[ ]               ### creat a list for wordlist
    the_wordlist=open("sowpods.txt","r")    ###open file for reading 
    
    line=the_wordlist.readline( )         ###let the length of the wordlist equal to length of words in the file
    while line !="":                      ### a while function for line
        line = line.rstrip('\n')          ###seperate differents words in different lines
        wordlist.append(line)             ###add line for wordlist
        line=the_wordlist.readline()
        
    return wordlist             ###return wordlist

def words_of_wordlist(wordlist):     ### the function for first question
    word=0                           ### give a variable for word
    wordlist 
    for word in range(len(wordlist)): ###let the range of the for-function at the range of the length of the wordlist
        if wordlist[word]!='':        ### a if-function to find out the length of the wordlist 
            word=word+1             
    print("a) The length of the wordlist is", word)    ### print out the answer

def words_with_four_letters(wordlist):  ### the function for 2nd question
    word4=0                             ### give a variable word4 as a variable to find out the total words with four letters  
    wordlist
    for word in range(len(wordlist)):   ###let the range of the for-function at the range of the length of the wordlist
        if len(wordlist[word])==4:      ### a if-function to find out which words have four letters
            word4=word4+1               ### add 1 to the answer when find a four-letter word
    print("b) The number of four-letter words in the wordlist is",word4)     ###print out the answer
 
          
def longest_word_q_x(wordlist):         ### the function for 3rd question
    wordlist              
    max=0                               ###let max be a variable and the value for max is 0 at beginnign
    for word in range(len(wordlist)):   ###let the range of the for-function at the range of the length of the wordlist
        y=wordlist[word]                ###let y equals to every single words in the wordlist
        if y[0]=='q' and y[-1]=='x':    ###find out which words has "q" at beginning and "x" at ending
            if len(y)>=max:             ### if the length of the word greater than max
                max=len(y)              ###max will be length of y 
    print("c) The length of the longest word in the dictionary beginning with q and ending with x is", max )   ### print out the final answer


def last_15_words(wordlist):            ### the function for 4th question
    rwordlist=wordlist[::-1]            ###reverse the wordlist 
    a=0                                 ### give a variable for a and let a=0
    print("d) The last ten 15-letters words are")
    for word in rwordlist:              ### the range of word is all words in wordlist
        if len(word)==15:               ###find out which words have 15 letters
            a=a+1                       ###add 1 to a if find a word with 15 letters
            if a<=10:                   ###stop the loop when we have already found 10 words at ending
                print("   ",a,".",word) ###print out the answer

def six_occurences_a(wordlist):         ### the function for 5th question
    wordlist
    print("e) The words with exactly 6 occurences are")
    for word in wordlist:               ### the range of word is all words in wordlist
        if word.count("a",0,len(word))==6: ###find out words has 6 "a" inside every single word
            print("    ",word)             ###print out the final answer

def maximum_occurences_o(wordlist):    ### the function for 6th question
    wordlist
    max=0                              ###give a variable at beginning 
                                       ### max will be the max number of "o" in every single words
    print("f) The words with the maximum possible numbers of 'o' ")
    for word in wordlist:             ### the range of words will be all words in the wordlist
        num=word.count("o",0,len(word))   ###find out the number of "o" in words contain "o"
        if num>=max:                      ###if the number of "o" greater than max 
            max=num                       ### let max equals to number of num
    for word in wordlist:                 ### the range of words will be all words in the wordlist
        if word.count("o",0,len(word))==max:  ### find out the words contain maximum number of "o"
            print(word)                       ###print out those words
             
def parlindrome(wordlist):             ### the function for 7th question
    print("g) palindromes begin with 'k' and 'z'")
    rwordlist=wordlist[::-1]          ###reverse the wordlist
    for word in wordlist:             ###the range of words will be all words in the wordlist
        if word==word[::-1] and (word[0]=="k" or word[0]=="z"): ###find out the words have same beginning and endding
                                                                ###the begging and ending for whose words must be either "k" or "z"
                                                                ###the palindrome means those words need be all same when see from both beginning and ending
                                                                ###because we reverse the function, it will be all same from begin to end
            print(word)               ###print out those words 

def frequency_table(wordlist):        ### the function for 8th question
    print("h) The Frequency Table is")
    F="Frequency Table"               ### let F equals to "Frequency Table"
    print("%24s" % (F))               ### using format code to bulid a correct format
    print(30*"-")
    W="Word Length"
    O="Occurences"
    print("%-10s %18s"%(W,O))        ### all these parts are building the frame of the frequency table 
    print(30*"-")
    total_word=0
    for word in wordlist:            ### using for function to find out the total words in the wordlist
        total_word+=1                ### add 1 to total_word when find out an answer 
        
    for word_length in range(2,16):  ###the length of the words in frequency table is 2-16
                                     ###for function give a limitation for the length of the words
                                     ### we need add 1 at the ending of for function in order it can count to 15
        occurences= 0                ### let occurences be 0 at beginning
        for word in wordlist:        ### the words all come from wordlist
            if len(word)==word_length:  ### let the length of words at the range of 2-16
                occurences+=1           ### add 1 to occerences when find out a word
        print("%10d %18d" % (word_length,occurences))   ###print out the word with correct format
    print(30*"-")   
    print("%14s %14d" %("Total word", total_word))
    print(30*"-")
    
def double_contain_words(wordlist):     ### the function for 9th question
    wordlist
    print("i) The words contain 'aa' and either 'ii' or 'oo' ")
    for word in wordlist:             ### the range of words equal to all words in wordlist
        if word.count("aa",0,len(word)) and (word.count("ii",0,len(word)) or word.count("oo",0,len(word))):  ###find out the word contains 'aa' and either'oo' or 'ii' 
            print(word)     ###print out those words
        
def contain_vowels(wordlist):       ### the function for 10th question 
    wordlist
    count=0                         ### let count be first vriable and equals to 0
    count2=0                        ### let count2 be second variable and also equals to 0
    print("j) The number of words contains every vowls: ")
    for word in wordlist:          ###the range of words will be all words in the wordlist
        if word.count("a",0,len(word)) and word.count("e",0,len(word)) and word.count("i",0,len(word)) and word.count("o",0,len(word)) and word.count("u",0,len(word)):
                                   ###find out the words contain all vowels inside each word
            count=count+1          ### add 1 to count when find a word
    print(count)                   ### print out the number of words contain every vowels 
    
    print("j) The number of words contains every vowls only once: ")
    for word in wordlist:          ###the range of words will be all words in the wordlist          
        if word.count("a",0,len(word))==1 and word.count("e",0,len(word))==1 and word.count("i",0,len(word))==1 and word.count("o",0,len(word))==1 and word.count("u",0,len(word))==1:
                                   ### find out the words contain every vowel for only once
            count2+=1              ### add 1 to count2 when find each word
    print(count2)                  ### print out the number of words which contain vowels only once 
main()                             ### call main funciton at the ending