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
        print(f'package_name is {package_name}')
        os.makedirs(name=package_name, mode=511, exist_ok=False)
        __init__filepath = os.path.join(package_name, '__init__.py')
        with open(__init__filepath, mode='w', encoding='utf-8', buffering=-1) as file:
            file.write('\n')
        for first_level_module in module_letters:
            module_name = f'module_{first_level_module}'
            module_file_path = os.path.join(package_name, f'{module_name}.py')
            with open(module_file_path, mode='w', encoding='utf-8', buffering=-1) as file:
                file.write(f'''print('{package_name}.{first_level_module}')\n''')
                file.write('')
        for second_level in package_letters:
            second_level_path = os.path.join(package_name, f'subpackage_{second_level}')
            second_level_name = f'{package_name}.subpackage_{second_level}'
            os.makedirs(name=second_level_path, mode=511, exist_ok=False)
            second_level__init__filepath = os.path.join(second_level_path, '__init__.py')
            with open(second_level__init__filepath, mode='w', encoding='utf-8', buffering=-1) as file:
                file.write('\n')
            for second_level_module in module_letters:
                second_level_module_name = f'{second_level_module}'
                second_level_module_file_path = os.path.join(second_level_path, f'{second_level_module_name}.py')
                with open(second_level_module_file_path, mode='w', encoding='utf-8', buffering=-1) as file:
                    file.write(f'''print('{second_level_name}.{second_level_module}')\n''')


if __name__ == '__main__':
    main()
