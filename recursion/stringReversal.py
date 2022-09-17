def reverseString(string):
    # What's the base case?
    if len(string) <= 1:
        return string
    # What's the smallest amount of work I can do in each iteration?
    return reverseString(string[1:]) + string[0]

input = "This is a test.. racecar should read racecar!!!"
print(input + " reveresed is: " + reverseString(input))