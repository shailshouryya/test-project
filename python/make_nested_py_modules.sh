# DEPRECATED
# leaving this here for reference, but future work
#   will take place in make_nested_py_modules.py to
#   more easily support cross-platform builds

rm -r package_*
for package_letter in {a..c}; do
    package_name="package_$package_letter"
    echo "package_name is $package_name"
    mkdir -p $package_name
    echo "" > $package_name/__init__.py
    for first_level_module in {a..e}; do
        echo "print('$package_name.$first_level_module')" > $package_name/module_$first_level_module.py;
    done
    for second_level in {a..c}; do
        second_level_path="$package_name/subpackage_$second_level"
        second_level_name="$package_name.subpackage_$second_level"
        mkdir -p $second_level_path
        echo "" > $second_level_path/__init__.py
        for second_level_module in {a..e}; do
            echo "print('$second_level_name.$second_level_module')" > $second_level_path/$second_level_module.py;
        done
    done
done
