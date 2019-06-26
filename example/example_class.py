class BazelPythonExample():
    def __init__(self, person, age):
        self.person = person
        self.age = age
    
    def add_X_years(self, X_years):
        self.age += X_years

    def print_age(self):
        if self.person:
            print "Age: %d" % self.age
        else:
            print "Not a person"

man = BazelPythonExample(1, 56)
man.print_age()
man.add_X_years(15)
man.print_age()

dog = BazelPythonExample(0, 6)
dog.print_age()
dog.add_X_years(3)
dog.print_age()
