#OOPS Concepts:
class animal:
  species = None
  name = None
  sound = None
 
  def __init__(self, name, species, sound, color): # Include the 'self' in the 'init'
    self.name = name
    self.species = species
    self.sound = sound
    self.color = color

class bird(animal):

 def __init__(self):
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"
    self.color = "green"


cow = animal("Ermintrude", "Bo Taurus", "Moo", "black")
print(cow.sound)

print()
#Methods
class animal:
  species = None
  name = None
  sound = None

  def __init__(self, name, species, sound):
    self.name = name
    self.species = species
    self.sound = sound

  def talk(self):
    print((f"{self.name} says {self.sound}"))

dog = animal("Brian", "Canine", "Woof")
dog.talk()

cow = animal("Ermintrude", "Bo Taurus", "Moo")
cow.talk()

print()
#Inheritance
class animal:
  species = None
  name = None
  sound = None

  def __init__(self, name, species, sound):
    self.name = name
    self.species = species
    self.sound = sound


class bird(animal):

  def __init__(self):
    self.name = "Bird"
    self.species = "Avian"
    self.sound = "Tweet"

polly = bird()

print()


#Day 64 Challenge
class job:
  name = None
  salary = None
  hoursWorked = None

  def __init__(self, name, salary, hoursWorked):
    self.name = name
    self.salary = salary
    self.hoursWorked = hoursWorked

  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")

class doctor(job):
  experience = None
  speciality = None

  def __init__(self, salary, hoursWorked, experience, speciality):
    self.name = "Doctor"
    self.salary = salary
    self.hoursWorked = hoursWorked
    self.experience = experience
    self.speciality = speciality

  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")
    print(f"{self.experience:<10} {self.speciality:>21}")

class teacher(job):
  subject = None
  position = None

  def __init__(self, salary, hoursWorked, subject,  position):
    self.name = "Teacher"
    self.hoursWorked = hoursWorked
    self.salary = salary
    self.subject = subject
    self.position = position

  def print(self):
    print("== JOB ==")
    print()
    print(f"{self.name:<10} {self.salary:^10} {self.hoursWorked:>10}")
    print(f"{self.subject:<10} {self.position:>21}")

lawyer = job("Lawyer", "$100,000", "40")
lawyer.print()

doc = doctor("$120,000", "48", "7", "Pediatric Consultant")
doc.print()

teach = teacher("$50,000", "48+", "CompSci", "Asst. Principal")
teach.print()
