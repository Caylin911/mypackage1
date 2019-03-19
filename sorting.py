def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''

    length = len(items) - 1

    for i in range(length):

        for j in range(length - i):

            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]

    return items

def merge_sort(items):
    '''Return array of items, sorted in ascending order'''
    my_list = []
    if len(items) < 2:
        return items
    middle = int(len(items)/2)
    r = merge_sort(items[:middle])
    l = merge_sort(items[middle:])
    while (len(l)>0) and (len(r)>0):
        if l[0] > r[0]:
            my_list.append(r[0])
            r.pop(0)
        else:
            my_list.append(l[0])
            l.pop(0)
    return my_list+l+r

def quicksort(items):
    '''Return array of items, sorted in ascending order'''

    i = 0

    if len(items) > 1:
        begin = items[0]
        for j in range(len(items)-1):

            if items[j+1] < begin:
                items[j+1],items[i+1] = items[i+1], items[j+1]
                i += 1
        items[0],items[i] = items[i],items[0]
        l = quicksort(items[:i])
        r = quicksort(items[i+1:])
        l.append(items[i])
        return l + r
    else:
        return items
