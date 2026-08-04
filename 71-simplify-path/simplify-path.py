class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        # Split path by '/' which automatically handles consecutive slashes
        parts = path.split('/')
        
        for part in parts:
            # Ignore empty strings (from multiple slashes) and current directory '.'
            if not part or part == '.':
                continue
            # Go up to the parent directory if possible
            elif part == '..':
                if stack:
                    stack.pop()
            # Valid directory or file name (including '...', '....', etc.)
            else:
                stack.append(part)
                
        # Join directories with a single '/' starting with '/'
        return '/' + '/'.join(stack)