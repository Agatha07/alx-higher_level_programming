#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list[:]
    if (0 < idx) or (idx > (len(my_list)):
        copy[idx] = element
        return (copy)
    return (my_list)
