import numpy as np
import pandas as pd
import os
import shutil

file_categories= {
        'Images': ['.jpeg', '.jpg', '.png', '.gif', '.tiff', '.psd', '.ai', '.raw'],
        'Videos': ['.avi', '.flv', '.wmv', '.mov', '.mp4', '.webm', '.vob', '.mng', '.qt', '.mpg', '.mpeg', '.3gp'],
        'Documents': ['.txt', '.pdf', '.doc', '.docx', '.odt', '.xls', '.xlsx', '.ods', '.ppt', '.pptx', '.odp', '.csv'],
        'Audio': ['.mp3', '.wav', '.wma', '.ogg', '.flac', '.alac', '.aiff', '.aac'],
        'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z', '.dmg'],
        'Executables': ['.exe', '.msi'],
        'Python Scripts': ['.py'],
        'Shell Scripts': ['.sh'],
        'HTML': ['.html'],
        'CSS': ['.css'],
        'JavaScript': ['.js'],
        'JSON': ['.json'],
        'XML': ['.xml'],
        'Java': ['.java'],
        'C++': ['.cpp'],
        'C': ['.c'],
        'Ruby': ['.rb'],
        'Perl': ['.pl'],
        'SQL': ['.sql'],
        'PHP': ['.php'],
        'Batch Files': ['.bat'],
        'C#': ['.cs'],
        'Go': ['.go'],
        'Swift': ['.swift'],
        'others': []
    }

def directory_opener(directory_path):
    if not os.path.exists(directory_path):
        print("The directory does not exist")
        return
    os.chdir(directory_path)
    list_of_files_and_folders = os.listdir()
    
    return list_of_files_and_folders

def make_folder(folder_path):
    for categories in file_categories.keys():
        category_path = os.path.join(folder_path, categories)
        if not os.path.exists(category_path):
            os.mkdir(category_path)


def file_oraniser(folder_path, list_of_files):
    for file in list_of_files:
        file_path = os.path.join(folder_path,file)
        if os.path.isfile(file_path):
            moved_file = False
            for categories in file_categories.keys():
                for extension in file_categories.get(categories):
                    if file.lower().endswith(extension):
                        destination_path = os.path.join(folder_path, categories,file)
                        shutil.move(file_path, destination_path)
                        moved_file = True
                        break
            if not moved_file:
                destination_path = os.path.join(folder_path,"others", file)     
                shutil.move(file_path, destination_path)
    print("File organised Successfully")


        
    
if __name__ == '__main__':
    path = input("Enter the path of the directory to be organised: ")
    files = directory_opener(path)
    print(f'The following is the list of folders and files in the input path \'{path}\' \n {files}')
    make_folder(path)
    file_oraniser(path, files)




