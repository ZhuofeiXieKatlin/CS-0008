while line !="":
    
    
    value_for_year = D.get(year)
    
    if  value_for_year == :
        D(year) = {}
        
        while True:
            movie = file.readline.rstrip("\n")
            if movie == "-" break
            actors = file.readline().rstrip("\n").split(",")
            value_for_year=D[year].get(movie)
             
             if  value_for_year==  false:
                 D[year][movie]=[]