import filecmp
import os.path
import shutil
import sys
import time


def sync_folder(source_directory, replica_directory):
    comparison = filecmp.dircmp(source_directory, replica_directory)
    new_paths = full_paths_of(comparison.left_only, source_directory)
    for item_path in new_paths:
        if os.path.isfile(item_path):
            copy_file(item_path, source_directory, replica_directory)
    unwanted_paths = full_paths_of(comparison.right_only, replica_directory)
    for item_path in unwanted_paths:
        if os.path.isfile(item_path):
            remove_file(item_path, replica_directory)


def remove_file(file_path, replica_directory):
    os.remove(file_path)
    print(f'File {file_name(file_path)} removed from {replica_directory}')


def copy_file(file_path, source_directory, replica_directory):
    shutil.copy(file_path, replica_directory)
    print(f'File {file_name(file_path)} copied from {source_directory} to {replica_directory}')


def file_name(full_path):
    return os.path.split(full_path)[-1]


def full_paths_of(file_names, directory):
    return [f'{directory}/{file_name}' for file_name in file_names]


def periodically_sync_folder(source_directory, replica_directory):
    while True:
        sync_folder(source_directory, replica_directory)
        time.sleep(3)


if __name__ == '__main__':
    periodically_sync_folder(sys.argv[1], sys.argv[2])
