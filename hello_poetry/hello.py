NO_INPUT_MESSAGE = "No input"


def message():
    return "hello!"


def make_big_letter(input):
    if len(input) > 0:
        first_letter = input[0]
        capital = first_letter.capitalize()
        new_str = capital + input[1:]
        return new_str
    else:
        return NO_INPUT_MESSAGE


def rpn(input):
    first_operand = int(input[0])
    second_operand = int(input[2])
    operator = input[4]
    if operator == '+':
        return first_operand + second_operand
    elif operator == '*':
        return first_operand * second_operand
    else:
        return first_operand - second_operand
