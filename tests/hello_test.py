from assertpy import assert_that
from hello_poetry.hello import NO_INPUT_MESSAGE, make_big_letter, message, rpn


def test_message_should_return_hello():
    expected_value = "hello!"
    actual_value = message()
    assert_that(actual_value).is_equal_to(expected_value)


def test_capitalize_should_capitalize_the_first_letter_when_first_letter_small():
    input = 'marwan'
    expected = 'Marwan'
    actual = make_big_letter(input=input)
    assert_that(actual).is_equal_to(expected)


def test_capitalize_should_keep_capitalized_the_first_letter_when_first_letter_capital():
    input = 'Marwan'
    expected = 'Marwan'
    actual = make_big_letter(input=input)
    assert_that(actual).is_equal_to(expected)


def test_capitalize_should_do_x_when_input_is_empty():
    name = ''
    expected = NO_INPUT_MESSAGE
    actual = make_big_letter(input=name)
    assert_that(actual).is_equal_to(expected)


def test_rpn_should_return_sum_of_rpn_expression_with_two_single_digit_operands():
    input = '4 5 +'
    expected = 9
    actual = rpn(input)
    assert_that(actual).is_equal_to(expected)


def test_rpn_should_return_result_of_subtraction_with_two_single_digit_operands():
    input = '1 5 -'
    expected = -4
    actual = rpn(input)
    assert_that(actual).is_equal_to(expected)

def test_rpn_should_return_result_of_multiplication_with_two_single_digit_operands():
    input = '3 5 *'
    expected = 15
    actual = rpn(input)
    assert_that(actual).is_equal_to(expected)


# our calculartor should calculate RP notation expressions:
# examples:
#  1 2 + -> 3
#  1 2 3 + * -> 5
