from math import * 

def f(x):
    fun = "sin(3 * x) + cos(5 * x)"
    return eval(fun)

def diff(x):
    fun = "3 * cos(3 * x) - 5 * sin(5 * x)"
    return eval(fun)

def diff_2(x):
    fun = "- 9 * sin(3 * x) - 25 * cos(5 * x)"
    return eval(fun)
