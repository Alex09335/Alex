day_user=int(input("enter the day:"))
month_user=int(input("enter the month:"))
year_user=int(input("enter the year:"))
def converter(day_user,month_user,year_user):
    if month_user==10 and day_user>10:
        intendedyear=year_user+622
      
    elif month_user>10:
        intendedyear=year_user+622
      
    else:
        intendedyear=year_user+621
                   
        print(intendedyear)   
          
converter(day_user,month_user,year_user)
        
        
