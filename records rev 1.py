class Student_Marks():
    def __init__(self):
        self.name = None
        self.mark = None

def StudentRecord():  
    new_Student = Student_Marks()
    new_Student.name = input("Please enter the students name: ")
    new_Student.mark = int(input("Please enter the students mark: "))
    print("The student's name is {0}".format(new_Student.name))
    print("The student's mark is {0}".format(new_Student.mark))

#main
StudentRecord()
