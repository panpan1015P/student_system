class Student:
    name: str
    id: int
    sex: str

class StudentManagement(Student):

    def __init__(self):
        self.student = {}
        self.count = 1000
    def addStudent(self,name,sex):
        # 加入计数器，实现自动分配id
        self.count += 1
        id = self.count
        self.student[id] = {"name":name,"sex":sex}

    def showStudent(self):
        print("添加的学员信息")
        for id in self.student:
            print(f"学号：{id}，姓名：{self.student[id]['name']}，性别：{self.student[id]['sex']}")

s1=StudentManagement()
s1.addStudent(name="张三",sex="男")
s1.addStudent(name="莉丝",sex="女")
s1.addStudent(name="王武",sex="男")
s1.showStudent()