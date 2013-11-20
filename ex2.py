    def __init__(self):
        self.hungry = True
        self.sing = 'bird'
    def eat(self):
        if self.hungry:
            print 'eat something'
            self.hungry = False
        else:
            print 'You cant eat'

class BuBu(Bird):
    def __init__(self):
        super(BuBu,self).__init__()
        
    def drink(self):
        if self.hungry:
            print "eat subsothing"
            self.hungry = False
        
    
b = BuBu()
b.eat()
b.sing
