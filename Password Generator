import random

def randoms(length):
    lowercased = [chr(i) for i in range(97, 123)]
    uppercased = [chr(i) for i in range(65, 91)]
    numbers = [str(i) for i in range(10)]
    symbols = list("!@#$%^&*()-_=+[]{}|;:'\",.<>?/")
    all_char = lowercased + uppercased + numbers + symbols
    password = "".join(random.choices(all_char, k=length))
    return password

length = int(input("Enter the Length: "))
passed = randoms(length)
print("Generated password:", passed)
for i in range(100): 
    a = input("You need another one means type YES else NO: ").lower()
    if a in ["no"]:
        length = length
        passed = randoms(length)
        print("Generated password:", passed)
    if a in ["yes"]:
        print("Thank You")
        print("You can use this password:",passed)
        break
