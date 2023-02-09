# 1) Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.


def fill_it(x):

    new_value = input('Введите данные: ')

    if new_value == '':

        return -1

    else:

        x.write(new_value)
        x.write('\n')
        return fill_it(x)


with open('n_txt.txt', 'w', encoding='utf-8') as content:

    fill_it(content)
