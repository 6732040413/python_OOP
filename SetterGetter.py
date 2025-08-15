# Getter / Setter method
# Setter การกำหนดค่าให้  object
# Getter การดึงค่าจาก object

# Ex_Setter
    # def setterName(self, newname):
    #   Self.__name = newname
# Ex_Getter
    # def getName(self):
    #   return self.__name

class Employee:
    def __init__(self, name, salary, department):
        # public attribute
        self.__name = name
        self.__salary = salary
        self.__department = department

    # public method
    def showData(self):
        print('ชื่อพนักงาน = {}'+self.getName())
        print('เงินเดือน = {}'+self.getSalary())
        print('แผนก = {}'+self.getDepartment())

# setter nethod
    def setName(self, newname):
        self.__name = newname
    def setSalary(self, newsalary):
        self.__salary = newsalary
    def setDepartment(self, newdepartment):
        self.__department = newdepartment

    # getter method
    def getName(self):
        return self.__name
    def getSalary(self):
        return self.__salary
    def getDepartment(self):
        return self.__department

emp1 = Employee('แซ็ค มิวสิค', 50000, 'มือมิกซ์')
print('พนักงานดีเด่นประจำปี = {}'.format(emp1.getName()))
print('เงินเดือน = {}'.format(emp1.getSalary()))
print('แผนก = {}'.format(emp1.getDepartment()))
