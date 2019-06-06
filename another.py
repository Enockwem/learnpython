#Special method in python e.g __repr__, __str__, __init__

class Employee:
        raise_amt = 1.04

        def __init__(self,first,last,pay):
                self.first = first
                self.last = last
                self.email = first + '.' + last + '@gmail.com'
                self.pay = pay

        def fullname(self):
                return ('{}','-','{}'.format(self.pay * self.raise_amt))

        def apply_raise(self):
                self.pay = int(self.pay * self.raise_amt)

        def __repr__(self):
                return "Employee('{}', '{}', {})".format(self.first,self.last,self.pay)

        def __str__(self):
                return '{} - {}'.format(self.fullname(),self.email)

#Passing the class as an argument for another class
class Developer(Employee): 
        def __init__(self,first,last,pay,prog_lang):
                super().__init__(first,last,pay)
                #Employee.__init__(self,first,last,pay)
                self.prog_lang = prog_lang

class Manager(Employee):
        def __init__(self,first,last,pay,employees=None):
                super().__init__(first,last,pay)
                if employees is None:
                        self.employees = []
                else:
                        self.employees = employees

        def add_emp(self,emp):
                if emp not in self.employees:
                        self.employees.append(emp)
                        
        def print_emp(self):
                for emp in self.employees:
                        print('--->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000,'python')
dev_2 = Developer('Test', 'Employee', 60000,'java')

mgr_1 = Manager('Sue','Emil',40000,[dev_1])

# This help() method give the method resolution order that python uses
#print(help(Developer)) 
print(dev_1.email)
print(dev_2.email)
print(dev_1.fullname)
print (dev_1.pay)
print (mgr_1)
