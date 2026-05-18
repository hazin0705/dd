class Liberalarts(Student):
    def __init__(self,name,computer,social):
        super.__init__(name,social)
        self.social = social
    
    def set_social(self,social):
        self.social = social

    def get_average(self):
        return (self.social+self.computer)/2
    


