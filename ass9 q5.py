class expen:
    
    def __init__(self, expen, saving, ):
        self.expen = expen
        self.saving = saving
        
    
    def display(self):
        print('expen: {}, saving: {}, '.\
              format(self.expen, self.saving), end=' ')
        
      
s1 = expen(1200,1300)

s1.display()
"""s2 = Movie('xyz', 'anil', 18,4)

s2.display()"""
