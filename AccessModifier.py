# AccessModifier
# คือระดับในการเข้าถึง class attribute method และอื่นๆ ในภาษาเชิงวัตถุ
# โดยมีประโยชน์อย่ามากในเรื่องของการกำหนดระดับการเข้าถึง
# สิทธิ์ในการเข้าใช้งาน การซ้อนข้อมูล และอื่นๆ

# Public คือการประกาศระดับการเข้าถึงที่เข้มงวดน้อยที่สุด หรือกล่าวได้ว่าใคร ๆ
# ก็สามารถเข้าถึงและเรียกใช้งานได้

# Protected(_) เป็นการประกาศระดับการเข้าถึงเฉพาะคลาสของตัวมันเองและคลาสลูก
# ที่สืบทอดคุณสมบัติไปใช้เท่านั้น

# Private(_) เป็นการประกาศระดับการเข้าถึงที่เข้มงวดที่สุด กล่าวคือ จะมีแต่คลาสของ
# ตัวมันเองเท่านั้นที่มีสิทธิ์ใช้งานได้

class Employee:
    def __init__(self, name, salary, department):
        # public attribute
        self.name = name
        self.salary = salary
        self.department = department

    # public method
    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('แผนก = {}'.format(self.department))

emp1 = Employee('แซ็ค มิวสิค', 50000, 'มือมิกซ์')
emp1.salary = 51000
emp1.showData()
