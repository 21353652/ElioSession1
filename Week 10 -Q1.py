#WEEK 10 - QUESTION 1

class Student ():
    
    def __init__ ( self, surname, name, sid , course ):
        self.surname = surname
        self.name = name
        self.sid = sid
        self.course = course

    def showDetails (self):
        
        print( " \nList of student information :\n\t")
        print ( " Surname :\t", " name :\t"," Student number :\t\t","Course :")
        print( self.surname,"\t", self.name,"\t\t", self.sid,"\t\t", self.course)



def main():
    
    surname = input ( "Enter the surname of the student :" )
    name = input ( "Enter the name of the student :" )
    sid = input ( "Enter the student number of the student :" )
    course = input ( "Enter the course of the student :" )

    school = Student(surname,name,sid,course)

    school.showDetails()

main()
