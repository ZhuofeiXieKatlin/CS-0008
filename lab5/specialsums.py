'''
Moldules: specialsums contains functions that sum onsecutive integers, sum squares 
of consecutive integers, and sum cubes of consecutive integers.
'''
def gauss(n):
    '''Carl Fredrick found a formula for 1+2+3+...+n in 2nd grade.
       we honor him by calling this sum, Gauss' sum'''
    sum=0
    for i in range(n+1):
        sum +=i
    return sum
def sumconsecutive(m,n):
    ''' This function computes the sum:
             m + (m+1) + (m+2) + ... + n, when 1<=m<n
             1 + 2 + 3 + ... + n, when m==n>=1
             n + (n+1) + (n+2) + (n+3) + ... +m, when 1<=n<m '''
    sum=0
    if 1<=m and m<n:
        for i in range(m,n+1):
            sum=sum+i
        return sum
    if m==n and n>=1:
        for i in range(n+1):
            sum=sum+i
        return sum
    if 1<=n and n<m:
        for i in range(n,m+1):
            sum=sum+i
        return sum
    
def sumofsqs(n):
    '''This function computes the sum of the squares of the integers from 1 to n.'''
    sum=0
    for i in range(n+1):
        sum+=i**2
    return sum
def sumofcubes(n):
    '''This funciton computes the sum of the cubes of the integers from 1 to n.'''
    sum=0
    for i in range(n+1):
        sum+=i**3
    return sum

        
        
