"""
Модуль os предоставляет множество функций для работы с операционной системой, причём их поведение, как правило,
не зависит от ОС, поэтому программы остаются переносимыми.

os.path является вложенным модулем в модуль os, и реализует некоторые полезные функции для работы с путями.
"""

import os

print(os.name)
print(os.environ)
print(os.getlogin())
print(os.getpid())
##print(os.uname())

# os.access(os.getcwd(), os.R_OK) - проверка доступа к объекту у текущего пользователя
# os.chdir() - смена текущей директории
# os.chmod() - смена прав доступа к объекту
# os.chown() - меняет id владельца и группы


print(os.getcwd())
print(os.listdir())

# os.mkdir('./test') - создаёт директорию
# os.remove('./') - удаляет путь к файлу
# os.rename('test', 'testing') - переименовывает файл или директорию
# os.rmdir('./') - удаляет пустую директорию

print(os.urandom(3))

print(os.path.abspath('./'))
print(os.path.basename('/Users/xqzme/Education/prog/exam/52'))
print(os.path.dirname('/Users/xqzme/Education/prog/exam/52'))
print(os.path.exists('/Users/xqzme/Education/prog/exam/54'))
