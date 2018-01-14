#WEEK 12 - QUESTION 3

from Q3CashRegister import CashRegister

cash = CashRegister()

print(" The Total amount of the price is : £ ",cash.getTotal())
print(" The Total number of items are : ",cash.getCount())
print("----------------------------------------") 

cash.addItem(99)

print(" The Total amount of the price is : £ ",cash.getTotal())
print(" The Total number of items are : ",cash.getCount())
print("----------------------------------------")

cash.clear()

print(" Cash class variable values after clearing : " ) 
print(" The Total amount of the price is : £ ",cash.getTotal())
print(" The Total number of items are : ",cash.getCount())



