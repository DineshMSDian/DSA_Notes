def pyout(n):

    if n == 27+1:   # Using Base Condition , it prevents the infinite loop
        return

    print(n)
    n += 1

    pyout(n)

n = 0
pyout(n)
