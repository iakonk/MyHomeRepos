def is_palindrome(string):

    def to_chars(string):
        alphabet = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", 'p', "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
        ans = ''
        for c in string.lower():
            if c in alphabet:
                ans += c
        return ans

    def is_pal(string):
        if len(string) <= 1:
            return True
        else:
            return string[0] == string[-1] and is_palindrome(string[1:-1])

    return is_pal(to_chars(string))


print(is_palindrome('ablewasiereisawleba'))