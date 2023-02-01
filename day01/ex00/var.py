
def my_var(quatrodois):
    print(quatrodois, "has a type", type(quatrodois)) 

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
