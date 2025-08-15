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

class AccessExample:
    def __init__(self):
        self.public_var = "Public Variable"         # เข้าถึงได้จากทุกที่
        self._protected_var = "Protected Variable"  # เข้าถึงได้จากคลาสลูก
        self.__private_var = "Private Variable"     # เข้าถึงได้เฉพาะภายในคลาสนี้
    def show_variables(self):
        print("Inside class:")
        print("Public:", self.public_var)
        print("Protected:", self._protected_var)
        print("Private:", self.__private_var)


class SubAccessExample(AccessExample):
    def show_protected(self):
        print("Inside subclass:")
        print("Protected:", self._protected_var)
        # print("Private:", self.__private_var)  #  จะเกิด error เพราะเข้าถึงไม่ได้


# สร้างอ็อบเจกต์
obj = AccessExample()
obj.show_variables()

print("\nAccess from outside the class:")
print("Public:", obj.public_var)           #  เข้าถึงได้
print("Protected:", obj._protected_var)    #  เข้าถึงได้แต่ไม่ควรทำ
# print("Private:", obj.__private_var)     #  จะเกิด error

# วิธีเข้าถึง private (ไม่แนะนำ แต่ทำได้ด้วย name mangling)
print("Private (via name mangling):", obj._AccessExample__private_var)

# ทดสอบการเข้าถึงจากคลาสลูก
sub_obj = SubAccessExample()
sub_obj.show_protected()
