from typing import List, Type

list_of_numbers: list[int] = [102, 504, 315, 3660, 827, 742, 331, 780, 963, 15, 20489]
list_of_numbers_with_all_digits = []


def max_number_of_digits(list_of_numbers_to_sort: list[int]):
    letter = str(max(list_of_numbers_to_sort))
    #   print(letter)`
    counted = len(letter)
    return counted

    #   for number in list_of_numbers:
    #   list_of_numbers.index(number)


def digits_number_equalize():
    global list_of_numbers_with_all_digits
    digits_searched_value = max_number_of_digits(list_of_numbers)

    for number in list_of_numbers:
        if len(str(number)) < digits_searched_value:
            number_value = int(len(str(number)))
            sum_of_values = "0" * (digits_searched_value - number_value) + str(number)
            #   print(number)
            #   print(sum_of_values)

            list_of_numbers_with_all_digits.append(sum_of_values)
            #   print(*list_of_numbers_with_all_digits)

        elif len(str(number)) == digits_searched_value:
            value = str(number)

            list_of_numbers_with_all_digits.append(value)
            #   print(*list_of_numbers_with_all_digits

        else:
            return "Something went wrong."

    return print(*list_of_numbers_with_all_digits)


def first_table():
    list_of_0 = []
    list_of_1 = []
    list_of_2 = []
    list_of_3 = []
    list_of_4 = []
    list_of_5 = []
    list_of_6 = []
    list_of_7 = []
    list_of_8 = []
    list_of_9 = []

    for digit in list_of_numbers_with_all_digits:
        lengh = len(digit)
        last_index = ...
        print(lengh)


if __name__ == '__main__':
    print(max_number_of_digits(list_of_numbers))
    print(digits_number_equalize())
    print(first_table())
