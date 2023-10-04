from dataclasses import dataclass

NO_INPUT_MESSAGE = "No input"


@dataclass
class Person:
    name: str
    surname: str
    yob: int

    def age(self):
        return 2023 - self.yob


def message():
    return "hello!"


def message_with_age(person):
    return f"Hello {person.name} {person.surname}, you are {person.age()} years old"


def make_big_letter(input):
    if len(input) > 0:
        first_letter = input[0]
        capital = first_letter.capitalize()
        new_str = capital + input[1:]
        return new_str
    else:
        return NO_INPUT_MESSAGE


@dataclass
class Operator:
    symbol: str

    def apply(self, first_operand, second_operand):
        if self.symbol == '+':
            return first_operand + second_operand
        elif self.symbol == '*':
            return first_operand * second_operand
        elif self.symbol == '/':
            return first_operand / second_operand
        else:
            return first_operand - second_operand


def rpn(input):
    first_operand = int(input[0])
    second_operand = int(input[2])
    symbol = input[4]
    operator = Operator(symbol)
    return operator.apply(first_operand, second_operand)


