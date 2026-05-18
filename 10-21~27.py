class Student:
    def __init__(self,name,computer):
        self.name = name
        self.computer = computer
    
    def get_name(self):
        return self.name
    
    def set_computer(self,computer):
        self.computer = computer

class Science(Student):
    def __init__(self,name,computer,science):
        super().__init__(name,computer)
        self.science = science
    
    def set_science(self,science):
        self.science = science

    def get_average(self):
        return (self.science+self.computer)/2

class Liberalarts(Student):
    def __init__(self,name,computer,social):
        super().__init__(name,computer)
        self.social = social
    
    def set_social(self,social):
        self.social = social

    def get_average(self):
        return (self.social+self.computer)/2

st1 = Science('hanbit',90,80)
print(st1.get_average())
st1.set_computer(90)
print(st1.get_average())

st2 = Liberalarts('hanbit',98,88)
print(st2.get_average())
st2.set_social(96)
print(st2.get_name(),':',st2.get_average())
