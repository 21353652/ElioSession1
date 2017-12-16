#WEEK 6 - QUESTION 5

counter=0
while counter <= 5:
    password = str(input ( " Enter the password : "))
    if password == "changeme":
        print ( " Accepted " )
        break
    elif counter <5:
        print ( " Sorry, the password is not correct !! Tray again")
        counter +=1
    else :
        print ( " Access denied, please press enter to exit and contact security to reset your password ")
        break
    
