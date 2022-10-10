while True:
    n =int(input("please enter any positive numbers"))
    if n<0:
        print("Error Enter positive value")
    else:
        sum =0
        i=n
        while i>0:
            sum +=i
            i -=1
        print("Sum of all positive numbers till ",n," is ",sum)
    