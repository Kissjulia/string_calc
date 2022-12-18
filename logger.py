from datetime import datetime as dt
path = 'log.txt'
def logger(value_a, value_b, value_c, result):
    log = f'{dt.now()} | {value_a} {value_b} {value_c} = {result}\n'
    with open(path, 'a') as data:
        data.write(log)