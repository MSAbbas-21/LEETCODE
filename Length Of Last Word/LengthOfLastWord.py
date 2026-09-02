class Solution(object):
    def length(self, s):
        word = s.split()
        return len(word[-1])