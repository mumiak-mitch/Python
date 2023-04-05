import numbers


def number_sqrt(lst):
    def get_numbers(l):
        for e in l:
            if isinstance(e, numbers.Number):
                yield e
            elif isinstance(e, (tuple, list)):
                yield from get_numbers(e)

    return sqrt(get_numbers(lst))


x1 = [1, 3, 5, 7, 9]
x2 = ["abc", [3, 5], 3.5, 2 + 3j, 4.5, 10]

print(number_sqrt(x1))
print(number_sqrt(x2))