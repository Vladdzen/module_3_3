def print_params (a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
value_list = [1, 'два', False]
value_dict = {'a': 55, 'b': True, 'c': 'текст'}
print_params(*value_list)
print_params(**value_dict)
value_list2 = ['три', 4]
print_params(*value_list2, 42)