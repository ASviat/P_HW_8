# 3) Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

my_dic =\
    {
        'One': 'Один',
        'Two': 'Два',
        'Three': 'Три',
        'Four': 'Четыре'
    }

stream_to_w = []

with open('Task03.txt', 'r', encoding='utf-8') as stream_r:

    for i in stream_r:
        i = i.split(' ', 1)
        stream_to_w.append(my_dic[i[0]] + ' ' + i[1])


print(stream_to_w)

with open('Task03_w.txt', 'w', encoding='utf-8') as stream_w:
    stream_w.writelines(stream_to_w)
