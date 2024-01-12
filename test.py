import os


dd = '/Users/azamatkaibaldiyev/GREYC_project'
# Paths for files
folder_path = os.path.join(dd, 'Tobii2_full_processing')
# Get to a folder with files
main_subfolders = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]
subfolder_name = main_subfolders[0]
#subfolder_path = os.path.join(folder_path, subfolder_name)
print(folder_path)
print(subfolder_name)
#print(subfolder_path)