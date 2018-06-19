class Movie:
    
    def __init__(self, name, artist, year,rate):
        self.name = name
        self.artist = artist
        self.year= year
        self.rate = rate
    
    def display(self):
        print('Name: {}, artist: {}, year: {},rate:{}'.\
              format(self.name, self.artist, self.year,self.rate), end=' ')
        
      
s1 = Movie('race', 'salman', 18,3)

s1.display()
s2 = Movie('xyz', 'anil', 18,4)

s2.display()
