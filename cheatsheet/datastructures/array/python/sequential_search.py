array = ['asdf', 'qwer', 'wert', 'bbkim', 'erty']
target = 'bbkim'

def sequential_search(array, target):
    for idx, each in enumerate(array):
        if each == target:
            return idx

    return -1


pos = sequential_search(array, target)
print('target {}\'s index: {}'.format(target, pos))
print('target {}\'s index: {}'.format(target, array.index(target)))


target = 'bhui'
pos = sequential_search(array, target)
print('target {}\'s index: {}'.format(target, pos))
print('target {}\'s index: {}'.format(target, array.index(target)))