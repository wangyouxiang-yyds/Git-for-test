
def function1(number):

    num = int(input(number))

    if num > 0:
        print(f"{num} is greater than 0")
    elif num < 0:
        print(f"{num} is smaller than 0")
    else:
        print(f"{num} is eqaul 0")

def add_sixty_nine(number):
    num = int(input(number))
    return num + 69


def this_function_will_cause_conflict():
    print("abcdefg")
    
def minus_seventy_eight(number):
    num = int(input(number))
    return num + 78

def for_loop(number):
    
    for i in number:
        for j in number:
            for k in number:
                print(i * j * k)