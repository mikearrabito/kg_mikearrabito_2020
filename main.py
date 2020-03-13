import sys

args = sys.argv[1:]

if len(args) == 0 or len(args) > 2:
    print("Invalid input (input 2 strings)")
    exit(-1)


def has_mapping(str):

    return True


print(has_mapping(args[2:3]))
