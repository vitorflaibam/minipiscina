with open("numbers.txt") as temp:
    numbers = temp.read().split(",")

def num(numeros):
    for number in numbers:
        print(number)

num(numbers)