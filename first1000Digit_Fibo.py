def getFirst1000DigitFib():
    FibArray = [0,1]

    # Dynamic programming
    def fibonacci(n): 
        if n<=len(FibArray): 
            return FibArray[n-1]
        else: 
            temp_fib = fibonacci(n-1)+fibonacci(n-2)
            FibArray.append(temp_fib)
            return temp_fib

    count = 2
    # Exit the while loop when the last element in FibArray becomes 1000 digits
    while len(str(FibArray[-1])) <= 999:
        fibonacci(count)
        count += 1
    
    return FibArray[-1], len(str(FibArray[-1]))

print(getFirst1000DigitFib())
