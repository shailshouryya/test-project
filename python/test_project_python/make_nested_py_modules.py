import os
import shutil


def main(package_levels=None, start=1, end=2):
    remove_script_created_contents()
    if package_levels is None:
        package_levels = {
            1: {
                'subpackage_prefix': 'package_',
                'subpackage_suffixes': ['a', 'b', 'c'],
                'module_prefix': 'module_',
                'module_suffixes': ['a', 'b', 'c', 'd', 'e'],
            },
            2: {
                'subpackage_prefix': 'subpackage_',
                'subpackage_suffixes': ['a', 'b', 'c'],
                'module_prefix': '',
                'module_suffixes': ['a', 'b', 'c', 'd', 'e'],
            },
            3: {
                'subpackage_prefix': 'subpackage_',
                'subpackage_suffixes': ['a', 'b', 'c'],
                'module_prefix': '',
                'module_suffixes': ['a', 'b', 'c', 'd', 'e'],
            },
            4: {
                'subpackage_prefix': 'subpackage_',
                'subpackage_suffixes': ['a', 'b', 'c'],
                'module_prefix': '',
                'module_suffixes': ['a', 'b', 'c', 'd', 'e'],
            },
        }
    create_packages(package_levels, start, end, base_path='.', base_name='', __init__files=[])


def remove_script_created_contents():
    top_level_path, top_level_nested_directories, top_level_files = next(os.walk('.'))
    # print(top_level_path, top_level_nested_directories, top_level_files)
    for nested_directory in top_level_nested_directories:
        if nested_directory.startswith('package_'):
            remove_directory(nested_directory)


def remove_directory(directory):
    shutil.rmtree(directory)


def create_packages(package_levels, start, end, base_path, base_name, __init__files=None):
    if start <= end:
        current_level     = start
        base_name         = base_name + '.' if base_name else ''
        subpackage_prefix = package_levels[current_level].get('subpackage_prefix', '')
        for subpackage_suffix in package_levels[current_level].get('subpackage_suffixes', []):
            subpackage_name = subpackage_prefix + subpackage_suffix
            package_name    = base_name + subpackage_name
            package_path    = os.path.join(base_path, subpackage_name)
            for __init__file, __init__package_path in __init__files:
                relative_subpackage_path, relative_subpackage_name = determine_relative_subpackage_info(package_name, __init__package_path)
                __init__file.write(f'from {relative_subpackage_path} import {relative_subpackage_name}\n')
            module_suffixes = package_levels[current_level].get('module_suffixes', [])
            module_prefix   = package_levels[current_level].get('module_prefix', '')
            print(f'package_name is {package_name}')
            os.makedirs(name=package_path, mode=511, exist_ok=False)
            __init__filepath = os.path.join(package_path, '__init__.py')
            with open(__init__filepath, mode='w', encoding='utf-8', buffering=-1) as __init__file:
                create_modules_for_subpackage(package_path, package_name, module_suffixes, module_prefix, __init__file)
                __init__files.append((__init__file, package_name))
                create_packages(package_levels, start+1, end, base_path=package_path, base_name=package_name, __init__files=__init__files)
                __init__files.pop()


def determine_relative_subpackage_info(package_name, __init__package_path):
    # imports still work with the hard coded path but provide less flexibility
    # than relative imports
    #     renaming a base package would require renaming the
    #     subpackage `import` statement in the `__init__` module when
    #     the import is a hard coded import
    #         for example, renaming `package_name` to `new_package_name` would require changing
    #         `import package_name.to.subpackage.module`
    #         to
    #         `import new_package_name.to.subpackage.module`
    #         in the package_name.to.__init__.py module (new_package_name.to.__init__ module after the rename)
    #     renaming a base package would NOT require renaming the
    #     subpackage `import` statement in the `__init__` module when
    #     the import is a relative import
    #         for example, renaming `package_name` to `new_package_name` would require no change to
    #         `from . import subpackage.module`
    #         in the package_name.to.__init__.py module (new_package_name.to.__init__ module after the rename)
    relative_subpackage_path_start = len(__init__package_path)
    normalize_subpackage_path      = package_name[relative_subpackage_path_start:]
    subpackages                    = normalize_subpackage_path.split('.')
    if len(subpackages) == 2:
        relative_subpackage_path = '.'
        relative_subpackage_name = subpackages[1]
    else:
        relative_subpackage_path = '.'.join(subpackages[:-1])
        relative_subpackage_name = subpackages[-1]
    return relative_subpackage_path, relative_subpackage_name


def create_modules_for_subpackage(package_path, package_name, module_suffixes, module_prefix, __init__file):
    for module_suffix in module_suffixes:
        module_name = f'{module_prefix}{module_suffix}'
        __init__file.write(f'from . import {module_name}\n')
        module_file_path = os.path.join(package_path, f'{module_name}.py')
        with open(module_file_path, mode='w', encoding='utf-8', buffering=-1) as file:
            file.write(f'''print('{package_name}.{module_name}')\n''')
            file.write('')


if __name__ == '__main__':
    main()
