# ClassInstanceVariable

# Class Variable คือ ตัวแปรที่ทำงานภายใน class
# ส่วนอื่นสามารถเข้าถึงข้อมูลส่วนนี้ได้เลย (static attribute)
# โดยไม่จำเป็นต้องสร้าง Object ขึ้นมา

# instance Varidble คือ ตัวแปรที่อยู่ภายใน object
# สามารถเข้าถึงข้อมูลส่วนนี้โดยต้องสร้าง Object ขึ้นมา

class Employee:
    # class variable
    _minSalary = 12000
    _minSalary = 50000
    _companyName = 'บริษัท แซ็ค มิวสิค จำกัด'

    def __init__(self, name, salary, department):
        # instance Varidble
        self.__name = name
        self.__salary = salary
        self.__department = department

    def _showData(self):
        print('ชื่อพนักงาน = {}'+self.__name())
        print('เงินเดือน = {}'+self.__salary())
        print('แผนก = {}'+self.__department())


emp1 = Employee('แซ็ค มิวสิค', 50000, 'มือมิกซ์')
print('เงินเดือนขั้นต่ำ = '+str(Employee._minSalary))
print(Employee._companyName)
