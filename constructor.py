# constructor
    # เป็น Method พิเศษที่จะถูกใช้งานเมื่อตอนเริ่มสร้างวัตถุ (ไม่ระบก็ุได้)
    # โครงสร้าง Constructor
        # def __init__(self):
        #     pass

# destructor
# เป็น method พิเศษตรงข้ามกับ constuctor จะถูกใช้งานเมื่อ
# สิ้นสุดการทำงานของ class หรือถูกทำก่อนจะสลาย objact
# ส่วนใหญ่จะเป็นกลุ่มคำสั่งที่มีหน้าที่ดีหน่วยความจำให้ระบบ (ไม่ระบุก็ได้)
# โครงสร้าง
# def __dal__(self):
# pass

# การสร้าง Constructor

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {} '.format(self.salary))
        print('แผนก = {}'.format(self.department))

# มีหรือไม่มีก็ได้ destructor
    def __del__(self):
        print('call destructor')

emp1 = Employee('แซ็ค มิวสิค จ.นครพนม',50000,50)
emp1.showData()

emp2 = Employee('จาตุรนต์',25000,1)
emp2.showData()

emp3 = Employee('salary',100000,10)
emp3.showData()

emp4 = Employee('plim', 50000, 'He')
emp4.salary = 20000
emp4.showData()
