# A program that outputs the sum of numbers

import numbers


def number_sum(lst):
    def get_numbers(l):
        for e in l:
            if isinstance(e, numbers.Number):
                yield e
            elif isinstance(e, (tuple, list)):
                yield from get_numbers(e)

    return sum(get_numbers(lst))


x1 = [1, 3, 5, 7, 9]

print(number_sum(x1))