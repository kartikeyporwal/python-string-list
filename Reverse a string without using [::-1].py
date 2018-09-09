def rev(string):
    st = ""
    for i in string:
        st = i + st
    return st

print(rev("Hello"))

print(rev("Hello World"))

def rev_str(string):
    st = ""
    for i in range(len(string)-1, -1, -1):
        st += string[i]
    return st


print(rev_str("Python"))
