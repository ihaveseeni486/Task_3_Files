import os

if __name__ == '__main__':

    fileLogName = 'files\\result_file.txt'
    with open(fileLogName, mode="w+", encoding='utf-8') as w_file:
        w_file.seek(0)
        w_file.close()

    dict_files = {}
    file_path = os.path.join(os.getcwd(), "files\\")
    with os.scandir(file_path) as listOfEntries:
        for entry in listOfEntries:
            # печать всех записей, являющихся файлами
            if entry.is_file():
                with open(entry.path, mode="r", encoding='utf-8') as r_file:
                    text_got = r_file.readlines()
                    list_mini = []
                    l = dict_files.get(len(text_got), 0)
                    if l != 0:
                        list_mini.append(l)
                    minidict = {}
                    minidict['filename'] = entry.name
                    minidict['text_got'] = text_got
                    list_mini.append(minidict)
                    dict_files[len(text_got)] = list_mini
                    r_file.close()

    with open(fileLogName, mode="w+", encoding='utf-8') as w_file:
        w_file.seek(0)
        flag = True
        while flag:
            max_val = max(dict_files.keys())
            values_to_write = dict_files.get(max_val)
            for vtr in values_to_write:
                a = vtr['filename']
                b = vtr['text_got']
                w_file.writelines(a + "\n")
                w_file.writelines(str(max_val) + "\n")
                w_file.writelines(''.join(b) + "\n")
            del dict_files[max_val]
            if len(dict_files) == 0:
                flag = False