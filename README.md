# business_optimization
Оптимизация части бизнес-процесса, целью которого является ежемесячная выгрузка и отправка документов Контрагентам. 
1)  Скрипт для формирования пустых файлов в формате *.txt с названием по шаблону "КА_<Код КА>_<тип_документа>_<дата>" по списку во вложении
   <Код КА> - значение из столбца А
   
   <тип_документа> - значение из столбца B. 
   !Значения типа документа могут быть указаны через запятую, в таком случае по каждому из них нужно сформировать отдельный файл
   
   <дата> - значение из столбца C
   
   + сохранение этих файлов в отдельную папку

2)  Второй скрипт получает список сохраненных файлов из папки и распределяет их по подпапкам при выполнении условия:
   Папка1) Файлы, по которым в мастер-файле в столбце D установлено значение 1
   Папка2) Файлы, у которых в названии файла 2 последние цифры <Кода_КА> одинаковые, например, PA_00011, PA_00022
   Папка3) Файлы, с датой в промежутке от 20.06.2020 до 10.07.2020
	   Если файл подходит под несколько условий, то скрипт делает его копию (копирует во все папки по условиям)
