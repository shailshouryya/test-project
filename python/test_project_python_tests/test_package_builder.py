from pprint import pprint
from typing import Any, Callable, Collection, List, Mapping, Optional, Tuple, TypeVar

from test_project_python.package_builder import (
    verify_instance_is_from_type,
)


InputArguments                         = TypeVar('InputArguments') 


def main():
    test_function(data_verify_instance_is_from_type)


def test_function(function_data: Tuple[Callable, Tuple[InputArguments, str]]):
    function, test_cases = function_data
    successes           = 0
    failures            = 0
    test_case_successes = []
    test_case_failures  = []
    for input_arguments, description in test_cases:
        try:
            actual_result = run_function(function, input_arguments)
        except TypeError as e:
            failures += 1
            test_case_failures.append((input_arguments, description))
        else:
            successes += 1
            test_case_successes.append((input_arguments, description))
    print(f'{successes} test cases passed, {failures} test cases failed for the `verify_instance_is_from_type` function!')
    print('Passing test cases:')
    for test_case_success in test_case_successes:
        print(format_result(function, test_case_success))
    print('Failing test cases:')
    for test_case_failure in test_case_failures:
        print(format_result(function, test_case_failure))
    return (successes, failures, test_case_successes, test_case_failures)


def run_function(function: Callable, input_arguments: Tuple) -> Any:
    try:
        result = function(*input_arguments)
    except Exception as error:
        result = error
    finally:
        return result


def format_result(function, test_case):
    input_arguments, description = test_case
    return f'{description}: {function.__name__}{input_arguments}'

none_type  = type(None)
data_verify_instance_is_from_single_acceptable_type = [
    ('s',   str,        'str_val'),
    (1,     int,        'int_val'),
    (1.0,   float,      'float_val'),
    ([],    Collection, 'list_val'),
    ((),    Collection, 'tuple_val'),
    ({},    Collection, 'dict_val'),
    (set(), Collection, 'set_val'),
    ('s',   Collection, 'str_val'),
    ({},    Mapping,    'dict_val'),
]
data_verify_instance_is_from_one_of_multiple_acceptable_types = [
    ('s',   (str, none_type),       'str_var'),
    (1,     (int, none_type),        'int_var'),
    (1.0,   (float, none_type),      'float_var'),
    ([],    (Collection, none_type), 'list_var'),
    ((),    (Collection, none_type), 'tuple_var'),
    ({},    (Collection, none_type), 'dict_var'),
    (set(), (Collection, none_type), 'set_var'),
    ('s',   (Collection, none_type), 'str_var'),
    ({},    (Mapping, none_type) ,   'dict_var'),
]
data_verify_instance_is_from_type = [
    verify_instance_is_from_type,
    (
        *(
            ((obj, acceptable_type, variable_name), f'{variable_name:<9} input with `{str(acceptable_type):<17}` as only acceptable type')
            for obj, acceptable_type, variable_name in data_verify_instance_is_from_single_acceptable_type
        ),
        *(
            ((obj, acceptable_types, variable_name), f'{variable_name:<9} input with `{str(acceptable_types):<39}` as only acceptable types')
            for obj, acceptable_types, variable_name in data_verify_instance_is_from_one_of_multiple_acceptable_types
        ),

    )
]


if __name__ == '__main__':
    main()
