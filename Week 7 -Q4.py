#WEEK 7 - QUESTION 4
print ( " Please enter your items. If you are done just press 'Enter'. ")
shoppinglist = []
entered = input ( " Enter your first item  please : ")
while entered != " " and entered != "":
    shoppinglist.append ( entered )
    entered = input ( " Enter another item please : ")
print( " thank you, your shopping list is : ", shoppinglist)

    
