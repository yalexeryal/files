import os


def writen_new_file(name_file, direct):

    def open_dir(direct):
        directory = f'{os.getcwd()}/{direct}/'
        files = os.listdir(directory)
        return files, directory

    def _sorted_files():
        dict_dir = {}
        for file in files:
            with open(f'{directory}/{file}') as f:
                counter = 0
                for _ in f:
                    counter += 1
                dict_dir[file] = counter
        dict_dir = list(dict_dir.items())
        dict_dir.sort(key=lambda i: i[1])
        return dict_dir

    files, directory = open_dir(direct)
    lines = ''
    for k, v in _sorted_files():
        lines = lines + f'{k}\n{v}\n'
        with open(f'{directory}/{k}') as file:
            for line in file:
                lines = lines + f'{line}'
    with open(name_file, 'a') as f:
        f.write(lines)
    return 'The file is written to the current folder'


print(writen_new_file('sorted.txt', '2.4files'))
