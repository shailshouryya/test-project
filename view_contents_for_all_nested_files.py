import os
import sys


def main(include_only='.', exclude_directory=None):
    '''
    Example usage (run from the root `test_project` directory):
    # this ignores the the .git directory in the current directory
    # note that we need to add the ./ prefix to .git directory
    $ python3 view_contents_for_all_nested_files.py . ./.git
    '''
    if len(sys.argv) > 1: include_only      = sys.argv[1]
    if len(sys.argv) > 2: exclude_directory = sys.argv[2]
    print_all_nested_files_to_console(include_only, exclude_directory)


def print_all_nested_files_to_console(directory, exclude_directory):
    for file_name in find_all_nested_files(directory, exclude_directory):
        with open(file_name, mode='r', encoding='utf-8', buffering=-1) as file:
            print(f'Contents of {file_name}:')
            print(file.read())
            print_boundary()

def find_all_nested_files(directory, exclude_directory):
    for current_directory, nested_directories, files in os.walk(directory):
        if exclude_directory is not None and current_directory.startswith(exclude_directory):
            continue
        for file in files: # does not enter this block if `files` is empty
            yield f'{current_directory}/{file}'


def print_boundary():
    print('=' * 50)


if __name__ == '__main__':
    main()
