def join(any_list, join_by):
    string_after_join = ""

    for i in any_list:
        if string_after_join == "":
            string_after_join += str(i)
        else:
            string_after_join = string_after_join + join_by + str(i)
            
    return string_after_join

print(join([x for x in range(11)], " "))

print(join([x for x in range(11)], "-"))
