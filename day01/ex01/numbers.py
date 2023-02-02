def num():
    with open("numbers.txt") as temp:
        numbers = temp.read().split(",")

    for number in numbers:
        print(number)
        
if __name__ == '__main__':
    num()
