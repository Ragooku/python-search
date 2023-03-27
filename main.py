import os  # библиотека для работы с операционкой
import hashlib # библиотека для качественной передачи информации
os.chdir("Файлы")

path = '.'
r =os.listdir(path)

x = []

print('1.Создать файл 2.Открыть 3.Переменовать 4.Удалить файл 5.Сортировать по имени файла 6.Поиск по папке 123')

a = input()
if a == ('Поиск по папке 123'):
    file_hash1 = hashlib.md5()
    file_hash2 = hashlib.md5()
    m = input('Имя 1 файла: ')
    n = input('Имя 2 файла: ')
    with open(m, 'rb')as file1:
        data = file1.read()
        file_hash1.update(data)
    with open(n, 'rb')as file2:
        data1 = file2.read()
        file_hash2.update(data1)
    if file_hash1.hexdigest() == file_hash2.hexdigest():
        print("Файлы найдены")
        print(m, n)
        h = input('Введите название файла для удаления: ')
        if h == m:
            os.remove(m)
        else:
            os.remove(n)



if a == ('Создать файл'):
    file = open(input('Введите названия файла: '), 'w')

if a == ('Открыть'):
    os.startfile(input('Введите навание файла: '))

if a == ('Переменовать'):
    os.rename(input('Ведите имя файла которое нужно переменовать: '), input('Введите новое имя файла: '))

if a == ('Удалить файл'):
    os.remove(input('Введите название файла который хотите удалить: '))

if a == ('Сортировать по имени файла'):
    for n, i in enumerate(r):
        x.append(i)
    b = input()
    if b == ('С1'):
        print(sorted(x))
    else:
        print(sorted(x, reverse=True))














