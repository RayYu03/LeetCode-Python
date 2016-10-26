# Time:  O(n)
# Space: O(n)
#
# Given an absolute path for a file (Unix-style), simplify it.
#
# For example,
# path = "/home/", => "/home"
# path = "/a/./b/../../c/", => "/c"
# click to show corner cases.
#
# Corner Cases:
# Did you consider the case where path = "/../"?
# In this case, you should return "/".
# Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
# In this case, you should ignore redundant slashes and return "/home/foo".
#

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack, tokens = [], path.split('/')
        print tokens
        for token in tokens:
            if token == '..' and stack:
                stack.pop()
            elif token != '..' and token != '.' and token:
                stack.append(token)
        return '/' + '/'.join(stack)

if __name__ == "__main__":
    print Solution().simplifyPath("/../")
    print Solution().simplifyPath("/home//foo/")
