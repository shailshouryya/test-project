from pprint import pprint
from typing import Collection, List, Mapping, Optional, Tuple, TypeVar

from test_project_python.package_builder import (
    verify_instance_is_from_type,
)


TestCases                         = TypeVar('TestCases') 


def main():
    test_function(data_verify_instance_is_from_type)


def test_function(function_data):
    function, test_cases = function_data
    successes           = 0
    failures            = 0
    test_case_successes = []
    test_case_failures  = []
    for test_case, description in test_cases:
        try:
            verify_instance_is_from_type(*test_case)
        except TypeError as e:
            failures += 1
            test_case_failures.append((test_case, description))
        else:
            successes += 1
            test_case_successes.append((test_case, description))
    print(f'{successes} test cases passed, {failures} test cases failed for the `verify_instance_is_from_type` function!')
    print('Passing test cases:')
    pprint(test_case_successes)
    print('Failing test cases:')
    pprint(test_case_failures)
    return (successes, failures, test_case_successes, test_case_failures)



none_type  = type(None)
data_verify_instance_is_from_type = [
    verify_instance_is_from_type,
    (
        (('s',    str,                   'str_var'),      '`str` input with string as only acceptable type'),
        (('s',   (str, none_type),       'str_var'),      '`str` input with `str` and `None` as acceptable types'),
        ((1,      int,                    'int_var'),     '`int` input with `int` as only acceptable type'),
        ((1,     (int, none_type),        'int_var'),     '`int` input with `int` and `None` as acceptable types'),
        ((1.0,    float,                  'float_var'),   '`float` input with `float` as only acceptable type'),
        ((1.0,   (float, none_type),      'float_var'),   '`float` input with `float` and `None` as acceptable types'),
        (([],     Collection,             'list_var'),    '`list` input with `Collection` as only acceptable type'),
        (([],    (Collection, none_type), 'list_var'),    '`list` input with `Collection` and `None` as acceptable types'),
        (((),     Collection,             'tuple_var'),   '`tuple` input with `Collection` as only acceptable type'),
        (((),    (Collection, none_type), 'tuple_var'),   '`tuple` input with `Collection` and `None` as acceptable types'),
        (({},     Collection,             'dict_var'),    '`dict` input with `Collection` as only acceptable type'),
        (({},    (Collection, none_type), 'dict_var'),    '`dict` input with `Collection` and `None` as acceptable types'),
        ((set(),  Collection,             'set_var'),     '`set` input with `Collection` as only acceptable type'),
        ((set(), (Collection, none_type), 'set_var'),     '`set` input with `Collection` and `None` as acceptable types'),
        (('s',    Collection,             'str_var'),     '`str` input with `Collection` as only acceptable type'),
        (('s',   (Collection, none_type), 'str_var'),     '`str` input with `Collection` and `None` as acceptable types'),
        (({},     Mapping,                'dict_var'),    '`dict` input with `Mapping` as only acceptable type'),
        (({},    (Mapping, none_type) ,   'dict_var'),    '`dict` input with `Mapping` and `None` as acceptable types'),
    )
]


if __name__ == '__main__':
    main()
