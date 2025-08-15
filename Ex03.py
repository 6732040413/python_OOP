# เขียนโปรแกรมสร้าง class ชื่อ Human โดยมี attribute และ Method ดังนี้
# attribute
# name เป็นชื่อของบุคคล
# age เป็นอายุของบุคคล
# method
# aging(year) รับ parameter 1 ตัว คือ year
# - แสดงอายุปัจจุบัน
# - เพิ่มอายุขึ้นเท่ากับ year
# - แสดงอายุหลังเพิ่มแล้ว

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def aging(self, year):
        print(f"Current age of {self.name}: {self.age}")
        self.age += year
        print(f"Age of {self.name} after {year} years: {self.age}")


person = Human("Jaturon", 22)
person.aging(1)
