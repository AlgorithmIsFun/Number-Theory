def primes(num):
    lst = []
    if num < -1:
        num = -num
        lst.append(-1)
    while num > 1:
        i = 1
        bol = True
        while bol:
            i += 1
            if num % i == 0:
                bol = False
        num = num // i
        lst.append(i)
    return lst

def FTA(num):
    lst = []
    while True:
        if num % 2 == 0:
            lst.append(2)
            num = num // 2
        else:
            lst.append(num)
            break
    if 1 in lst:
        lst.remove(1)
    return lst

def GCD(num1, num2):
    lst1 = primes(num1)
    lst2 = primes(num2)
    num = 1
    for i in lst1:
        if i in lst2:
            num *= i
            lst2.remove(i)
    return num

def GCD2(num1, num2):
    a = num1
    b = num2
    while True:
        rem = division(a, b)
        if rem == 0:
            break
        b = a
        a = rem
    return a

def division(a, b):
    quot = b // a
    return b - (quot * a)

def perfect(num):
    lst = primes(num)
    summ = 0
    for i in lst:
        summ += i
    summ += 1
    return num == summ

def LCM(a, b):
    total = a * b
    gcd = GCD(a, b)
    return total // gcd

def politeness(start, num):
    summ = 0
    while start < num:
        summ += start
        start += 1
        if num < summ:
            return False
        elif num == summ:
            return True
def num_of_polite(num):
    num2 = 0
    for i in range(num):
        if politeness(i,num):
            num2 += 1
    return num2

    
def smith(num):
    prime = 0
    for i in primes(num):
        prime += i
    digits = 0
    new_num = num
    while new_num != 0:
        digits = new_num % 10
        new_num = new_num // 10
    return prime == digits
    
def Fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return Fibonacci(num-1) + Fibonacci(num-2)

