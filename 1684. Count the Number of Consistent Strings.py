from typing import List
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        alphabet ={
        'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104,
        'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112,
        'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120,
        'y': 121, 'z': 122
        }
        for c in allowed:
            if c in alphabet:
                del alphabet[c]
        output = 0
        for word in words:
            check_output = 0
            for c in word:
                if c in alphabet:
                    check_output=0
                    break
                else:
                    check_output =1
            output+=check_output
        return output
                    
        

        # Yes, that's correct. The del statement in Python is used to delete items from data structures like lists,     
        # dictionaries, sets, etc., but it cannot be used directly on strings. 