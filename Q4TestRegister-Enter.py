#WEEK 12 - QUESTION 4

from Q4TestRegister import TestRegister

cash = TestRegister()

print(" The Total amount of the price is : £ ",cash.getTotal())
print(" The Total number of items are : ",cash.getCount())
print("----------------------------------------") 

cash.addItem(99)

print(" The Total amount of the price is : £ ",cash.getTotal())
print(" The Total number of items are : ",cash.getCount())
print("----------------------------------------")

pay = float(input ( " How many money do you give me ? £ "))

print("Your change is : £ ",cash.givechange(pay))
print("----------------------------------------")

cash.clear()

print(" Cash class variable values after clearing : " ) 
print(" The Total amount of the price is : £ ",cash.getTotal())
print(" The Total number of items are : ",cash.getCount())



