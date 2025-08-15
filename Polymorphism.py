# Polymorphism

# การพ้องรูป

# เกิดจาก poly หลากหลาย morphology รูปแบบ
# ในทางโปรแกรมคือการที่ method ชื่อเดียวกัน
#สามารถรับอาร์กิวเมนต์ที่แตกต่างกันได้หลายรูปแบบ
# โดย method นี้จะถูกเรียกว่า pverload method

#Overloading
class Employee:
    __minSalary = 12000
    maxSalary = 50000
    companyName = "บริษัท XYZ จำกัด"

    def __init__(self, name, salary, department):
        self.__name = name
        self.__salary = salary
        self._department = department

    # แสดงรายละเอียด
    def _showData(self):
        print("ชื่อพนักงาน = " + self.__name)
        print("เงินเดือน = " + str(self.__salary))
        print("แผนก = " + self._department)

    # รายได้ต่อปี
    def _getIncome(self):
        return self.__salary * 12

    def __str__(self):
        return "ชื่อพนักงาน = {} , แผนก = {} , เงินเดือน = {} , รายได้ต่อปี = {}".format(
            self.__name, self._department, self.__salary, self._getIncome()
        )


class Accounting(Employee):
    __departmentName = "แผนกบัญชี"

    def __init__(self, name, salary, age):
        super().__init__(name, salary, self.__departmentName)
        self.age = age

    def _showData(self):
        super()._showData()
        print("อายุ =" + str(self.age))


class Programmer(Employee):
    __departmentName = "แผนกพัฒนาระบบ"

    def __init__(self, name, salary, experiece, skill):
        super().__init__(name, salary, self.__departmentName)
        self.experiece = experiece
        self.skill = skill

    def _showData(self):
        super()._showData()
        print("ประสบการณ์ = " + str(self.experiece) + "ปี")
        print("ทักษะ = " + self.skill)

class Sale(Employee):
    __departmentName = "แผนกขาย"

    def __init__(self, name, salary, area):
        super().__init__(name, salary, self.__departmentName)
        self.area = area

    def _showData(self):
        super()._showData()
        print("พื้นที่รับผิดชอบ = " + self.area)

account = Accounting("นัท", 35000, 35)
account._showData()
programmer = Programmer("โย", 50000, 2, "พัฒนาเกม")
programmer._showData()
sale = Sale("หนึ่ง", 25000, "เชียงคาน")
sale._showData()