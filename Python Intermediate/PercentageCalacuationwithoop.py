class  Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        
    @property
    def calcPercentage(self):
        self.percentage = str((self.phy + self.chem + self.math)/3) + "%"
        return self.percentage
stu1 = Student(90, 80, 70)
print(stu1.calcPercentage)

stu1.phy = 89
print(stu1.calcPercentage)