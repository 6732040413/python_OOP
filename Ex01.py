# เขียนโปรแกรมสร้าง class Tree โดยมี attribute และ method ดังนี้
# attribute
#    height เป็นความสูงต้นไม้
#    width เป็นกว้างต้นไม้
#    generated_money เป็นเงินที่หาได้
# method
#    feed_A() ทำหน้าที่แสดงค่าเงินที่หาได้ และความกว้างของต้นไม้หลังจากให้ปุ๋ยชนิด A
#    โดยจะลด generated_money 10 หน่วย แต่จะเพิ่ม wigth 12 หน่วย
#    Feed B() ทำหน้าที่แสดงค่าเงินที่หาได้ และแสดงความสูงของต้นไม้หลังจากให้ปุ๋ยชนิด B
#    โดยจะลด generated_money 8 หน่วย แต่จะเพิ่ม height 10 หน่วย
#    sell() ทำหน้าที่แสดงค่าจำนวนเงินที่ขายต้นไม้ได้ โดย generated_money จะเพิ่มเท่ากับ
#    width * height ** 0.8

class Tree:
    def __init__(self, height, width, generated_money):
        self.height = height
        self.width = width
        self.generated_money = generated_money

    def feed_A(self):
        self.generated_money = self.generated_money - 10
        self.width = self.width + 12

    def feed_B(self):
        self.generated_money = self.generated_money - 8
        self.height = self.height + 10

    def sell(self):
        self.generated_money = self.generated_money + self.width * self.height ** 0.8
        print("Width = ", self.width, "Height = ", self.height)
        print("Generated Money = ", self.generated_money)

tree_A = Tree(10, 10, 1000)
tree_A.feed_A()
tree_A.feed_B()
tree_A.sell()

print(" ")

tree_B = Tree(23, 8, 254)
tree_B.feed_B()
tree_B.sell()

print("")

tree_C = Tree(300, 14, 850)
tree_C.feed_A()
tree_C.sell()
