import re
import shutil
import os
import pandas as pd
from datetime import date

file_list = os.listdir('files')
df = pd.read_excel('Задание.xlsx')
folder = 'Папка{}'
date_start = date(2020, 6, 20)
date_end = date(2020, 7, 10)
codes_ca = df['Код_КА'].tolist()  # список всех кодов КА


def main():
    for i in range(4)[1:]:  # создаем папки
        os.mkdir(folder.format(i))  # получаем список сохраненных файлов
    for file in file_list:
        code_ca = re.findall(r'[P][A][_]\d+', file)  # вырезаем код КА из названия файла
        d_1(code_ca[0], file)
        d_2(code_ca[0], file)
        check_date(code_ca[0], file)
    return


def d_1(ka, file_name):
    cond = df.iloc[codes_ca.index(ka), 3]  # получаем условие из мастер-файла
    if cond == 1:  # если условие выполняется, копируем файл в Папку1
        shutil.copyfile('files/{}'.format(file_name), os.path.join(folder.format(1), '{}'.format(file_name)))
    return


def d_2(ka, file_name):
    if ka[-1] == ka[-2]:  # если последний и предпоследний элементы равны, копируем файл в Папку2
        shutil.copyfile('files/{}'.format(file_name), os.path.join(folder.format(2), '{}'.format(file_name)))
    return


def check_date(ka, file_name):
    cond = df.iloc[codes_ca.index(ka), 2].split('.')  # получаем дату документа из мастер-файла
    try:
        doc_date = date(int(cond[2]), int(cond[1]), int(cond[0]))  # преобразовываем в тип date
        res = date_start <= doc_date <= date_end  # сравниваем с заданным промежутком
        if res is True:  # если условие выполняется, копируем файл в Папку3
            shutil.copyfile('files/{}'.format(file_name), os.path.join(folder.format(3), '{}'.format(file_name)))
    except ValueError:
        pass
    return


if __name__ == '__main__':
    main()
