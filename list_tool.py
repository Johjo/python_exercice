def create_list():
    return [1, 2, 3, 4, 50]

def append(l, value):
    l.append(value)


def contain(l, value):
    return value in l


def delete(l, index):
    del l[index]


def insert(l, index, value):
    l.insert(index, value)


def pop(l, index):
    return l.pop(index)


def extend(l1, l2):
    l1.extend(l2)
    return l1