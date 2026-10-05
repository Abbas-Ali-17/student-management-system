
class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks


    def show_info(self):
         print("your name is: ",self.name)
         print("your age is: ",self.age)
         print("your marks are: ",self.marks)

    def get_average(self):
         average=0
         for x in self.marks:
             average=average+x
         average1=average/len(self.marks)
         return average1
    def update_marks(self,new_marks):
        self.marks=new_marks

    def get_result(self):
        avg =self.get_average()
        if (avg>=50):
            print("You passed the Exam : ")
        else:
            print("You failed the exam : ")

class student_manager:
    def __init__(self):
        self.students=[]


    def add_student(self,student):
        self.students.append(student)
        return student

    def view_students(self):
        for student in self.students:
            student.show_info()
    
manager=student_manager()


student1=student("Abbas",22,[80,90,95])
student2=student("ALI",23,[80,90,95])
student1.update_marks([50,60,70])

student1.show_info()
print("you marks average is: ",student1.get_average())

student1.get_result()
manager.add_student(student1)
manager.add_student(student2)
manager.view_students()