# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('Task02.txt', 'r') as stream_w:

    my_stream_list = [i for i in stream_w]

rows_number = len(my_stream_list)

print(f'Количество строк = {rows_number}')

for i in range(0, rows_number):
    print(f'Количество слов в строке {i+1} =', end=' ')
    print(len(''. join(my_stream_list[i]).split()))
