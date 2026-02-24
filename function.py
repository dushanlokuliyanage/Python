

def calTotal(price : int , quntity: int, discount):
    sub = quntity *  price
    disTotal = sub * (100 - discount) / 100
    return disTotal

total = calTotal(500 , 5, 20)
print(total)


a = 1
def f(x):
    b = 2
    return b + x

y = f(a)
print(y) 


def function():
    print("Hello")
    function()

function()

def fibonachi(n):
    if n == 0:
        return 0
    elif n == 1 :
        return 1
    else:
        return fibonachi(n - 1) + fibonachi ( n- 2)

result = fibonachi(5)
print(result)

# Local Scope - In simply u only can access in the function
def total(n1, n2):
    tot = n1 + n2
    return tot
result = total(10,20)
print(result)

