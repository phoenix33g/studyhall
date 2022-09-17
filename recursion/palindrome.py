def palindrome(string):
    # Base-case if it is a palindrome
    if len(string) <= 1:
        return True
    # Check the first and last chars, pass the remaining to recurseve
    if string[0].lower() == string[len(string)-1].lower():
        return palindrome(string[1:len(string)-1])
    # Base-case if all checks don't pass, it's a nope
    return False


input = "Kayyak"
print("Is " + input + " a palindrome?-> " + str(palindrome(input)))