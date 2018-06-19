class Student:
    college = 'DIT'
    def __init__(self, name, rno, marks):
        self.name = name
        self.rno = rno
        self.marks = marks
    
    def display(self):
        print('Name: {}, RollNo: {}, Marks: {},'.format(self.name, self.rno, self.marks), end=' ')
        print('College:', self.college)
        
    def setCollege(self, cname):
        self.college = cname
        
    def getName(self):
        return self.name
      
s1 = Student('aavi', 1, 80)

s1.setCollege('DBIT')

s1.display()
