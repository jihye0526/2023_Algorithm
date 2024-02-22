class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        currStr, currNum = '', 0

        for c in s:
            if c == '[':
                st.append(currStr)
                st.append(currNum)
                currStr = ''
                currNum = 0
            elif c == ']':
                prevNum = st.pop()
                prevStr = st.pop()
                currStr = prevStr + currStr * prevNum
            elif c.isdigit():
                currNum = currNum * 10 + int(c)
            else:
                currStr += c
                
        return currStr
        