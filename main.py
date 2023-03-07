import os


def join_files():
    dic_text = {}
    fname = {}
    for filename in os.listdir('Files'):
        with open(os.path.join('Files', filename), 'r', encoding='utf-8') as f:
            line_list = []
            count = 0
            for line_ in f:
                count += 1
                line_list.append(line_)
            if count in dic_text:
                print('Одинаковое количество строк! Сортировка не будет выполнена!')
                return
            else:
                dic_text[count] = line_list
            if count in fname:
                print('Одинаковое количество строк! Сортировка не будет выполнена!')
                return
            else:
                fname[count] = filename

    sorted_text = dict(sorted(dic_text.items()))

    for key, value in fname.items():
        for keys, values in sorted_text.items():
            if key == keys:
                sorted_text[keys].append(value)

    with open(os.path.join('output.txt'), 'w', encoding='utf-8') as w:
        for keys, values in sorted_text.items():
            w.writelines(values[-1] + '\n')
            w.writelines(str(keys) + '\n')
            w.writelines(str("".join(values[:-1])) + '\n')
    print('Операция завершена успешно!')


join_files()
