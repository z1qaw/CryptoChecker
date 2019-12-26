import re


def separate_decimal_points(decimal):
    str_decimal = None

    if type(decimal) is float:
        str_decimal = str(decimal)
    
    if type(decimal) is str:
        str_decimal = decimal
    
    if not re.findall('\.', str_decimal):
        str_decimal += '.0000'

    integer_part = re.findall('\w+\.', str_decimal)[0][:-1]
    separated_integer = ''
    for decimal_counter, decimal in enumerate(integer_part[::-1]):
        separated_integer += decimal
        if (((decimal_counter + 1) % 3) == 0) and ((decimal_counter + 1) != len(integer_part)):
            separated_integer += ','
    return ''.join((separated_integer[::-1], str_decimal.replace(integer_part, '')))
    


def main():
    dec = '00000311234.3121'
    print(separate_decimal_points(dec))
    

if __name__ == '__main__':
    main()
