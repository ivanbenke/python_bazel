class BazelPythonExample():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def add_X_years(self, X_years):
        self.age += X_years

    def print_age(self):
        print "Age: %s" % self.age
    
    def print_name(self):
        print "Name: %s" % self.name


# man = BazelPythonExample("Mark", 56)
# man.print_name()
# man.print_age()
# man.add_X_years(15)
# man.print_age()

# dog = BazelPythonExample("Rex", 6)
# dog.print_name()
# dog.print_age()
# dog.add_X_years(3)
# dog.print_age()
