try:
    a = int(input())
    if a > 0:
        raise Exception('число > 0: ошибка')
    elif a == 0:
        raise ValueError
except ValueError:
    print('value_error')
except Exception as e:
    print(e)
else:
    print('all is Ok')
finally:
    print('^_^')
