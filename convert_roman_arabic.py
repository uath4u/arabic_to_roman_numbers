#!/usr/bin/env python
# -*- coding: utf-8 -*-

class NotInRangeError(Exception):
    """The error is raised, if number is not in Range between 1 to 3000
    :parameter
        int: number -- number which caused the error
    """

    def __init__(self, number):
        self.message = f"{number} is not in range between 1 and 3000"
        super().__init__(self.message)


def convert_arabic_to_roman_number(number=1):
    """Convert an arabic number into roman number

    :parameter
        int: number -- arabic number to convert into roman number

    :return
        str: roman_number -- converted roman number
    """

    # Set up necessary variables
    arabic_numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    number_sign = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_number = ""

    try:
        number = int(number)
        if 1 <= number <= 3000:
            # Transforming arabic number into roman number
            for i in arabic_numbers:
                while number >= i:
                    times = int(number / i)
                    for y in range(times):
                        roman_number = roman_number + number_sign[arabic_numbers.index(i)]
                    number = number - times * i
            return roman_number
        else:
            raise NotInRangeError(number)
    except ValueError as exc:
        raise exc


if __name__ == '__main__':

    print(convert_arabic_to_roman_number(1834))
