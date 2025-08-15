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
        self._name = name
        self._salary = salary
        self._department = department
        self._showData()

    # public method
    def _showData(self):
        print('ชื่อพนักงาน = {}'.format(self._name))
        print('เงินเดือน = {}'.format(self._salary))
        print('แผนก = {}'.format(self._department))

emp1 = Employee('แซ็ค มิวสิค', 50000, 'มือมิกซ์')
emp1._salary = 53000
emp1._showData()
