from Q2Class import Student

#WEEK 10-11 - QUESTION 2-2

# ENTER STUDENT DETAILS

def main():
    
    surname = input ( "Enter the surname of the student :" )
    name = input ( "Enter the name of the student :" )
    sid = input ( "Enter the student number of the student :" )
    course = input ( "Enter the course of the student :" )

    school = Student(surname,name,sid,course)

    school.showDetails()

    newSurname = input ( " Enter the new Surname : ")
    newname = input ( "Enter the new name : ")
    school.updatenewSurname(newSurname)
    school.updatenewname(newname)
    
    school.showDetails()

main()
