def operator():
    num1 = input('enter number1:')
    num2 = input('enter number2:')

    print('select the operation 1 is for adition  2 is for subtraction')

    operation = input('enter opertaion:')
    if int(operation) == 1:
        ans = int(num1) + int(num2)
        print(ans)
    else:
        ans = int(num1) - int(num2)
        print(ans)


def type1():
    a = input('enter anything:')
    print(type(a))


def loop():
    a = ['hello', 'world', 'everyone']
    for i in a:
        if i == 2:
            print(i)
        else:
            print('nothing')


def fibonaci():
    a = int(input('enter number for series:'))
    n1, n2, count = 0, 1, 0
    if a < 0:
        print('wrong input')
    elif a == 1:
        print('1')
    else:
        while count < a:
            print(n1)
            res = n1 + n2
            n1 = n2
            n2 = res
            count += 1

fibonaci()
