class Student:

    def __init__(self, name:str, surname = None, age:int = 0, note:float = 0.0):
        self.__name = name
        self.surname = surname
        self.age = age
        self.__note = note

    def change_note(self,new_note:float):
        if 0 < new_note <=100:
            self.__note = new_note
        else:
            raise ValueError("Invalid note. Must be between 0 and 100.")

    def get_info(self):
        if not self.surname:
            full_name = f"{self.__name}"
        else:
            full_name = f"{self.__name} {self.surname}"
        return f"{full_name}, age: {self.age}, avg_note: {self.__note}"

student1 = Student('Stepan','Bandera',43, 94.0)
student2 = Student("Andrew","Cowboy")
student3 = Student(name = "Steve",age = 23)

print(student1.get_info())
student1.change_note(99.0)
print(student1.get_info())
print("_"*40)

print(student2.get_info())
student2.age = 12
print(student2.get_info())
print("_"*40)

print(student3.get_info())
student3.surname = "Jobs"
print(student3.get_info())
