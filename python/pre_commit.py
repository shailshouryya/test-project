import mypy.main


def main():
    package_configs = [
        ['-p', 'test_project_python'],
        ['-p', 'test_project_python_tests'],
    ]
    for package_config in package_configs:
        print(f'''mypy {' '.join(package_config)}''')
        mypy.main.main(args=package_config, clean_exit=True)



if __name__ == '__main__':
    main()
