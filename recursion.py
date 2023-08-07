def countdown(num):
    if num == 0:
        print("Kaboom")
    else:
        print(num)
        countdown(num - 1)

countdown(5)


def countdown2(num):
    for number in range(-num,1):
            print(-number)
    print("Kaboom")

countdown2(20)



def infinite_recursion(word):
    print(word)
    infinite_recursion(word)
infinite_recursion("Hi")