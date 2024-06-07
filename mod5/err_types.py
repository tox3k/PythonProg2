from block_errors import BlockErrors

err_types = {ZeroDivisionError, TypeError}
with BlockErrors(err_types):
    a = 1 / 0
print('Выполнено без ошибок')

#Expected out:  Выполнено без ошибок

err_types = {ZeroDivisionError}
with BlockErrors(err_types):
    a = 1 / '0'
print('Выполнено без ошибок')

#Expected out:  TypeError: unsupported operand type(s) for /: 'int' and 'str'

outer_err_types = {TypeError}
with BlockErrors(outer_err_types):
    inner_err_types = {ZeroDivisionError}
    with BlockErrors(inner_err_types):
        a = 1 / '0'
    print('Внутренний блок: выполнено без ошибок')
print('Внешний блок: выполнено без ошибок')

#Expected out:  Внешний блок: выполнено без ошибок

err_types = {Exception}
with BlockErrors(err_types):
    a = 1 / '0'
print('Выполнено без ошибок')

#Expected out:  Выполнено без ошибок