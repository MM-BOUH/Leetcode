class Solution:
    def toLowerCase(self, s: str) -> str:
        dictionary = {
            'A': 'a', 'B': 'b', 'C': 'c', 'D': 'd', 'E': 'e', 'F': 'f', 'G': 'g',
            'H': 'h', 'I': 'i', 'J': 'j', 'K': 'k', 'L': 'l', 'M': 'm', 'N': 'n',
            'O': 'o', 'P': 'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't', 'U': 'u',
            'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z'
            }
        # is: This is used for identity comparison. It checks whether two variables refer to the same object in memory. 
        # list1 = [1, 2, 3]
        # list2 = list1
        # list3 = [1, 2, 3]
        # print(list1 is list2)  # True, list1 and list2 refer to the same list
        # print(list1 is list3)  # False, list1 and list3 are different instances with the same content
        # in: This is used for membership testing. It checks if a value (an item) is a member of a collection, like a
        # list, tuple, dictionary, set, etc. 
        # my_list = [1, 2, 3]
        # my_dict = {'a': 1, 'b': 2, 'c': 3}

        # print(2 in my_list)     # True, because 2 is an item in my_list
        # print('b' in my_dict)   # True, because 'b' is a key in my_dict
        # print(1 in my_dict)     # False, 1 is not a key in my_dict (it's a value)

        lower_case_str = ""
        for c in s:
            print(c)
            if c in dictionary:
                c = dictionary[c]
                lower_case_str+=c
            else:
                lower_case_str+=c
        return lower_case_str
