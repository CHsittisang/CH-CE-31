from dataclasses import dataclass , field
from abc import ABC, abstractmethod
from typing import List

@dataclass
class ผุู้คน(ABC):
    ชื่อ: str
    อายุ: int
    รหัสบัตรประชาชน: int

    @abstractmethod
    def ลงคะแนน(self):
        pass

@dataclass
class ประชาชน(ผุู้คน):
    
    def ลงคะแนน(self):
        pass

@dataclass
class กกต(ผุู้คน):

    def ลงคะแนน(self):
        pass

@dataclass
class พรรคการเมือง:
    เลขพรรค: int
    ชื่อพรรค: str
    

@dataclass
class ระบบเลือกตั้ง:

    กลุ่มพรรคการเมือง: list = field(default_factory=list)
    คะแนนพรรคการเมือง: list = field(default_factory=list)

    def เพิ่มพรรคการเมื่อง(self, พรรค):
        self.กลุ่มพรรคการเมือง.append(พรรค)
        self.คะแนนพรรคการเมือง.append(0)

    def ตรวจสอบเลขพรรค(self , พรรค):
        if len(self.กลุ่มพรรคการเมือง) == 0:
            self.เพิ่มพรรคการเมื่อง(พรรค)
        else:
            for i in self.กลุ่มพรรคการเมือง:
                if i.เลขพรรค != พรรค.เลขพรรค :
                    self.เพิ่มพรรคการเมื่อง(พรรค)
                else:
                    print("พรรคนี้มีอยู่แล้ว")
                    break
            
    def แสดงรายชื่อพรรคการเมือง(self):
        for i in self.กลุ่มพรรคการเมือง:
            print(f"{i.เลขพรรค} : {i.ชื่อพรรค} ")

    def เก็บคะแนน(self):
        pass


        


d = พรรคการเมือง(เลขพรรค=10, ชื่อพรรค="ก้าวไกล")
a = พรรคการเมือง(เลขพรรค=2, ชื่อพรรค="เพื่อไทย")
c = พรรคการเมือง(เลขพรรค=1, ชื่อพรรค="ประชาธิปัตย์")
t = พรรคการเมือง(เลขพรรค=4, ชื่อพรรค="พลังประชารัฐ")
z = พรรคการเมือง(เลขพรรค=10, ชื่อพรรค="เสรีรวมไทย")
ตู่ = ระบบเลือกตั้ง()
e = [d,a,c,t,z]
for i in e:
    ตู่.ตรวจสอบเลขพรรค(i)
        

    
ตู่.แสดงรายชื่อพรรคการเมือง()



            






# from dataclasses import dataclass, field
# from abc import ABC,abstractmethod
# from typing import List

# @dataclass
# class User(ABC):
#     name: str
#     age : int
#     identity_card : str

#     @abstractmethod
#     def vote():
#         pass

# @dataclass
# class Member(User):
#     name: str
#     age : int
#     identity_card : str
    
#     def vote(self, system, political_id):
#         system.vote(political_id)
#         return system.show(political_id)

# @dataclass
# class Admin(User):
#     name: str
#     age : int
#     identity_card : str
    
#     def vote(self, system, political_id):
#         system.vote(political_id)
#         return system.show(political_id)
    
#     def โกง(self, system, political_id, qty):
#         for political in system.political_list:
#             if political.identity == political_id :
#                 political.edit_point = political.edit_point + qty
#                 print("โกง!")
#                 return political.edit_point


# @dataclass
# class Political: 
#     identity : int
#     name : str
#     point : int

#     @property
#     def edit_point(self):
#         return self.point

#     @edit_point.setter
#     def edit_point(self, qty):
#         self.point = qty

# @dataclass
# class System:
#     political_list : List[Political] = field(default_factory=list)

#     def append_political(self, political):
#         self.political_list.append(political)

#     def vote(self, id):
#         for political in self.political_list:
#             if political.identity == id :
#                 political.edit_point = political.edit_point + 1
#                 print("vote!")
#                 return political.edit_point

#     def show(self, id):
#         for political in self.political_list:
#             if political.identity == id :
#                 print("show!")
#                 return political.edit_point

# member = Member(name="WIND", age=1000,identity_card=987654321)
# admin = Admin(name="HEE", age=1000, identity_card=123456789)

# hee_hee = Political(identity = 100000, name = "HeeHee", point = 250)
# nine_near = Political(identity = 696969, name = "9near", point = 0)

# print(hee_hee.edit_point)
# print(nine_near.edit_point)

# system = System()

# system.append_political(hee_hee)
# system.append_political(nine_near)

# system.vote(100000)
# system.vote(696969)

# print(hee_hee.edit_point)
# print(nine_near.edit_point)

# member.vote(system, 100000)
# member.vote(system, 696969)

# print(hee_hee.edit_point)
# print(nine_near.edit_point)

# admin.โกง(system, 100000, 1000)

# print(hee_hee.edit_point)
# print(nine_near.edit_point)