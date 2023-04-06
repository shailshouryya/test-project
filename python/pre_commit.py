import os
import subprocess

import mypy.main
import pylint.lint


def main():
    changed_py_files = subprocess.getoutput('git diff --name-only --staged "*.py"').splitlines()
    lint_changed_py_files(changed_py_files)
    package_configs = [
        ['-p', 'test_project_python'],
        ['-p', 'test_project_python_tests'],
    ]
    for package_config in package_configs:
        print(f'''mypy {' '.join(package_config)}''')
        mypy.main.main(args=package_config, clean_exit=True)


def lint_changed_py_files(changed_py_files):
    config_path    = os.path.join('python', '.pylintrc')
    pylint_options = f'--rcfile={config_path}'
    for changed_py_file in changed_py_files:
        # pylint.run_pylint(pylint_options + [changed_py_file])
        # # calls pylint.lint.Run(argv or sys.argv[1:])
        # # but does not allow specifying the reporter, exit, do_exit
        # # arguments to pylint.lint.Run.__init__
        pylint.lint.Run(args=[pylint_options, changed_py_file], exit=False)



if __name__ == '__main__':
    main()
