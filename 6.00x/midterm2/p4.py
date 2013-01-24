class Person(object):
    def __init__(self, name):
        self.name = name
    def __lt__(self, other):
        return self.name < other.name
    def __str__(self):
        return self.name
    def getName(self):
        return self.name

class edXPerson(Person):
    nextIdNum = 0
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = edXPerson.nextIdNum
        edXPerson.nextIdNum += 1
    def getIdNum(self):
        return self.idNum
    def __lt__(self, other):
        if self.idNum == other.idNum:
            return self.name < other.name
        else:
            return self.idNum < other.idNum
    def isStudent(self):
        return isinstance(self, Student)

class Student(edXPerson):
    pass

class UniversityStudent(Student):
    pass

class SelfLearner(Student):
    def __init__(self, name):
        Student.__init__(self, name)
        self.idNum = 0

class Subject(object):
    def __init__(self):
        self.students = []

    def addStudent(self, student):
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)

    def allStudents(self):
        genStudents = sorted(self.students)
        for student in genStudents:
            yield student

    def __str__(self):
        return 'Subject with ' + str(len(self.students)) + ' students.'

p1 = edXPerson('Fred Flintstone')
p2 = UniversityStudent('Wilma Flintstone')
p3 = Student('Betty Rubble')
p4 = SelfLearner('Barney Rubble')
p5 = SelfLearner('Dino')
p = Person('Eric Grimson')

#print "1. ",
#print p2 < p3
#print "2. ",
#print p2.getIdNum() < p3.getIdNum()
#print "3. ",
#print p2.name < p3.name
#print "4. ",
#print p4 < p3
#print "5. ",
#print p4 < p5
#print "6. ",
#print p1.isStudent()
#print "7. ",
#print p3.isStudent()
#print "8. ",
#print p5.isStudent()
#print "9. ",
#print p.isStudent()

mySubject = Subject()
mySubject.addStudent(p1)
mySubject.addStudent(p2)
mySubject.addStudent(p3)
mySubject.addStudent(p4)
mySubject.addStudent(p5)

for s in mySubject.allStudents():
    print s
