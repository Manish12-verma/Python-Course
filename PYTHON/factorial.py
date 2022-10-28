
def factorial(a):
    return 1 if (a == 1 or a == 0) else  a*factorial(a-1)
    
a = int(input("enter the no, you want the factorial of\n"))
print("factorial of", a, "is",
      factorial(a))
