def newton(a, b, eps, n_max, f):
    """Метод Ньютона (касательных)"""
    f_dx = lambda x: df_approx(f, x)

    f_a = f(a)
    f_b = f(b)

    # значения не разные знаки
    if cmp_float(0, f_a * f_b) > 0:
        return 0, -1

    # значение на границе 0
    if cmp_float(f_a * f_b, 0) == 0:

        return a if cmp_float(f_a, 0) == 0 else b, 0

    iter = 1

    # достигнут ли n_max при недостаточной точности
    flag = False

    while (abs(b - a) >= eps and iter <= n_max):
        # количество достигло максимального -> цикл прерывается
        if iter == n_max:
            flag = True
            break

        b, a = b - f(b) / f_dx(b), b

        iter += 1

    return b, iter, flag
