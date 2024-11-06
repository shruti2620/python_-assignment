# write the python programm to get te fibonacci series from the range 

def fibonacci_series(n):
    fib_sequence = []
    a,b = 0,1 
    while a<= n :
        fib_sequence.append(a)
        a,b = b,a+b 
        print(fib_sequence)

num = int(input("Enter the range of fibonacci series:"))
if num<0:
    print("enter non-negative number")
else:
    print(f"Fibonacci series up to {num} is : {fibonacci_series(num)}")