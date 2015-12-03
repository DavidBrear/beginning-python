def search(sequence, number, lower=0, upper=None):
    if upper is None: upper = len(sequence)-1
    if lower == upper:
        assert number == sequence[upper], 'Number not found'
        return upper

    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle+1, upper)
        else:
            return search(sequence, number, lower, middle)


seq = list(set([34, 67, 8, 123, 4, 100, 95]))
print list(enumerate(seq))
print search(seq, 100)
