# Check Permutation: Given two strings,write a method to decide if one is a permutation of the
# other.

from collections import Counter

#Approach 1 : Sorting
#Time: O(nlogn)
def checkPermutation(s1, s2):
    return sorted(s1) == sorted(s2)


#Approach 2 :
#Time complexity : O(n)
def checkPermutation2(s1,s2):
    if len(s1) != len(s2):
        return False
    else:
        return Counter(s1) == Counter(s2)



def main():
    str_name1 = ""
    str_name2 =""

    while str_name1 != 'exit' and str_name2 != 'exit':
        str_name1 = raw_input()
        str_name2 = raw_input()
        print(checkPermutation2(str_name1,str_name2))


if __name__ == "__main__":
    main()