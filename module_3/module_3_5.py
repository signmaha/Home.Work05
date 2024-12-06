def get_multipiled_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:

        return first * get_multipiled_digits(int(str_number[1:]))
    else:
        return first


print(get_multipiled_digits(40203))
print(get_multipiled_digits(402030))
