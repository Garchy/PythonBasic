import os

path_find = input('Path: ')
term_find = input('Filter: ')

def size_format(size):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if size < kilo:
        text = 'B'
    elif size < mega:
        size /= kilo
        text = 'K'
    elif size < giga:
        size /= mega
        text = 'M'
    elif size < tera:
        size /= giga
        text = 'G'
    elif size < peta:
        size /= tera
        text = 'T'
    else:
        size /= peta
        text = 'P'

    size = round(size, 2)
    return f'{size}{text}'    

count = 0
for root, directorys, files in os.walk(path_find):
    for file in files:
        if term_find in file:
            try:
                count += 1
                full_path = os.path.join(root, file)
                file_name, file_ext = os.path.splitext(file)
                size = os.path.getsize(full_path)
            
                print('\nFile: ', file_name)
                print('Path: ', full_path)
                print('Name: ', file_name)
                print('Extension: ', file_ext)
                print('Size: ', size)
                print('Formated size: ', size_format(size))

            except PermissionError as e:
                print('No Permission.')
            except FileNotFoundError as e:
                print('File not found.')
            except Exception as e:
                print('Unknown error.')

print(f'\n{count} file(s) found')