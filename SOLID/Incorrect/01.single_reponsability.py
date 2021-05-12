
class Student:
    #contructor
    def __init__(self, id, full_name):
        self.id = id
        self.full_name = full_name
        
    def get_id(self):
        return self.id
    def get_full_name(self):
        return self.full_name
    
    def insert_full_name(self):
        student.append(self.full_name)
        
    def remove_full_name(self):
        student.remove(self.full_name)

#lista       
student = []
student_one = Student(1,"Christian Alatorre")
print(student_one.get_full_name())
print(student)
student_one.insert_full_name()
print(student)

student_two = Student(2,"Axel Luna")
print(student_two.get_full_name())
print(student)
student_two.insert_full_name()
print(student)
        