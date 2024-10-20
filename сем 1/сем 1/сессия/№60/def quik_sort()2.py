def quik_sort(x):
    if len(x) <= 1:
        return x
    king = x[0]
    left = [i for i in x if i < king]
    middle = [i for i in x if i == king]
    right = [i for i in x if i > king]
    return quik_sort(left) + middle + quik_sort(right)

print(quik_sort([32, 43, -43, 0, 34, 123, 34, 5, -5, 3]))
