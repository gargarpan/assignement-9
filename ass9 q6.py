class expen:
    
    def __init__(self, expen, saving,total ):
        self.expen = expen
        self.saving = saving
        self.total=expen+saving
        
    
    def display(self):
        print('expen: {}, saving: {},total{} '.\
              format(self.expen, self.saving,self.total), end=' ')
        
      
s1 = expen(1200,1300,'expen'+'saving')

s1.display()
