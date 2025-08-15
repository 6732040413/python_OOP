# FnClassObject
# ฟังก์ชั่นที่ทำงานร่วมกับ class และ object

# isinstance และ dir คือฟังก์ชั่นที่ทำงานร่วมกัน class และ object
# โดยมีรายละเอียด ดังนี้
# isinstance => เช็ดว่า object นี้ถูกสร้างจาก class ที่เรานิยามหรือไม่
# dir => แสดง attribute และ method
# __class__ => แสดงชื่อ class และ object

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {} '.format(self.salary))
        print('แผนก = {}'.format(self.department))


emp1 = Employee('แซ็ค มิวสิค จ.นครพนม',50000,50)
emp2 = Employee('จาตุรนต์',25000,1)
emp3 = Employee('salary',100000,10)
emp4 = Employee('plim', 50000, 'He')

print(isinstance(emp1, Employee)) #ตรวจสอบว่า object ถูกสร้างจาก class ที่ตรวจสอบไหม
print(dir(emp1))
print(emp1.__class__)
