import pandas as pd
import os

pattern = 'КА_{}_{}_{}.txt'
double = ['акт', 'счет']
folder = 'files'
condition = 'акт,счет'
df = pd.read_excel('Задание.xlsx')


def create_files():
    os.mkdir(folder)  # создаем папку
    for i in range(len(df)):  # итерируемся по значениям из мастер-файла
        if df.iloc[i, 1] == condition:  # при отработке этого условия формируем файлы для каждого типа
            for j in double:
                f = open(os.path.join(folder, pattern.format(df.iloc[i, 0], j, df.iloc[i, 2])), 'w')
                f.close()
        else:
            # иначе формируем файл указанного типа
            f = open(os.path.join(folder, pattern.format(df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2])), 'w')
            f.close()


if __name__ == '__main__':
    create_files()
