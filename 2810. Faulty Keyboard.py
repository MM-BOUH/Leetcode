class Solution:
    # def reverseString(self, s: str) -> str:
    def finalString(self, s: str) -> str:
        i = 0
        while i < len(s):
            if s[i] == 'i':
                print(i)
                print(s[i-1::-1])
                s = s[i-1::-1] + s[i+1:]
            else:
                i+=1
        return s
######## s[i-1::-1]: This starts at index i-1 and goes backwards to the start of the string. The -1 specifies the step, which in this case is backward.