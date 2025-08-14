"""
Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
Результат запишіть у файл result_<your_second_name>.csv
"""

from pathlib import Path
import csv

# get current dir path
base_path = Path().absolute()

#create a result folder, if not exists
result_folder_path = Path(base_path, "csv_result")
if not result_folder_path.exists():
    result_folder_path.mkdir()

#get list of required csv files
csv_files = list(csv_file for csv_file in base_path.iterdir() if (csv_file.is_file() and csv_file.suffix == ".csv"))
print(csv_files)


def remove_csv_dup_lines(original_csv,target_csv,delim):
    # reading csv files content
    clear_input = []
    with open(original_csv, mode = 'r', newline = '') as of:
        of_reader = list(csv.reader(of, delimiter = delim)) # тут при використанні delimiter = ';' дублікати не прибираються..а
        # при delimiter = ',' все, ніби, ок, хоча значення в рядку розділені  ';', а не ','. Цей момент не розумію.
        of_header = of_reader[0]
        of_content = of_reader[1:]
        for r in of_content:
            if r not in clear_input:
                clear_input.append(r)

    # creating a new csv without duplicates
    with open(target_csv,mode = 'w',newline = '') as tf:
        tf_writer = csv.writer(tf,delimiter=',')
        tf_writer.writerows(clear_input)


#launching a function with different delimiters for each file
for file in csv_files:
    if file.name == 'rmc.csv':
        delim = ','
    else:
        delim = ';'
    new_file = Path(result_folder_path, f"result_{file.name}_Romaniuk.csv")

    remove_csv_dup_lines(file,new_file,delim= delim)



