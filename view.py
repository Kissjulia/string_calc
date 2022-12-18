def view_data(data, title):
    print(f'{title} = {data}')

def get_value():
    return int(input('value = '))


def input_str():
    expression = str(input('Введите в одну строку, что вы хотите посчитать'))
    compiled_str = compile(expression, 'string', 'eval')

    print(eval(compiled_str))