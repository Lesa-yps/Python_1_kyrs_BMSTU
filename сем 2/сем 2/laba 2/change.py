import re

# Функция адаптирует функцию под язык программирования
def changer(strk):
    strk = strk.replace("^", "**")
    while (res := re.search("ln\d+.?\d*", strk)):
        res = res.group()
        res = res.replace(",", ".")
        strk = strk.replace(res, "log(" + res[2:] + ")")
    while (res := re.search("lg\d+.?\d*", strk)):
        res = res.group()
        res = res.replace(",", ".")
        strk = strk.replace(res, "log10(" + res[2:] + ")")
    strk = strk.replace("lgx", "log10(x)")
    strk = strk.replace("lnx", "log(x)")
    strk = strk.replace("lg", "log10")
    strk = strk.replace("ln", "log")
    strk = strk.replace("log", "m.log")
    return strk
