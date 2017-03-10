class Calculator(object):
    def __init__(self):
        pass
    
    def power(self,n,p):
        self.n = n
        self.p = p
        if self.n|self.p <0:
            raise Exception("n and p should be non-negative")
        return (self.n**self.p)

if __name__ == '__main__':
	myCalculator=Calculator()
	T=int(input())
	for i in range(T):
	    n,p = map(int, input().split())
	    try:
	        ans=myCalculator.power(n,p)
	        print(ans)
	    except Exception as e:
	        print(e)