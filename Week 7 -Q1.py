#WEEK 7 - QUESTION 1
a = [ 66.25, 333, 333, 1, 1234.5 ]
a.insert(2, -1)#The method insert()does not return any value but it inserts
                #the given element at the given index. 
a.append(333)#The method append()does not return any value but updates 
             # existing list,add at the end of the list the item/s given.
print (" The new list is : ", a )
print (" The lowest index in list for the item 333: ", a.index(333))
a.remove(333)#This method remove()does not return any value but removes
            #the given object from the list.
print (" The new list after removed the item 333 is : ", a) 
a.reverse()#The method reverse()does not return any value but reverse
            #the given object from the list.
print (" The new reverse list is : ", a)
a.sort()#The method sort()does not return any value but it changes from
        #the original list.
print (" The new list with changed order of the items is : ", a ) 
