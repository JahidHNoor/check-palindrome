repeat = "y"
y = "y"
Y = "Y"
while repeat == y or repeat == Y:
    Data = input("Enter anything that you wanna check palindrome: ")
    check = Data [::-1]
    if check == Data:
        print("This is a palindrome.")
    else :
        print("This is not a palindrome")
    repeat = input("If you want to check again press y and hit enter: ")

