class Students:

  def __init__(self,fname,lastname,tuition):
    self.fname= fname.upper
    self.lastname = lastname.lower
    self.email = fname + '.' + lastname + "@gmail.com"
    self.tuition = tuition
  
  def student_name(self):
    return ('{}','{}'.format(fname,lastname))
  
  def amount_paid(self):
    return student_name +' pays ' + tuition

mystudent = Students('Enock','Male',1750000)
mystudent1 = Students('Timothy', 'Tumwesigye',899000)

print(mystudent.email)
print(mystudent1.email)

print(mystudent.student_name)
print(mystudent1.student_name)

print(mystudent.tuition)
print(mystudent1.tuition)