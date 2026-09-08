# Palindrome Check: Check whether a string is a palindrome using recursion
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

text = input("Enter a string: ")
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a palindrome")
