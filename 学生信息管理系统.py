#!/usr/bin/env python  
# -*- coding: utf8 -*- 
# @Time : 2020/10/19 1:12
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
#所有的学生数据，用一个列表模拟学生数据库
data = [
    {
        'id': 15758224955,
        'name': 'Tom',
        'sex': '男',
        'address': '肇庆'
    },
    {
        'id': 1575825000,
        'name': 'Jerry',
        'sex': '男',
        'address': '清远'
    },
    {
        'id': 1575825032,
        'name': 'Kitty',
        'sex': '女',
        'address': '广州'
    },
    {
        'id': 1575825036,
        'name': 'Merry',
        'sex': '女',
        'address': '佛山'
    }
]


# 美化显示
def beauty_print(data_list):
    for index, student in enumerate(data_list):
        print(f'序号：{index}', end='\t')
        print(f'姓名：{student["name"]}', end='\t')
        print(f'性别：{student["sex"]}', end='\t')
        print(f'地址：{student["address"]}')

# 输入名字
def input_name():
    while True:
        name = input('输入名字：').strip()
        if name:
            return name
        else:
            continue

# 选择性别
def choose_sex():
    while True:
        print('1(男）|2（女）')
        n=input('选择性别：')
        if n == '1':
            return '男'
        elif n == '2':
            return '女'
        else:
            continue

#1.显示所有学生信息
def show_all():
    beauty_print(data)

#2.新建学生信息
def create_student():
    name = input_name()
    sex = choose_sex()
    address = input('输入地址： ')
    student =  {
         'name': name,
         'sex': sex,
         'address': address
    }
    data.append(student)

#3.查询学生信息
def find_student():
    name = input('查询学生的名字: ')
    for student in data:
        if student['name'] == name:
            print(student)
            return  #查询到学生后，返回到函数就结束了
    else:
        print('查无此人')

#4.修改学生信息
def modify_student():
    name = input('查询学生的名字: ')
    for student in data:
        if student['name'] == name:
            print(student)
            student['name'] = input('输入名字: ')
            student['sex'] = input('输入性别: ')
            student['address'] = input('输入地址： ')
    else:
        print('查无此人')

#5.删除学生信息
def remove_student():
    name = input('查询学生的名字: ')
    for student in data:
        if student['name'] == name:
            print(student)
            data.remove(student)
            return
    else:
        print('查无此人')

while True:
    print("""
***********************************
欢迎使用【学生管理系统】V1.0
    1.显示所有学生信息
    2.新建学生信息
    3.查询学生信息
    4.修改学生信息
    5.删除学生信息
    0.退出系统
***********************************
    """)
    op = input('请输入序号: ')
    if op == '1':
        show_all()
    elif op == '2':
        create_student()
    elif op == '3':
        find_student()
    elif op == '4':
        modify_student()
    elif op == '5':
        remove_student()
    elif op == '0':
        print('退出系统')
        break
