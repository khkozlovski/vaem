import filecmp
import os.path
import shutil


def sync_folder():
    directories = 'C://Users/magwn/Documents/'
    source_directory = f'{directories}source'
    replica_directory = f'{directories}replica'
    comparison = filecmp.dircmp(source_directory, replica_directory)
    item_names = comparison.left_only
    for item_name in item_names:
        item_is_file = os.path.isfile(f'{source_directory}/{item_name}')
        if item_is_file:
            shutil.copyfile(f'{source_directory}/{item_name}', f'{replica_directory}/{item_name}')
            print(f'File {item_name} copied from {source_directory} to {replica_directory}')


sync_folder()
