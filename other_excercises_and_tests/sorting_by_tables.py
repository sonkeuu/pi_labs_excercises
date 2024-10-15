from typing import List, Type

list_of_numbers: list[int] = [102, 504, 315, 3660, 827, 742, 331, 780, 963, 15, 2048]


def max_number_of_digits(list_of_numbers_to_sort: list[int]):

    letter = str(max(list_of_numbers_to_sort))
    #   print(letter)
    counted = len(letter)
    return counted

    #   for number in list_of_numbers:
    #   list_of_numbers.index(number)


def digits_number_equalize():
    digits_searched_number = max_number_of_digits(list_of_numbers)



if __name__ == '__main__':
    print(max_number_of_digits(list_of_numbers))

