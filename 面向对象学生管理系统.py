#!/usr/bin/env python  
# -*- coding: utf8 -*- 
# @Time : 2020/10/20 0:13
__author__ = 'andy chen'

"""
最简单的函数式编程实现学生管理系统的基本功能
***********************************
欢迎使用【学生管理系统】V1.0
    1.显示所有学生信息
    2.新建学生信息
    3.查询学生信息
    4.修改学生信息
    5.删除学生信息
    0.退出系统
***********************************
"""

from datetime import datetime

#模拟的学生数据
data = [
    {
        'id': 15758224955,
        'name': 'Tom',
        'sex': '男',
        'birthday': '19980203'
    },
    {
        'id': 1575825000,
        'name': 'Jerry',
        'sex': '男',
        'birthday': '20010304'
    },
    {
        'id': 1575825032,
        'name': 'Kitty',
        'sex': '女',
        'birthday': '20020405'
    },
    {
        'id': 1575825036,
        'name': 'Merry',
        'sex': '女',
        'birthday': '20010606'
    }
]

#学生类
class Student:
    #学生初始化
    def __init__(self,name,sex,birthday):
        self.name = name
        self.sex = sex
        self.birthday = birthday

    #获取学生年龄
    def get_age(self):
        # 获取现在的年份
        this_year = datetime.now().year
        age = this_year - int(self.birthday[:4])
        return age

#学生管理系统类
class StudentSystem:
    def __init__(self,name):
        self.name = name
        self.data = []

    #美化输出打印
    def beauty_print(self,data_list):
        for index, student in enumerate(data_list):
            print(f'序号: {index}',end='\t')
            print(f'姓名: {student.name}',end='\t')
            print(f'性别: {student.sex}', end='\t')
            print(f'年龄: {student.get_age()}')

    #加载数据
    def load_data(self):
        for item in data:
            student = Student(item['name'],item['sex'],item['birthday'])
            self.data.append(student)

    #启动学生管理系统
    def start(self):
        #在系统启动时：第一步是加载数据
        self.load_data()
        while True:
            self.show_menu()
            op = input('选择操作: ')
            if op == '1':
                self.show_all_student()
            elif op == '2':
                self.create_student()
            elif op == '3':
                self.find_student()
            elif op == '4':
                self.modify_student()
            elif op == '5':
                self.remove_student()
            elif op == '0':
                print('退出系统')
                break
            else:
                print('请输入正确的操作')

    #显示菜单
    def show_menu(self):
        print(f"""
        ******************************
        欢迎使用【{self.name}】
        1.显示所有学生信息
        2.新建学生信息
        3.查询学生信息
        4.修改学生信息
        5.删除学生信息
        0.退出系统
        ******************************
        """)

    # 校验姓名不能为空和只输入空格
    def input_name(self):
        while True:
            # 去掉首尾空格
            name = input('输入姓名: ').strip()
            if name:
                return name
            else:
                continue

    # 选择性别
    def choose_sex(self):
        while True:
            print('1(男）|2（女）')
            n = input('选择性别：')
            if n == '1':
                return '男'
            elif n == '2':
                return '女'
            else:
                return '未知'

    # 根据名字查询学生
    def find_student_by_name(self):
        name = self.input_name()
        find_list = []
        for student in self.data:
            if name.lower() in student.name.lower():
                find_list.append(student)
        if find_list:
            return find_list
        else:
            print(f'没有找到此学生: {name}')

    # 1.显示所有学生信息
    def show_all_student(self):
            self.beauty_print(self.data)

    # 2.新建学生信息
    def create_student(self):
        name = self.input_name()
        sex = self.choose_sex()
        birthday = input('输入生日:')
        student = Student(name,sex,birthday)
        self.data.append(student)

    # 3.查询学生信息
    def find_student(self):
        find_list = self.find_student_by_name()
        self.beauty_print(find_list)

    # 4.修改学生信息
    def modify_student(self):
        find_list = self.find_student_by_name()
        if find_list:
            self.beauty_print(find_list)
            index = int(input('请选择修改的序号：'))
            # 判断序号是否在查询的学生信息中
            if index < len(find_list):
                student = find_list[index]
                print('当前修改的是：')
                self.beauty_print([student])
                name = input('输入修改的姓名：').strip()
                sex = self.choose_sex()
                birthday = input('输入修改的生日：')
                if name:
                    student.name = name
                if sex:
                    student.sex = sex
                if birthday:
                    student.birthday = birthday
            else:
                print('你输入的序号不存在！')

    # 5.删除学生信息
    def remove_student(self):
        find_list = self.find_student_by_name()
        if find_list:
            self.beauty_print(find_list)
            index = int(input('选择删除的序号：'))
            if index < len(find_list):
                print('当前要删除的是：')
                student = find_list[index]
                self.beauty_print([student])
                self.data.remove(student)
            else:
                print('您选择的序号不存在！！！')

if __name__ == '__main__':
    student_sys = StudentSystem('波大学生系统')
    student_sys.start()
