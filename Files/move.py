import os 
import shutil

origin_path = input('Origin path: ')
new_path = input('New path: ')

count=0
try:
    os.mkdir(new_path)
except FileExistsError:
    print(f'{new_path} already exists')

#change origin_path to new_path to remove files
for root, dirs, files in os.walk(origin_path): 
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(new_path, file)

        shutil.move(old_file_path, new_file_path)

        #os.remove(new_file_path) #remove files
        count += 1
print(f'executed {count} times')