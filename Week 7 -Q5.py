#WEEK 7 - QUESTION 5
first = str(input (" Enter the first sentence : "))
second = str(input (" Enter the second sentence : "))
long = (first + " " + second )
print ( long )
sentence = long.split ( " ")
#for i in range ( 0, len( long )):
#    sentence.append ( long[i] )
print ( sentence )
sentence.sort ()
print( len ( sentence ))
dictionary = {}
for word in sentence:
    dictionary [word] = sentence.count ( word )
print ( dictionary )

    
    
