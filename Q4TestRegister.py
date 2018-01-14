#WEEK 12 - QUESTION 4

class TestRegister : 
    
   def __init__(self) : 
      self._itemCount = 0 
      self._totalPrice = 0.0 
      self._pay = 0.0 
    
   def addItem(self, price) : 
      self._itemCount = self._itemCount + 1 
      self._totalPrice = self._totalPrice + price  
       
    
   def getTotal(self) : 
      return self._totalPrice 
  
   def getCount(self) : 
      return self._itemCount 
  
   def clear(self) : 
      self._itemCount = 0 
      self._totalPrice = 0.0


   def givechange(self,paid):
      return ( paid - self._totalPrice)



  
