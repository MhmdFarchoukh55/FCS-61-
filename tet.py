class aminal:
    def __init__(self,name,yearBirth):
        self.name=name
        self.yearBirth=yearBirth
    def display_name(self):
        print(self.name)
    def calculateAge(self):
        x=2025-self.yearBirth
        print("your age is ", x)
class Bird(aminal):
    def __init__(self,name,yearBirth,color):
        self.color=color
        super().__init__(name,yearBirth)
    def BirdColor(self):
        print("the brid color is ",self.color,aminal.display_name())
    
a=aminal("zouzou",2005)
a.display_name()
a.calculateAge()
b=Bird("sousso",2003,"red")
b.BirdColor()
b.display_name()