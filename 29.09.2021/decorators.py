def decorator_fun(func):
    def greet():
        print('-----------------------------------')
        func()
        print('------------------------------------')
    return greet

@decorator_fun
def print_name():
    print("Mohamed Yasin M")


@decorator_fun
def print_name1():
    print("Mohamed Yasin M")

# new_fun = decorator_fun(print_name)
# new_fun()

print_name()

print_name1()