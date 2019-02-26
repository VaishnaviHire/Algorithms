
# Is Unique: Implement an algorithm to determine if a string has all unique characters.
#  What if you cannot use additional data structures?

def verifyUnique(string):
    visited_letters = {}

    for i in string:
        if i in visited_letters:
            return False
        else:
            visited_letters[i] = True
    return True


def main():
    str_name = ""
    while str_name != 'exit':
        str_name = raw_input()
        print(verifyUnique(str_name))


if __name__ == "__main__":
    main()

#Time : O(n)
#Space : O(1)
