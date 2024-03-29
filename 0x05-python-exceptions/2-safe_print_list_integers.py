#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for j in range(x):
        try:
            print("{:d}".format(my_list[j]), end="")
            i += 1
        except(ValueError, TypeError):
            continue
    print()
    return i

# Test cases
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print:", nb_print)

    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, len(my_list))
    print("nb_print:", nb_print)

    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
    print("nb_print:", nb_print)
