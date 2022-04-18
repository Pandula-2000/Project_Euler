# Project Euler
# Problem 19


normalMonths={'January':31 ,'February':28, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31 ,'November':30 ,'December':31}
specialMonths={'January':31 ,'February':29, 'March':31, 'April':30, 'May':31, 'June':30, 'July':31, 'August':31, 'September':30, 'October':31 ,'November':30 ,'December':31}

count = 0
day = 1
months=[] 
for year in range(1900,2001) :

    if str(year)[-2:] == '00' : #finding leap years for centuries
        if year%400 == 0:
            months=specialMonths
        else:
            months=normalMonths
    else:                       # finding leap years for rest of the years
        if year%4 == 0:
            months=specialMonths
        else:
            months=normalMonths
    
    for month in months :

        if day == 7 and year != 1900:  # they dont ask for 1900
            count = count + 1          #day==7 means its a sunday 
        for i in range(months[month] +1):#use values from the dictionary to loop through each day in month
            if day == 7:            #reset the week days
                day = 0
            day=day+1
                    
print(count)






    








    
    
