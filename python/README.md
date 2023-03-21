# test_project_python

NOTE: substitute the alias you set for `python` on your local machine for any commands below that call `python`. Common aliases include `python`, `python3`, `py3`, `python3.x`, or `py3.x` (where `x` corresponds to the python minor release version of your installation).


This project contains a dummy python project to
- test how packaging works for python
  - using the `setuptools`  module
    - see the comments in the `setup.py` file for more references and information
  - when uploading to https://test.pypi.org/ and/or https://pypi.org/
    - references describing basic packaging information:
      - [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
      - [Python: Creating a pip installable package](https://betterscientificsoftware.github.io/python-for-hpc/tutorials/python-pypi-packaging/)
      - [GPG signing - how does that really work with PyPI?](https://github.com/pypa/twine/issues/157)
      - [Packaging and distributing projects](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/)
    - references describing more advanced packaging capabilities:
      - [Packaging namespace packages](https://packaging.python.org/en/latest/guides/packaging-namespace-packages/)
      - [Creating and discovering plugins](https://packaging.python.org/en/latest/guides/creating-and-discovering-plugins/)
      - [Packaging binary extensions](https://packaging.python.org/en/latest/guides/packaging-binary-extensions/)
    - packaging.python.org landing page: [Python Packaging User Guide](https://packaging.python.org/en/latest/)
      - maintained by [Python Packaging Authority](https://www.pypa.io/en/latest/)


## Requirements

This package uses [f-strings](https://cito.github.io/blog/f-strings/) ([learn more about f-strings here](https://realpython.com/python-f-strings/)), so this package requires Python version 3.6+ to run properly.

If you do not have Python installed, or have an older version of Python, you can download Python 3.11.2 (the latest stable version as UTC 2023-03-18) from one of the links below and follow the instructions to set up Python for your machine. If you want to install a different version, visit the [Python Downloads page](https://www.python.org/downloads/) and select the version you want.
- [Gzipped source tarball](https://www.python.org/ftp/python/3.11.2/Python-3.11.2.tgz)
- [XZ compressed source tarball](https://www.python.org/ftp/python/3.11.2/Python-3.11.2.tar.xz)
- [macOS 64-bit universal2 installer](https://www.python.org/ftp/python/3.11.2/python-3.11.2-macos11.pkg)
- [Windows embeddable package (32-bit)](https://www.python.org/ftp/python/3.11.2/python-3.11.2-embed-win32.zip)
- [Windows embeddable package (64-bit)](https://www.python.org/ftp/python/3.11.2/python-3.11.2-embed-amd64.zip)
- [Windows embeddable package (ARM64)](https://www.python.org/ftp/python/3.11.2/python-3.11.2-embed-arm64.zip)
- [Windows installer (32-bit)](https://www.python.org/ftp/python/3.11.2/python-3.11.2.exe)
- [Windows installer (64-bit)](https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe)
- [Windows installer (ARM64)](https://www.python.org/ftp/python/3.11.2/python-3.11.2-arm64.exe)
- [Instructions for downloading Python on other platforms](https://www.python.org/download/other/)

### Development requirements

The following requirements are NOT required to run the `test_project_python` package locally (after installing with `python -m pip install --upgrade test_project_python`), but ARE required to follow along with the [Building a python package for distribution](#building-a-python-package-for-distribution) section below.

```
python -m pip install --upgrade pip build twine
```

The download link below to GnuPG is NOT required for the [Building a python package for distribution](#building-a-python-package-for-distribution) section below, but will enable you to sign your package.
- https://gnupg.org/download/
- for more details about downloading, installing, and using `gpg` (and related tools), see the [GPG section](../README.md#gpg) under the [Programming language agnostic tools section](../README.md#programming-language-agnostic-tools) in the [main README in the GitHub repository](../README.md)

## Project Structure

Note that some of the files below are configuration/build/binary files auto-generated after running commands to set up the package locally, and are NOT included in the repo:
- the `python setup.py sdist` commands creates
  - `dist/test-project-python-0.0.2.post6.tar.gz`
  - `test_project_python.egg-info` (and nested contents)
- the `python setup.py bdist_wheel` command creates
  - `build/bdist.OPERATINGSYSTEMNAME-moreoperatingsysteminfo`
  - `dist/test_project_python-0.0.2.post6-py3-none-any.whl`
  - `build/lib/`(and nested contents)
  - `test_project_python.egg-info` (and nested contents)
- the `python -m pip install .` command creates
  - `build/bdist.OPERATINGSYSTEMNAME-moreoperatingsysteminfo`
  - `build/lib/`(and nested contents)
  - `test_project_python.egg-info` (and nested contents)
- the `gpg --detach-sign -a dist/test-project-python-0.0.2.post6.tar.gz` command creates
  - `dist/test-project-python-0.0.2.post6.tar.gz.asc`
- the `gpg --detach-sign -a dist/test_project_python-0.0.2.post6-py3-none-any.whl` command creates
  - `dist/test_project_python-0.0.2.post6-py3-none-any.whl.asc`

Also note that running python files as modules locally creates a `__pycache__` directory and `.pyc` file nested inside the `__pycache__` directory (which were manually excluded from the structure below) for that corresponding module!
- note that this
  - only happens when running `python3 -m path.to.module.name`
  - does NOT happen when running `python3 path/to/module/name.py`


(structure taken from the output of the `tree` command run from the `test-project/python` directory)
```
.
├── README.md
├── build
│   ├── bdist.OPERATINGSYSTEMNAME-moreoperatingsysteminfo
│   └── lib
│       ├── package_a
│       │   ├── __init__.py
│       │   ├── module_a.py
│       │   ├── module_b.py
│       │   ├── module_c.py
│       │   ├── module_d.py
│       │   ├── module_e.py
│       │   ├── subpackage_a
│       │   │   ├── __init__.py    # this __init__.py module MUST exist for setuptools to *automatically* detect subpackage_a
│       │   │   ├── a.py
│       │   │   ├── b.py
│       │   │   ├── c.py
│       │   │   ├── d.py
│       │   │   └── e.py
│       │   ├── subpackage_b
│       │   │   ├── __init__.py    # this __init__.py module MUST exist for setuptools to *automatically* detect subpackage_b
│       │   │   ├── a.py
│       │   │   ├── b.py
│       │   │   ├── c.py
│       │   │   ├── d.py
│       │   │   └── e.py
│       │   └── subpackage_c
│       │       ├── __init__.py    # this __init__.py module MUST exist for setuptools to *automatically* detect subpackage_c
│       │       ├── a.py
│       │       ├── b.py
│       │       ├── c.py
│       │       ├── d.py
│       │       └── e.py
│       ├── package_b
│       │   ├── __init__.py
│       │   ├── module_a.py
│       │   ├── module_b.py
│       │   ├── module_c.py
│       │   ├── module_d.py
│       │   ├── module_e.py
│       │   ├── subpackage_a
│       │   │   ├── __init__.py    # this __init__.py module MUST exist for setuptools to *automatically* detect subpackage_a
│       │   │   ├── a.py
│       │   │   ├── b.py
│       │   │   ├── c.py
│       │   │   ├── d.py
│       │   │   └── e.py
│       │   ├── subpackage_b
│       │   │   ├── __init__.py    # this __init__.py module MUST exist for setuptools to *automatically* detect subpackage_b
│       │   │   ├── a.py
│       │   │   ├── b.py
│       │   │   ├── c.py
│       │   │   ├── d.py
│       │   │   └── e.py
│       │   └── subpackage_c
│       │       ├── __init__.py    # this __init__.py module MUST exist for setuptools to *automatically* detect subpackage_c
│       │       ├── a.py
│       │       ├── b.py
│       │       ├── c.py
│       │       ├── d.py
│       │       └── e.py
│       ├── package_c
│       │   ├── __init__.py
│       │   ├── module_a.py
│       │   ├── module_b.py
│       │   ├── module_c.py
│       │   ├── module_d.py
│       │   ├── module_e.py
│       │   ├── subpackage_a
│       │   │   ├── __init__.py    # this __init__.py module MUST exist for setuptools to *automatically* detect subpackage_a
│       │   │   ├── a.py
│       │   │   ├── b.py
│       │   │   ├── c.py
│       │   │   ├── d.py
│       │   │   └── e.py
│       │   ├── subpackage_b
│       │   │   ├── __init__.py    # this __init__.py module MUST exist for setuptools to *automatically* detect subpackage_b
│       │   │   ├── a.py
│       │   │   ├── b.py
│       │   │   ├── c.py
│       │   │   ├── d.py
│       │   │   └── e.py
│       │   └── subpackage_c
│       │       ├── __init__.py    # this __init__.py module MUST exist for setuptools to *automatically* detect subpackage_c
│       │       ├── a.py
│       │       ├── b.py
│       │       ├── c.py
│       │       ├── d.py
│       │       └── e.py
│       └── test_project_python
│           ├── __init__.py
│           └── __main__.py
│           └── make_nested_py_modules.py
│           └── make_nested_py_modules_examples.py
├── dist
│   ├── test-project-python-0.0.2.post6.tar.gz
│   ├── test-project-python-0.0.2.post6.tar.gz.asc
│   └── test_project_python-0.0.2.post6-py3-none-any.whl
│   └── test_project_python-0.0.2.post6-py3-none-any.whl.asc
├── make_nested_py_modules.sh
├── package_a
│   ├── __init__.py
│   ├── module_a.py
│   ├── module_b.py
│   ├── module_c.py
│   ├── module_d.py
│   ├── module_e.py
│   ├── subpackage_a
│   │   ├── __init__.py    # this __init__.py module MUST exist for setuptools to *automatically* detect subpackage_a
│   │   ├── a.py
│   │   ├── b.py
│   │   ├── c.py
│   │   ├── d.py
│   │   └── e.py
│   ├── subpackage_b
│   │   ├── __init__.py    # this __init__.py module MUST exist for setuptools to *automatically* detect subpackage_b
│   │   ├── a.py
│   │   ├── b.py
│   │   ├── c.py
│   │   ├── d.py
│   │   └── e.py
│   └── subpackage_c
│       ├── __init__.py    # this __init__.py module MUST exist for setuptools to *automatically* detect subpackage_c
│       ├── a.py
│       ├── b.py
│       ├── c.py
│       ├── d.py
│       └── e.py
├── package_b
│   ├── __init__.py
│   ├── module_a.py
│   ├── module_b.py
│   ├── module_c.py
│   ├── module_d.py
│   ├── module_e.py
│   ├── subpackage_a
│   │   ├── __init__.py    # this __init__.py module MUST exist for setuptools to *automatically* detect subpackage_a
│   │   ├── a.py
│   │   ├── b.py
│   │   ├── c.py
│   │   ├── d.py
│   │   └── e.py
│   ├── subpackage_b
│   │   ├── __init__.py    # this __init__.py module MUST exist for setuptools to *automatically* detect subpackage_b
│   │   ├── a.py
│   │   ├── b.py
│   │   ├── c.py
│   │   ├── d.py
│   │   └── e.py
│   └── subpackage_c
│       ├── __init__.py    # this __init__.py module MUST exist for setuptools to *automatically* detect subpackage_c
│       ├── a.py
│       ├── b.py
│       ├── c.py
│       ├── d.py
│       └── e.py
├── package_c
│   ├── __init__.py
│   ├── module_a.py
│   ├── module_b.py
│   ├── module_c.py
│   ├── module_d.py
│   ├── module_e.py
│   ├── subpackage_a
│   │   ├── __init__.py    # this __init__.py module MUST exist for setuptools to *automatically* detect subpackage_a
│   │   ├── a.py
│   │   ├── b.py
│   │   ├── c.py
│   │   ├── d.py
│   │   └── e.py
│   ├── subpackage_b
│   │   ├── __init__.py    # this __init__.py module MUST exist for setuptools to *automatically* detect subpackage_b
│   │   ├── a.py
│   │   ├── b.py
│   │   ├── c.py
│   │   ├── d.py
│   │   └── e.py
│   └── subpackage_c
│       ├── __init__.py    # this __init__.py module MUST exist for setuptools to *automatically* detect subpackage_c
│       ├── a.py
│       ├── b.py
│       ├── c.py
│       ├── d.py
│       └── e.py
├── setup.py
└── test_project_python
│   ├── __init__.py
│   ├── __main__.py
│   ├── make_nested_py_modules.py
│   ├── make_nested_py_modules_examples.py
└── test_project_python.egg-info
    ├── PKG-INFO
    ├── SOURCES.txt
    ├── dependency_links.txt
    ├── entry_points.txt
    └── top_level.txt
```

## Examples

```
### install/upgrade the test_project_python package ###
python -m pip install --upgrade test_project_python



### run modules defined in the test_project_python package ###
python -m test_project_python.make_nested_py_modules
# now take a look at the directories and modules created by this command

python -m test_project_python.make_nested_py_modules_examples
# now take a look at the directories and modules created by this command



### run commands defined in entry_points['console_scripts'] located in the setup.py module ###
command_name
command_name_for_function_in__main__
```


## Version tag rules for a python package for distribution

The version tag (specified in the `version` argument to the `setuptools.setup` function in `setup.py`) must follow the rules outlined in [PEP 440 – Version Identification and Dependency Specification](https://peps.python.org/pep-0440/). Not doing so will result in an error such as the following (the following snippet used the `version` value of `0.0.2.update1` in the `setuptools.setup` function in `setup.py`):

```
$ twine upload --repository-url https://test.pypi.org/legacy/ dist/test_project_python-0.0.2.update1-py3-none-any.whl dist/test-project-python-0.0.2.update1.tar.gz dist/test-project-python-0.0.2.update1.tar.gz.asc dist/test_project_python-0.0.2.update1-py3-none-any.whl.asc
Uploading distributions to https://test.pypi.org/legacy/
Enter your username: username
Enter your password:
Uploading test_project_python-0.0.2.update1-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 49.2/49.2 kB • 00:00 • X.Y MB/s
WARNING  Error during upload. Retry with the --verbose option for more details.
ERROR    HTTPError: 400 Bad Request from https://test.pypi.org/legacy/
         '0.0.2.update1' is an invalid value for Version. Error: Start and end with a letter or numeral containing only ASCII numeric and '.', '_' and '-'. See https://packaging.python.org/specifications/core-metadata for more
         information.

### with the --verbose flag ###
$ twine upload --repository-url https://test.pypi.org/legacy/ dist/test_project_python-0.0.2.update1-py3-none-any.whl dist/test-project-python-0.0.2.update1.tar.gz dist/test-project-python-0.0.2.update1.tar.gz.asc dist/test_project_python-0.0.2.update1-py3-none-any.whl.asc --verbose
Uploading distributions to https://test.pypi.org/legacy/
INFO     dist/test_project_python-0.0.2.update1-py3-none-any.whl (22.1 KB)
INFO     Signed with dist/test_project_python-0.0.2.update1-py3-none-any.whl.asc
INFO     dist/test-project-python-0.0.2.update1.tar.gz (15.2 KB)
INFO     Signed with dist/test-project-python-0.0.2.update1.tar.gz.asc
INFO     Querying keyring for username
Enter your username: username
INFO     Querying keyring for password
Enter your password:
INFO     username: username
INFO     password: <hidden>
Uploading test_project_python-0.0.2.update1-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 49.2/49.2 kB • 00:00 • X.Y MB/s
INFO     Response from https://test.pypi.org/legacy/:
         400 '0.0.2.update1' is an invalid value for Version. Error: Start and end with a letter or numeral containing only ASCII numeric and '.', '_' and '-'. See https://packaging.python.org/specifications/core-metadata for more
         information.
INFO     <html>
          <head>
           <title>400 '0.0.2.update1' is an invalid value for Version. Error: Start and end with a letter or numeral containing only ASCII numeric and '.', '_' and '-'. See https://packaging.python.org/specifications/core-metadata for
         more information.</title>
          </head>
          <body>
           <h1>400 '0.0.2.update1' is an invalid value for Version. Error: Start and end with a letter or numeral containing only ASCII numeric and '.', '_' and '-'. See https://packaging.python.org/specifications/core-metadata for more
         information.</h1>
           The server could not comply with the request since it is either malformed or otherwise incorrect.<br/><br/>
         &#x27;0.0.2.update1&#x27; is an invalid value for Version. Error: Start and end with a letter or numeral containing only ASCII numeric and &#x27;.&#x27;, &#x27;_&#x27; and &#x27;-&#x27;. See
         https://packaging.python.org/specifications/core-metadata for more information.


          </body>
         </html>
ERROR    HTTPError: 400 Bad Request from https://test.pypi.org/legacy/
         '0.0.2.update1' is an invalid value for Version. Error: Start and end with a letter or numeral containing only ASCII numeric and '.', '_' and '-'. See https://packaging.python.org/specifications/core-metadata for more
         information.
```


## Building a python package for distribution

```
# update the package version to the new MAJOR.MINOR.PATCH everywhere in the project


# run the following commands from the root of your python project (and make sure your setup.py module is here)
#
# in the test_project_python project, this is from the
# /path/to/test-project/python directory (the setup.py module is here)


# https://stackoverflow.com/questions/34928001/distutils-ignores-changes-to-setup-py-when-building-an-extension
python setup.py clean --all                           # avoid using cached information
rm -r build/                                          # python setup.py clean --all **should** remove all contents of build/, but just in case
rm -r project_name.egg-info                           # **should** be updated automatically with both the setup.py and pip install command below, but just in case
rm -r package_* example_*                             # remove script generated packages (test_project_python specific, another projects will have a different cleaning process)
python -m test_project_python.make_nested_py_modules  # build script generated packages (test_project_python specific, another projects will have a different build process)
python setup.py sdist bdist_wheel                     # build packages for distribution
python -m pip install .                               # install the package locally
# run the sequence again (so run the 7 commands sequentially twice) just in case something somehow remains cached

:: Windows equivalent commands
:: NOTE: :: (double colons) is the Windows syntax for writing comments in CMD
python setup.py clean --all
rmdir /S /Q build/
rmdir /S /Q project_name.egg-info
for /d %G in ("package_*", "example_*") do rmdir /S /Q "%~dpnG"
python -m test_project_python.make_nested_py_modules
python setup.py sdist bdist_wheel
python -m pip install .
:: run the sequence again (so run the 7 commands sequentially twice) just in case something somehow remains cached


<#
PowerShell is very flexible and has multiple aliases for common commands, so
feel free to substitute a different alias if you have one that you prefer.
For example, you can use any of the aliases shown from the output of

> help Remove-Item

so instead of
> Remove-Item -recurse -path the_path_to_folder

you can do
> Remove-Item -recurse the_path_to_folder # equivalent
> ri    -r the_path_to_folder             # equivalent
> rm    -r the_path_to_folder             # equivalent
> rmdir -r the_path_to_folder             # equivalent
> del   -r the_path_to_folder             # equivalent
> erase -r the_path_to_folder             # equivalent
> rd    -r the_path_to_folder             # equivalent
#>
python setup.py clean --all
Remove-Item -recurse -path build/
Remove-Item -recurse -path project_name.egg-info
Remove-Item -recurse -path package_*             # notice that Remove-Item does NOT accept multiple
Remove-Item -recurse -path example_*             # arguments to Remove-Item (or any of its aliases)
python -m test_project_python.make_nested_py_modules
python setup.py sdist bdist_wheel
python -m pip install .
# run the sequence again (so run the 8 commands sequentially twice) just in case something somehow remains cached


# sign the package with your gpg key (optional)
# NOTE that your command may be `gpg2` instead of `gpg` (depends on how you installed this)
# also NOTE that the dashes or underscores in the dist/projectname.tar.gz is dependent on how
#      you named things in your setup.py module; specifically dependent on the `name` argument
#      you provide to the setuptools.setup function (if you use underscores for the `name` value, the
#          file will be dist/project_name.tar.gz, whereas if you use dashes for the `name` value, the
#          file will be dist/project-name.tar.gz)
gpg --detach-sign -a dist/project_name-MAJOR.MINOR.PATCH-py3-none-any.whl
gpg --detach-sign -a dist/project-name-MAJOR.MINOR.PATCH.tar.gz


### upload to PyPI ###
# upload to https://test.pypi.org/
twine upload --repository-url https://test.pypi.org/legacy/ dist/project_name-MAJOR.MINOR.PATCH-py3-none-any.whl dist/project_name-MAJOR.MINOR.PATCH-py3-none-any.whl.asc dist/project-name-MAJOR.MINOR.PATCH.tar.gz dist/project-name-MAJOR.MINOR.PATCH.tar.gz.asc

# upload to https://pypi.org/
twine upload dist/project_name-MAJOR.MINOR.PATCH-py3-none-any.whl dist/project_name-MAJOR.MINOR.PATCH-py3-none-any.whl.asc dist/project-name-MAJOR.MINOR.PATCH.tar.gz dist/project-name-MAJOR.MINOR.PATCH.tar.gz.asc

```


## Releases

See the [latest release](https://github.com/shailshouryya/test-project/releases/tag/0.0.2.post6-python) from the [releases page](https://github.com/shailshouryya/test-project/releases)
