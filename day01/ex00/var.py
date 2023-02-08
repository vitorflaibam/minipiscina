def my_var(fourty_two):
    print(fourty_two, "has a type", type(fourty_two)) 

if __name__ == '__main__':
    my_var(42)
    my_var("42")
    my_var("quarante-deux")
    my_var(42.0)
    my_var(True)
    my_var([42])
    my_var({42: 42})
    my_var((42,))
    my_var(set())
