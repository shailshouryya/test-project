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

The information included below covers building both an [import package](https://packaging.python.org/en/latest/glossary/#term-Import-Package) **and** a [distribution package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package).


## Requirements

This package uses [f-strings](https://cito.github.io/blog/f-strings/) ([learn more about f-strings here](https://realpython.com/python-f-strings/)), so this package requires Python version 3.6+ to run properly.

If you do not have Python installed, or have an older version of Python, you can download Python 3.11.2 (the latest stable version as of UTC 2023-03-18) from one of the links below and follow the instructions to set up Python for your machine. If you want to install a different version, visit the [Python Downloads page](https://www.python.org/downloads/) and select the version you want.
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


## Examples

NOTE that the following commands need to be run from your shell, and **not** your python interpreter!


### Installing or upgrading the `test_project_python` package
```text
python -m pip install --upgrade test_project_python
```


### Running modules defined in the `test_project_python` package

```text
python -m test_project_python.make_nested_py_modules
# now take a look at the directories and modules created by this command

python -m test_project_python.make_nested_py_modules_examples
# now take a look at the directories and modules created by this command
```


### Running commands defined in `entry_points['console_scripts']` located in the `setup.py` module

```text
command_name
command_name_for_function_in__main__
```


## Project Structure

The tree structure included below includes all the contents of the `test_project_python` project hosted in the GitHub repository. When you download the package using `python -m pip install --upgrade test_project_python`, you install **only** the contents included under the `build/lib` directory! **Usually**, this (the contents under the `build/lib` directory) is installed in

- the `/path/to/your/python_version/site-packages/` directory on Debian based Linux distributions
- the `/path/to/your/python/python_version/lib/python_version/site-packages/` directory on macOS
- the `C:\path\to\your\python_version\site-packages\` folder on Windows

The exact location may vary based on which Python installer you used, how you configured your Python installation, and which operating system you are using, so this might not be exactly correct for your package installation (but should be close). To find the exact location of the package installation, open up a Python interpreter and run

```python
import test_project_python

test_project_python.__file__
```


Note that some of the files below are configuration/build/binary files auto-generated by running commands to set up the package locally, and are NOT included in the GitHub repository:

- the ([no longer recommended](https://blog.ganssle.io/tag/setuptools.html#summary)) `python setup.py sdist` commands creates
  - `dist/test-project-python-0.0.2.post9.tar.gz`
  - `test_project_python.egg-info` (and nested contents)
  - use `python -m build` or `python -m build --no-isolation` command instead to use the [latest](https://packaging.python.org/en/latest/key_projects/#build) [build tools](https://packaging.python.org/en/latest/key_projects/#project-summaries)
- the ([no longer recommended](https://blog.ganssle.io/tag/setuptools.html#summary)) `python setup.py bdist_wheel` command creates
  - `build/bdist.OPERATINGSYSTEMNAME-moreoperatingsysteminfo`
  - `dist/test_project_python-0.0.2.post9-py3-none-any.whl`
  - `build/lib/`(and nested contents)
  - `test_project_python.egg-info` (and nested contents)
  - use `python -m build` or `python -m build --no-isolation` command instead to use the [latest](https://packaging.python.org/en/latest/key_projects/#build) [build tools](https://packaging.python.org/en/latest/key_projects/#project-summaries)
- the [`python -m build` command](https://packaging.python.org/en/latest/tutorials/packaging-projects/#generating-distribution-archives) creates
  - `dist/test-project-python-0.0.2.post9.tar.gz`
  - `dist/test_project_python-0.0.2.post9-py3-none-any.whl`
  - `test_project_python.egg-info` (and nested contents)
- the `python -m pip install .` command creates
  - `build/bdist.OPERATINGSYSTEMNAME-moreoperatingsysteminfo`
  - `build/lib/`(and nested contents)
  - `test_project_python.egg-info` (and nested contents)
- the `gpg --detach-sign -a dist/test-project-python-0.0.2.post9.tar.gz` command creates
  - `dist/test-project-python-0.0.2.post9.tar.gz.asc`
- the `gpg --detach-sign -a dist/test_project_python-0.0.2.post9-py3-none-any.whl` command creates
  - `dist/test_project_python-0.0.2.post9-py3-none-any.whl.asc`

Also note that running python files as modules locally creates a `__pycache__` directory and `.pyc` file nested inside the `__pycache__` directory (which were manually excluded from the structure below) for that corresponding module!

- note that this `.pyc` file creation inside the `__pycache__` directory
  - only happens when running `python3 -m path.to.module.name`
  - does NOT happen when running `python3 path/to/module/name.py`

(structure taken from the output of the `tree` command run from the `test-project/python` directory)

```text
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
│   ├── test-project-python-0.0.2.post9.tar.gz
│   ├── test-project-python-0.0.2.post9.tar.gz.asc
│   └── test_project_python-0.0.2.post9-py3-none-any.whl
│   └── test_project_python-0.0.2.post9-py3-none-any.whl.asc
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


## Development requirements

The following requirements are NOT required to run the `test_project_python` package locally (after installing with `python -m pip install --upgrade test_project_python`), but ARE required to follow along with the [Building a python package for distribution](#building-a-python-package-for-distribution) section below.

```text
python -m pip install --upgrade pip build twine
```

The download link below to GnuPG is NOT required for the [Building a python package for distribution](#building-a-python-package-for-distribution) section below, but will enable you to sign your package.
- https://gnupg.org/download/
- for more details about downloading, installing, and using `gpg` (and related tools), see the [GPG section](../README.md#gpg) under the [Programming language agnostic tools section](../README.md#programming-language-agnostic-tools) in the [main README in the GitHub repository](../README.md)


## Version tag rules for a python package for distribution

The version tag (specified in the `version` argument to the `setuptools.setup` function in `setup.py`) must follow the rules outlined in [PEP 440 – Version Identification and Dependency Specification](https://peps.python.org/pep-0440/). Not doing so will result in an error such as the following (the following snippet used the `version` value of `0.0.2.update1` in the `setuptools.setup` function in `setup.py`):

```text
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

NOTE that Python's versioning rules outlined in [PEP 440](https://peps.python.org/pep-0440/) are different and impose more restrictions than both `git` and GitHub do.

- for more details about versioning rules and guidelines for `git` and GitHub, see the [Version tag rules section](../README.md#version-tag-rules) under the [General Guidelines section](../README.md#general-guidelines) in the [main README in the GitHub repository](../README.md)

Also note that Python build tools (such as `setuptools` and `build`) normalize valid semantic version tags to follow a `#.#.#.suffix#` format, so you'll see a message such as the following when building your package with a command like `python -m build` or `python -m build --no-isolation` if your tag **does follow valid semantic versioning** rules, but does not follow the `#.#.#.suffix#` format (NOTE that this does not apply if your tag format is only `#.#.#` and does not have a suffix):

```text
# valid semantic version tag and no normalization required:
# version='0.0.2-post-8' in `setup` function in setup.py  # no UserWarning message



# all of the following tags use a valid semantic version tag, but require normalization:

# uses a . (dot) or _ (underscore) after the #.#.# part
UserWarning: Normalizing '0.0.2-post-8' to '0.0.2.post8'  # version='0.0.2-post-8' in `setup` function in setup.py
UserWarning: Normalizing '0.0.2.post-8' to '0.0.2.post8'  # version='0.0.2.post-8' in `setup` function in setup.py
UserWarning: Normalizing '0.0.2-post.8' to '0.0.2.post8'  # version='0.0.2-post.8' in `setup` function in setup.py
UserWarning: Normalizing '0.0.2_post_8' to '0.0.2.post8'  # version='0.0.2_post_8' in `setup` function in setup.py
UserWarning: Normalizing '0.0.2.post_8' to '0.0.2.post8'  # version='0.0.2.post_8' in `setup` function in setup.py
UserWarning: Normalizing '0.0.2_post.8' to '0.0.2.post8'  # version='0.0.2_post.8' in `setup` function in setup.py
UserWarning: Normalizing '0.0.2_post-8' to '0.0.2.post8'  # version='0.0.2_post-8' in `setup` function in setup.py
UserWarning: Normalizing '0.0.2-post_8' to '0.0.2.post8'  # version='0.0.2-post_8' in `setup` function in setup.py

# no . (dot) after the #.#.# part:
UserWarning: Normalizing '0.0.2post-8' to '0.0.2.post8'   # version='0.0.2post-8' in `setup` function in setup.py
UserWarning: Normalizing '0.0.2post-8' to '0.0.2.post8'   # version='0.0.2post-8' in `setup` function in setup.py
UserWarning: Normalizing '0.0.2post.8' to '0.0.2.post8'   # version='0.0.2post.8' in `setup` function in setup.py
UserWarning: Normalizing '0.0.2post_8' to '0.0.2.post8'   # version='0.0.2post_8' in `setup` function in setup.py
UserWarning: Normalizing '0.0.2post_8' to '0.0.2.post8'   # version='0.0.2post_8' in `setup` function in setup.py
UserWarning: Normalizing '0.0.2post.8' to '0.0.2.post8'   # version='0.0.2post.8' in `setup` function in setup.py
UserWarning: Normalizing '0.0.2post-8' to '0.0.2.post8'   # version='0.0.2post-8' in `setup` function in setup.py
UserWarning: Normalizing '0.0.2post_8' to '0.0.2.post8'   # version='0.0.2post_8' in `setup` function in setup.py
UserWarning: Normalizing '0.0.2post.8' to '0.0.2.post8'   # version='0.0.2post.8' in `setup` function in setup.py

# no . (dot) before the suffix:
UserWarning: Normalizing '0.0.2post8' to '0.0.2.post8'    # version='0.0.2post8'   in `setup` function in setup.py

# . (dot) after the suffix:
UserWarning: Normalizing '0.0.2.post.8' to '0.0.2.post8'  # version='0.0.2.post.8' in `setup` function in setup.py
```


## Naming conventions

A guide on building a Python project would be incomplete without including any of the two hardest things in computer science: naming things, cache invalidation, and off-by-one errors. There are many conventions for naming things in your project, and picking something that satisfies all the different conventions is (probably) impossible. You should try to pick something that is easily understandable and intuitive to other people, since your project will (eventually) be read/used by other people. This project uses the principles outlined in [Robert Martin](https://blog.cleancoder.com/)'s [A Handbook of Agile Software Craftsmanship](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882) book (see a [quick summary here](https://thecoderoad.blog/2020/03/29/clean-code-naming-conventions/). A quick overview:

- variables, arguments/parameters, and constants use a noun or noun phrase for the name (this would also apply to classes, but this project does not (currently) use any classes)
- functions use a verb or verb phrase (you'll typically see this described as "methods" - but since this project does not (currently) use any classes, there are only functions and no methods)
  - [A Grammar-Based Naming Convention](https://dev.to/somedood/a-grammar-based-naming-convention-13jf#functions) suggests naming functions using a combination of two parts: a transitive verb and a direct object
    - "In other words, the names for functions are usually in the form of `verb + noun`. This communicates to us that the name is a command, or rather a function, that we can call whenever we want."
  - some simple examples without [going too deep into English grammar](https://english.stackexchange.com/questions/218157/adjectives-versus-noun-adjuncts) (not all of these examples are actual functions in the project):
    - `{verb or verb_phrase}_{noun or noun_phrase}` such as `create_subpackage`
    - `{word or word_phrase describing}_{verb or verb_phrase}_{noun or noun_phrase}` such as `quickly_create_subpackage`
    - `{verb or verb_phrase}_{word or word_phrase describing}_{noun or noun_phrase}` such as `create_important_subpackage`
    - `{verb or verb_phrase}_{noun or noun_phrase}_{extended description}` such as `create_subpackage_later` or `create_modules_for_subpackage`
- modules use a noun or noun phrase
  - this does not seem to be explicitly outlined, but since modules are semantically more like classes than they are like functions/methods, modules use this naming convention in this project
- packages use a noun or noun phrase
  - this also does not seem to be explicitly outlined, but a package is a group of modules, and modules use a noun or noun phrase as their name, so the package also uses this as the naming convention in this project
    - **technically**, `test_project_python` can be a `{verb}_{noun_phrase}` as well since `test` is also a verb
      - however, the `test` is intended to be an adjective describing the `project_python` in this context
        - this is a `test` project in Python that outlines how to do things
        - as opposed to a `production` project in Python that does something important
- NOTE that Python does not have a ["true" `private` access modifier](https://en.wikipedia.org/wiki/Access_modifiers#Names_of_keywords) that is enforced by the Python language, but does have [class name mangling](https://docs.python.org/3/reference/expressions.html#atom-identifiers)

<details>
<summary><strong>More references for naming conventions</strong></summary>

This is mentioned in some of the links below as well, but placing here for quick reference: Python modules and packages need to be `import`able, and Python does not allow hyphens to be used in an `import` path. This means you need to name all your modules (files ending in `.py`) and packages (folders containing Python modules) **without** any hyphens! Having underscores in the module name or package name are okay, though.

- [Best practices for naming python utils / extending core modules?](https://softwareengineering.stackexchange.com/questions/438589/best-practices-for-naming-python-utils-extending-core-modules)
- [Python Same Module Name Convention](https://stackoverflow.com/questions/44221225/python-same-module-name-convention)
- [Naming convention and structure for utility classes and methods](https://stackoverflow.com/questions/1271254/naming-convention-and-structure-for-utility-classes-and-methods)
- [Folder naming convention for python projects](https://stackoverflow.com/questions/52827722/folder-naming-convention-for-python-projects)
- [Python naming conventions for modules in subpackages](https://stackoverflow.com/questions/60057775/python-naming-conventions-for-modules-in-subpackages)
- [Semantically more appropriate package name than `util` for the following things?](https://softwareengineering.stackexchange.com/questions/284799/semantically-more-appropriate-package-name-than-util-for-the-following-things)
- [Python file naming convention?](https://softwareengineering.stackexchange.com/questions/308972/python-file-naming-convention)
  - Python files are referred to as "modules", so refer to the "Module Naming" section here [Python Naming Convention](https://github.com/naming-convention/naming-convention-guides/tree/master/python)
- [How to choose proper variable names for long names in python](https://stackoverflow.com/questions/48721582/how-to-choose-proper-variable-names-for-long-names-in-python/48721872#48721872)
- [Naming](https://google.github.io/styleguide/pyguide.html#s3.16-naming) section of the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [PEP 423 – Naming conventions and recipes related to packaging](https://peps.python.org/pep-0423/)
- [Stop naming your python modules "utils"](https://www.reddit.com/r/Python/comments/g1dxfn/stop_naming_your_python_modules_utils/)
- [Util Packages Are Evil](https://www.adam-bien.com/roller/abien/entry/util_packages_are_evil)
- [Anti-Patterns and Worst Practices – Utils Class](https://lostechies.com/chrismissal/2009/06/01/anti-patterns-and-worst-practices-utils-class/)
- [Clean code tips - names and functions](https://www.code4it.dev/blog/clean-code-names-and-functions)
- [Clean Code - Naming](https://dipta007.com/clean-code-naming/)
- [Use prepositions in naming verb-phrase functions?](https://softwareengineering.stackexchange.com/questions/404135/use-prepositions-in-naming-verb-phrase-functions)
- [Use verbs with functions, nouns with classes - what about interfaces? [closed]](https://softwareengineering.stackexchange.com/questions/156824/use-verbs-with-functions-nouns-with-classes-what-about-interfaces)
- [Chapter 1. Naming Conventions](https://www.oreilly.com/library/view/java-pocket-guide/9781491938683/ch01.html) (from [Java Pocket Guide, 4th Edition](https://www.oreilly.com/library/view/java-pocket-guide/9781491938683/)
- [Noun-classes and verb-classes](https://medium.com/@wladislavk/noun-classes-and-verb-classes-b39eebb5c942)
- [Do I ought to follow naming conventions for Java packages?](https://stackoverflow.com/questions/38635340/do-i-ought-to-follow-naming-conventions-for-java-packages) (about Java, but useful discussion)
- [A Grammar-Based Naming Convention](https://dev.to/somedood/a-grammar-based-naming-convention-13jf)
- [interesting discussion in comments here](https://dev.to/somedood/a-grammar-based-naming-convention-13jf?comments_sort=oldest#toggle-comments-sort-dropdown)
- [Python package name conventions](https://stackoverflow.com/questions/2713874/python-package-name-conventions)
- [Use a single name](https://peps.python.org/pep-0423/#use-a-single-name)

</details>


## Building a python package for distribution

To build a Python package for distribution for other people, update your package version to the new `MAJOR.MINOR.PATCH` version (or `MAJOR.MINOR.PATCH.suffix` or `MAJOR.MINOR.PATCH.suffix#`) everywhere in the project. Then, run the following commands from the root of your python project (and make sure your `setup.py` module is here) using the commands for the operating system and shell you are using. In the `test_project_python` project, this is from the `/path/to/test-project/python` directory (which is where the `setup.py` module is located).


### Preparing the package for distribution


#### Unix terminals such as bash, sh, zsh, ...

```bash
# https://stackoverflow.com/questions/34928001/distutils-ignores-changes-to-setup-py-when-building-an-extension

python setup.py clean --all                           # avoid using cached information
rm -r build                                           # python setup.py clean --all **should** remove all contents of build/, but just in case
rm -r project_name.egg-info                           # **should** be updated automatically with both the setup.py and pip install command below, but just in case
rm -r package_* example_*                             # remove script generated packages (test_project_python specific, another project will have a different cleaning process)
python -m test_project_python.make_nested_py_modules  # build script generated packages (test_project_python specific, another project will have a different build process)
python -m build                                       # build packages for distribution (add --no-isolation to avoid virtual environment requirement)
python -m pip install .                               # install the package locally

# run the sequence again (so run the 7 commands sequentially twice) just in case something somehow remains cached
```


#### Windows Command Line (also referred to as CMD, .bat, .cmd, batch script)

```bat
:: NOTE: :: (double colons) is the Windows syntax for writing comments in CMD

python setup.py clean --all                                      &:: avoid using cached information
rmdir /S /Q build                                                &:: python setup.py clean --all **should** remove all contents of build/, but just in case
rmdir /S /Q project_name.egg-info                                &:: **should** be updated automatically with both the setup.py and pip install command below, but just in case
for /d %G in ("package_*", "example_*") do rmdir /S /Q "%~dpnG"  &:: remove script generated packages (test_project_python specific, another project will have a different cleaning process)
python -m test_project_python.make_nested_py_modules             &:: build script generated packages (test_project_python specific, another project will have a different build process)
python -m build                                                  &:: build packages for distribution (add --no-isolation to avoid virtual environment requirement)
python -m pip install .                                          &:: install the package locally

:: run the sequence again (so run the 7 commands sequentially twice) just in case something somehow remains cached
```


#### PowerShell

```powershell
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

NOTE that Remove-Item does NOT accept multiple
arguments to Remove-Item (and the aliases also do not accept multiple arguments)
#>

python setup.py clean --all                            # avoid using cached information
Remove-Item -recurse -path build                       # python setup.py clean --all **should** remove all contents of build/, but just in case
Remove-Item -recurse -path project_name.egg-info       # **should** be updated automatically with both the setup.py and pip install command below, but just in case
Remove-Item -recurse -path package_*                   # remove script generated packages (test_project_python specific, another project will have a different cleaning process)
Remove-Item -recurse -path example_*                   # remove script generated packages (test_project_python specific, another project will have a different cleaning process)
python -m test_project_python.make_nested_py_modules   # build script generated packages (test_project_python specific, another project will have a different build process)
python -m build                                        # build packages for distribution (add --no-isolation to avoid virtual environment requirement)
python -m pip install .                                # install the package locally

# run the sequence again (so run the 8 commands sequentially twice) just in case something somehow remains cached
```


### Signing the package with GPG (optional)

- NOTE that your command may be `gpg2` instead of `gpg` (depends on how you installed this)
- also NOTE that the dashes or underscores in the `dist/projectname.tar.gz` is dependent on how you named things in your `setup.py` module
  - more specifically, the file name depends on the `name` argument provided to the `setuptools.setup` function
    - if you use underscores for the `name` value, the file will be `dist/project_name-MAJOR.MINOR.PATCH.tar.gz` (or `dist/project_name-MAJOR.MINOR.PATCH.suffix.tar.gz` or `dist/project_name-MAJOR.MINOR.PATCH.suffix.tar.gz`)
    - if you use dashes for the `name` value, the file will be `dist/project-name-MAJOR.MINOR.PATCH.tar.gz` (or `dist/project-name-MAJOR.MINOR.PATCH.suffix.tar.gz` or `dist/project-name-MAJOR.MINOR.PATCH.suffix#.tar.gz`)

NOTE that the following commands need to be run from your shell, and **not** your python interpreter!

```text
gpg --detach-sign -a dist/project_name-MAJOR.MINOR.PATCH-py3-none-any.whl
gpg --detach-sign -a dist/project-name-MAJOR.MINOR.PATCH.tar.gz
```


### Uploading the package to the hosting index

Uploading a package to a Python packaging index using a tool such as [`twine`](https://twine.readthedocs.io/en/stable/) requires having an account on the corresponding index. In other words, to upload to

- the [Test PyPI](https://test.pypi.org) index, you need to [make an account there](https://test.pypi.org/account/register/) if you do not already have one
- the [PyPI](https://pypi.org) index, you need to [make an account there](https://pypi.org/account/register/) if you do not already have one
- a private index, you need to have an account with the hosting organization and sufficient privileges to publish packages
  - the exact details will vary, so ask the index maintainers/administrators what is required for the process of uploading and maintaining Python packages on your private index
- a self-hosted index such as [pypiserver](https://github.com/pypiserver/pypiserver/blob/master/README.rst), you need to follow whatever steps the person/organization maintaining the hosted service has established 🙂

Also NOTE that if you want to upload **all** packages to an index, you can specify `dist/*` instead of individually listing each package you want to upload as the examples do below. Keep in mind that you cannot overwrite already existing versions of a package on Test PyPI and PyPI (which is **probably** true for a private index and self-hosted index as well).

NOTE that the following commands need to be run from your shell, and **not** your python interpreter!

#### Uploading the new package to https://test.pypi.org/

```text
twine upload --repository-url https://test.pypi.org/legacy/ dist/project_name-MAJOR.MINOR.PATCH-py3-none-any.whl dist/project_name-MAJOR.MINOR.PATCH-py3-none-any.whl.asc dist/project-name-MAJOR.MINOR.PATCH.tar.gz dist/project-name-MAJOR.MINOR.PATCH.tar.gz.asc
```


#### Uploading the new package to https://pypi.org/

- does **not** require specifying the `--repository-url`

```text
twine upload dist/project_name-MAJOR.MINOR.PATCH-py3-none-any.whl dist/project_name-MAJOR.MINOR.PATCH-py3-none-any.whl.asc dist/project-name-MAJOR.MINOR.PATCH.tar.gz dist/project-name-MAJOR.MINOR.PATCH.tar.gz.asc
```

NOTE: Uploading to Test PyPI or PyPI [do not require registering your package](https://packaging.python.org/en/latest/guides/migrating-to-pypi-org/#registering-package-names-metadata) using the `setup.py register` (deprecated) command or the [`twine register`](https://twine.readthedocs.io/en/stable/#twine-register) command, but a private or a self-hosted index (such as [pypiserver](https://github.com/pypiserver/pypiserver/blob/master/README.rst#upload-with-twine)] may require some form of registration. Contact the maintainer/administrator of the index for more information. For historical information, read the [Support for legacy register API](https://github.com/pypi/warehouse/issues/1627) thread.

To see some suggested best practices associated with distributing Python packages on PyPI, read [Sharing Your Labor of Love: PyPI Quick and Dirty](https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/) by [Hynek Schlawack](https://hynek.me/articles/sharing-your-labor-of-love-pypi-quick-and-dirty/). This article has lots of useful advice, and indicates invoking `python setup.py sdist` and `python setup.py sdist bdist_wheel` is no longer recommended (see the linked [Why you shouldn't invoke setup.py directly](https://blog.ganssle.io/articles/2021/10/setup-py-deprecated.html) article for more information). Instead, you should use [`python -m build`](https://pypa-build.readthedocs.io/en/stable/index.html).


## Releases

See the [latest release](https://github.com/shailshouryya/test-project/releases/tag/0.0.2.post9-python) from the [releases page](https://github.com/shailshouryya/test-project/releases)
