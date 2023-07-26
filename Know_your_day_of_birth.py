from datetime import *
Year=int(input('Enter Year : '))
Month=int(input('Enter Month : '))
Date=int(input('Enter Date : '))

day=date(Year,Month,Date).weekday()

if day==0:
    print("The Day You were born is : ","Monday")
    
        
elif day==1:
    print("The Day You were born is : ","Tuesday")
    
elif day==2:
     print("The Day You were born is : ","Wednesday")
   
elif day==3:
    print("The Day You were born is : ","Thursday")
elif day==4:
    print("The Day You were born is : ","Friday")
    
elif day==5:
    print("The Day You were born is : ","Saturday")
    
    
else:       
    print("The Day You were born is : ","Sunday")
    



# this is the code to know about on which day you were born