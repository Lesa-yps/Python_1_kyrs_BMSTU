answers = []


def date_to_seconds(date):
    components = date.split(':')
    for component in components:
        if not (component.isdecimal() and len(component) == 2):
            return None
    if int(components[0]) > 23 or int(components[1]) > 59 or int(components[2]) > 59:
        return None
    if len(components) != 3:
        return None
    return int(components[0]) * 60 * 60 + int(components[1]) * 60 + int(components[2])


for x1 in range(int(input())):
    day = [0] * (60 * 60 * 24)
    correct = True
    for x2 in range(int(input())):
        left, right = map(date_to_seconds, input().split('-'))
        if left is None or right is None:
            correct = False
            continue
        if left > right:
            correct = False
        for x in range(left, right + 1):
            day[x] += 1
            if day[x] > 1:
                correct = False
    answers.append(['NO', 'YES'][correct])
print('\n'.join(answers))
