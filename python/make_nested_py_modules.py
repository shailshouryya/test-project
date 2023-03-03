import os
import shutil


def main():
    remove_script_created_contents()
    create_packages(['a', 'b', 'c'], ['a', 'b', 'c', 'd', 'e'])

def remove_script_created_contents():
    top_level_path, top_level_nested_directories, top_level_files = next(os.walk('.'))
    # print(top_level_path, top_level_nested_directories, top_level_files)
    for nested_directory in top_level_nested_directories:
        if nested_directory.startswith('package_'):
            remove_directory(nested_directory)


def remove_directory(directory):
    shutil.rmtree(directory)


def create_packages(package_letters, module_letters):
    for package_letter in package_letters:
        package_name = f'package_{package_letter}'
        package_path = os.path.join('.', package_name)
        print(f'package_name is {package_name}')
        create_subpackage(package_path, package_name, module_letters, module_prefix='module_')
        for second_level in package_letters:
            second_level_name = f'{package_name}.subpackage_{second_level}'
            second_level_path = os.path.join(package_name, f'subpackage_{second_level}')
            create_subpackage(second_level_path, second_level_name, module_letters, module_prefix='')


def create_subpackage(package_path, package_name, module_letters, module_prefix):
    os.makedirs(name=package_path, mode=511, exist_ok=False)
    __init__filepath = os.path.join(package_path, '__init__.py')
    with open(__init__filepath, mode='w', encoding='utf-8', buffering=-1) as file:
        file.write('\n')
    for module in module_letters:
        module_name = f'{module_prefix}{module}'
        module_file_path = os.path.join(package_path, f'{module_name}.py')
        with open(module_file_path, mode='w', encoding='utf-8', buffering=-1) as file:
            file.write(f'''print('{package_name}.{module}')\n''')
            file.write('')


if __name__ == '__main__':
    main()
