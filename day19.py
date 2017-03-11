from interface import Interface,implements

class AdvancedArithmetic(Interface):
    def divisorSum(self,n):pass

class Calculator(implements(AdvancedArithmetic)):
    def divisorSum(self,n):
        sum = 0
        for i in range(1,n+1//2):
            if n%i == 0 :
                sum += i
        return sum+n
        
        
if __name__ == "__main__":
    n = input()
    try:
        n = int(n)
    except:
        print("Enter a valid number")
    
    calculate = Calculator()
    print(calculate.divisorSum(n))