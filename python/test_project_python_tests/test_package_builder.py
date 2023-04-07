from pprint import pprint
from typing import Any, Callable, Collection, List, Mapping, Optional, Tuple, TypeVar

from test_project_python.package_builder import (
    verify_instance_is_from_type,
)


InputArguments                         = Tuple[Any, ...]
Description                            = str
ExpectedResult                         = TypeVar('ExpectedResult')
ActualResult                           = TypeVar('ActualResult')


def main() -> None:
    test_function(data_verify_instance_is_from_type)


def test_function(function_data: Tuple[Callable, Collection[Tuple[InputArguments, Description, ExpectedResult]]]):
    function, test_cases = function_data
    successes           = 0
    failures            = 0
    test_case_results = []
    for input_arguments, description, expected_result in test_cases:
        actual_result = run_function(function, input_arguments)
        if actual_result != expected_result:
            failures += 1
        else:
            successes += 1
        test_case_results.append((input_arguments, description, expected_result, actual_result))
    print(f'{successes} test cases passed, {failures} test cases failed for the `verify_instance_is_from_type` function!')
    for test_case_result in test_case_results:
        print(format_test_case_result(function, test_case_result))
    return (successes, failures, test_case_results)


def run_function(function: Callable[..., Any], input_arguments: InputArguments) -> Any:
    try:
        result = function(*input_arguments)
    except Exception as error:
        result = type(error)
    finally:
        return result


def format_test_case_result(function: Callable[..., Any], test_case: Tuple[InputArguments, Description, ExpectedResult, ActualResult]) -> str:
    input_arguments, description, expected_result, actual_result = test_case
    formatted_match = '==' if expected_result == actual_result else '!='
    formatted_test_case_result = f'{description}: {function.__name__}{input_arguments} {formatted_match} {expected_result}'
    if expected_result != actual_result:
        formatted_test_case_result += f'\n❌ actaul_result={actual_result} ❌'
    return formatted_test_case_result


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
            ((obj, acceptable_type, variable_name), f'{variable_name:<9} input with `{str(acceptable_type):<17}` as only acceptable type', None)
            for obj, acceptable_type, variable_name in data_verify_instance_is_from_single_acceptable_type
        ),
        *(
            ((obj, acceptable_types, variable_name), f'{variable_name:<9} input with `{str(acceptable_types):<39}` as only acceptable types', None)
            for obj, acceptable_types, variable_name in data_verify_instance_is_from_one_of_multiple_acceptable_types
        ),

    )
]


if __name__ == '__main__':
    main()
