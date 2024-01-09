import re

class Solution:
    def reverseWords(self, s: str) -> str:
        com = re.compile('\S+')
        s_list = com.findall(s)
        s_list.reverse()

        return ' '.join(s_list)