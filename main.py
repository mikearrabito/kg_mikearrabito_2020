import sys


def has_mapping(arg):
    s1 = arg[0]
    s2 = arg[1]
    if len(s1) != len(s2):
        return False

    map = {}
    i = 0

    for char in s1:
        if char in map and map[char] != s2[i]:
            """
            If we have used a char from s1 and mapped it already
            return false, since we are mapping the same character from s1 twice,
            except in the case of char we are mapped to appearing in s2 at current index
            (e.g.: s1= aba, s2=aca, when reaching last char, a is correctly mapped to a, so return true)
            """
            return False
        else:
            """
            Mapping char from s1 to s2, adding to list of used chars (from s1)
            """
            map[char] = s2[i]
            i += 1

    # print(map)
    return True


args = sys.argv[1:]

if len(args) != 2:
    print("Invalid input (please input 2 strings)")
    exit(-1)

print(has_mapping(args))
