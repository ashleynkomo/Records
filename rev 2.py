class Student_Marks():
    def __init__(self):
        self.name = None
        self.mark = None

def StudentRecord():
    student_List = []
    for count in range(3):
        student_List.append(Student_Marks())
    for records in student_List:
        records.name = input("Please enter the students name: ")
        records.mark = int(input("Please enter the students mark: "))
    return student_List

def Display_students(student_List):
    for student in student_List:
        print("{0}'s mark is {1}".format(new_Student.name, new_Student.mark))


#main
students = StudentRecord()
Display_students()
