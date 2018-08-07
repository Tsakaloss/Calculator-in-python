import sys
from lib import operations


# Manage the operations
def mathing_func(a, b, sign):
    if sign == '+':
        return operations.Calculations.plus(a, b)
    elif sign == '-':
        return operations.Calculations.minus(a, b)
    elif sign == '*':
        return operations.Calculations.multiply(a, b)
    elif sign == '/':
        return operations.Calculations.divine(a, b)
    else:
        print("Wrong sign detected.")
        sys.exit(1)


def calculator():
    try:
        while True:
            sign_position_counter = 0
            position_list_counter = 0
            numbers_listed = []
            signs_only = []
            counter = 1  # For the text to input third+ sign or = for result
            start_quit = input(
                'Type \'start\' to start using this calculator or type close to quit: ')
            if start_quit == 'close':
                break
            if start_quit == 'start':
                while True:
                    number_for_list = float(
                        input('Enter a number of your choice: '))
                    numbers_listed.insert(
                        position_list_counter, number_for_list)
                    position_list_counter += 1
                    if counter == 1:
                        sign_for_operation = input(
                            'Enter one of the following: + - * or /  : ')
                        signs_only.insert(sign_position_counter,
                                          sign_for_operation)
                        counter += 1
                        position_list_counter += 1
                        sign_position_counter += 1
                    else:
                        # Can later add it with '+' at the end of the string after one run
                        sign_for_operation = input(
                            'Enter one of the following: + - * / OR = to do the math  : ')
                        if sign_for_operation == '=':
                            amount = len(numbers_listed)
                            amount -= 1
                            for i in range(amount):
                                result = mathing_func(
                                    numbers_listed[i], numbers_listed[i + 1], signs_only[i])
                                numbers_listed.remove(numbers_listed[i + 1])
                                numbers_listed.insert(i + 1, result)
                            print("The result is: ", result)
                            break
                        else:
                            signs_only.insert(
                                sign_position_counter, sign_for_operation)
                            sign_position_counter += 1

    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)  # exits


if __name__ == '__main__':
    calculator()
