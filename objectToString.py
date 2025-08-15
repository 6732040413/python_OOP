# objectToSteing

# แปลง object เป็น String
# def __str__(self):
#  return "ชุดข้อความ"

# objectToString
# แปลง Object เป็น String
# def __str__(self):
#   return "ชุดข้อความ"


class Employee:
    minSalary = 12000
    maxSalary = 50000
    companyName = "บริษัท XYZ จำกัด"

    def __init__(self, name, salary, department):
        self.__name = name
        self.__salary = salary
        self.__department = department

    # แสดงรายละเอียด
    def _showData(self):
        print("ชื่อพนักงาน = " + self.__name)
        print("เงินเดือน = " + str(self.__salary))
        print("แผนก = " + self.__department)

    # รายได้ต่อปี
    def _getIncome(self):
        return self.__salary * 12

    def __str__(self):
        return "ชื่อพนักงาน = {} , แผนก = {} , เงินเดือน = {} , รายได้ต่อปี = {}".format(
            self.__name, self.__department, self.__salary, self._getIncome()
        )


class Accounting(Employee):
    __departmentName = "แผนกบัญชี"

    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)


class Programmer(Employee):
    __departmentName = "แผนกพัฒนาระบบ"

    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)


class Sale(Employee):
    __departmentName = "แผนกขาย"

    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)


account = Accounting("นัท", 35000)
print(account.__str__())
programmer = Programmer("โย", 50000)
print(programmer.__str__())
sale = Sale("หนึ่ง", 25000)
print(sale.__str__())
