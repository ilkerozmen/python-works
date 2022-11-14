# inheritance (Kalıtım): Miras alma
 # Person => name, lastname, age, eat(), run(), drink()
 # Student(Person), Teacher(Person)
 # Animal => Dog(Animal), Cat(Animal)

class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        # print("Person Created")
    def who_am_i(self):
        print("I am a person.")
    def eating(self):
        print("I am eating.")

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.studentNumber = number
        # print("Student Created")
    
    # override                               student üzerinden person sınıfından çağırılan bir metod person sınıfındaki kodu ezer buna override denir.
    def who_am_i(self):
        print("I am a student.")

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch
    
    def who_am_i(self):
        print(f"I am a {self.branch} teacher.")
        

p1 = Person('İlker', 'Özmen')
s1 = Student('Müsemma', 'Altındaş', 123)
t1 = Teacher('Serkan', 'Aslan', 'Math')

print(p1.firstName + ' ' + p1.lastName)
print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()
t1.who_am_i()
p1.eating()
s1.eating()
