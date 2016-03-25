# dzen
#python_course

#coding: utf - 8

#1. Найти в данной папке все файлы, в которых содержится слово python, и вывести на экран имена файлов.
#2. Посчитать общее количество найденных слов и вывести на экран
#3. Записать в файл "result.txt" список найденных файлов и число найденных слов python



#1, 2
import os
path = r'C:\Users\MARI\Desktop\PYTHON\lesson_1'  #Путь к папке

filenames = []  #Список, в который мы занесем названия файлов, с python
count_py = 0  # Счетчик количества слов python

for file in os.listdir(path):  
    f = open(path + '\\' + file) 
    u = (f.read()).upper()  
   if 'PYTHON' in u:  # Если есть нужный нам элемент, то...
            filenames.append(file)  # ...добавляем название этого файла в filenames и...
            if u.count('PYTHON') > 1:  # ... если количество вхождений > 1, то...
                count_py += u.count('PYTHON')  # считаем, сколько вхождений, и прибавляем к счетчику
            else:
                count_py += 1  # Если количество вхождений = 1, то прибавляем 1 к счетчику

print (filenames)
print (count_py)

#3

f = open(r'C:\Users\MARI\Desktop\PYTHON\lesson_1, 'w')  # Cоздаем файл result.txt.
f.write('1. List of files, which contain the word "python": \n')  # Пишем заголовок

index = 0  # Счетчик индекса элемента в filenames
while True:  
    if index == len(filenames):
        break  # Когда счетчик индекса дойдет до длины файла, останавливим 
    f.write(filenames[index] + ' \n')  # Пишем названия файлов, содержащих слово python
    index += 1

f.write('2. Count of "python": ' + str(count_py))  # Пишем общее количество слов python

