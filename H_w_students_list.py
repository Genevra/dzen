# coding: utf-8

#Делаем программу "students_list.py".

#1. Она должна сделать следующее:

#Создаем список.
#Заполняем его нашими именами (+фамилиями).
#2. Выводим имя одного студента на экран:

#Получаем индекс через функцию input().
#Выводим на экран студента по этому индексу.
#3. Выводим на экран имена нескольких студентов:

#Получаем через input() начало и конец среза.
#Выводим на экран студентов из такого среза.
#4. Находим количество студентов, в именах которых есть буква "р".

#*5. Находим группы студентов с одинаковыми именами и создаем списки этих групп.

#1
students_list = ['Pavel Bondarev', 'Butakov Alexander', 'Daniel Ershov', 
'Anastasiya Zakharenko', 'Alexey Ivanov', 'Korolchuk Egor',
'Anton Kozhanov', 'Lekarev Andrew', 'Pavel Loginov', 
'Dmitry Makarov', 'Evgeny Makarov', 'Vitaly Makovkin', 
'Nesterenko Denis', 'Nikoghosian Ishkhan', 'Marina Petrova', 
'Yuri Ryabov', 'Daniel Savitsky', 'Dmitry Sinitckiy', 'Sukharev Kirill', 'Denis Tsyganov']

#2
student_index = int(input('Input Index Student: '))
print('Students: ', students_list[student_index],'\n')

#3
student_slice_1 = int(input('Input first argumet for slice: '))
student_slice_2 = int(input('Input second argumet for slice: '))
print('Students slice:', students_list[student_slice_1:student_slice_2], '\n')

#4
count = 0
for i in students_list:

    if 'p' in i:
        count += 1
print("Students with 'p': ", count)
