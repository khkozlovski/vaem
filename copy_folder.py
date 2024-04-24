from imports import os, shutil, filecmp, dircmp, pathlib
from variables import documents


def check_source():  #this should compare original to copy
    directory = documents
    comparison = filecmp.dircmp(directory + 'source', directory + 'replica')
    comparison.report()
    # common_files = ', '.join(comparison.common)
    # left_only_files = ', '.join(comparison.left_only)
    # right_only_files = ', '.join(comparison.right_only)
    # with open(documents + 'folder_diff.txt', 'w') as folder_report:
    #     folder_report.write('Common Files: ' + common_files + '\n')
    #     folder_report.write('\n' + 'Only in Source Folder: ' + left_only_files + '\n')
    #     folder_report.write('\n' + 'Only in Replica Folder: ' + right_only_files + '\n')

    # match, mismatch, errors = filecmp.cmpfiles(source, replica, common)
    #
    # print("Shallow comparison:")
    # print("Match :", match)
    # print("Mismatch :", mismatch)
    # print("Errors :", errors, "\n")
    #
    # match, mismatch, errors = filecmp.cmpfiles(source, replica, common, shallow=False)
    #
    # print("Deep comparison:")
    # print("Match :", match)
    # print("Mismatch :", mismatch)
    # print("Errors :", errors)


def backup_update():
    check_source_update = check_source()
    update = copy_directory()
    if check_source_update is True:
        update()


check_source()
