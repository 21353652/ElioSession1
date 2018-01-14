#WEEK 10-11 - QUESTION 2-1

# Class variables definition



class Student():
    
    def __init__ ( self, surname, name, sid , course ):
        self.surname = surname
        self.name = name
        self.sid = sid
        self.course = course

    def showDetails(self):
        
        print( " \nList of student information :\n\t")
        print ( " Surname :\t", " Name :\t"," Student number :\t\t","Course :")
        print( self.surname,"\t", self.name,"\t\t", self.sid,"\t\t", self.course)

    def updatenewSurname(self,newSurname):
        self.surname = newSurname
        print ( " newSurname is : ",newSurname)
    def updatenewname(self,newname):
        self.name = newname
        print ( " newname is :", newname)
   

# testing

# create a person

onestudent = Student("Incon","Elio",54665465,"CS")
onestudent.showDetails()
onestudent.updatenewSurname("Joe")

onestudent.showDetails()
