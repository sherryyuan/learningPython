show_message = 2
print(show_message)


def Hello(name):
    # How to call global variables
    global show_message
    show_message = "Sherry"
    print('Hello ' + name)


# String related
Hello("SHERRY")
print(show_message)

word1 = "Hello"
word2 = "sherry"

word = word1 + word2
print(word)

word = word1 + " " + word2
print(word)

word = word.title()
print(word)

word = format(word, "^20")
print(word)

print(word.lstrip())

## number in Python
# 对于整数除法，我们只需要把其中一个数字换成浮点数，比如把 5 换成 5.0 这样计算的结果就能正确的表示出我们的计算结果。
number = 3.4444
number = round(number, 1)
print(number)
'''
This is a multiple line comment 
'''
