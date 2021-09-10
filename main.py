# and b are two sorted list
def mergeLists(a,b):
    m = len(a)
    n = len(b)
    res = []
    i = 0
    j = 0
    # compare elements between two list till either gets complete
    while i < m and j < n:
        if a[i] <= b[j]:
            res.append(a[i])
            i = i + 1

        else:
            res.append(b[j])
            j = j + 1

    while i < m:
        res.append(a[i])
        i = i + 1

    while j < n:
        res.append(b[j])
        j = j + 1

    return res


if __name__ == '__main__':
    lsta = [10,15]
    lstb = [5,6,6,30,40]

    print(mergeLists(lsta, lstb))