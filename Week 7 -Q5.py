#WEEK 7 - QUESTION 5
s1 = input ( " Enter the first sentence : ")
s2 = input ( " Enter the second sentence : ")
sentence =s1+" "+s2
print ("\t-------------------------")
print (" This is one long sentence concatenated with the two sentences given:\n\t", sentence )
print ("\t-------------------------")
sentence2 = sentence.split()
print (" Split the sentence into a  list of words :\n\t",sentence2)
print ("\t-------------------------")
print (" Sort the words in alphabetical order and print them out :\n\t",sorted(sentence2))
print ("\t-------------------------")
print (" Print the total number of words contained in your list :\n\t",len(sentence2))
print ("\t-------------------------")
dictionary = {}
for word in sentence2:
    dictionary[word] = sentence2.count(word)
print (" Create a dictionary :\n\t",dictionary)



