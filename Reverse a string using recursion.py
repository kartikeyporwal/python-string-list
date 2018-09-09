def rev_recur(string):
    if len(string) == 0:
        return string
    return rev_recur(string[1:]) + string[0]

print(rev_recur("hello"))
