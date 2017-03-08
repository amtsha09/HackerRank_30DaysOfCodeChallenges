############# Day 9 ################# FACTORIAL

def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
    
if __name__ == "__main__":
    n=int(input("please enter the number: "))
    print(factorial(n))

