import sys

class Solution:
    def __init__(self):
        self.stack = list()
        self.queue = list()
    
    def pushCharacter(self, i):
        self.stack.append(i)
    
    def enqueueCharacter(self,i):
        self.queue.append(i)
    
    def popCharacter(self):
        return self.stack.pop()
    
    def dequeueCharacter(self):
        a = self.queue[0]
        self.queue.remove(a)
        return a

if __name__ == '__main__':

	# read the string s
	s=input()
	#Create the Solution class object
	obj=Solution()   

	l=len(s)
	# push/enqueue all the characters of string s to stack
	for i in range(l):
	    obj.pushCharacter(s[i])
	    obj.enqueueCharacter(s[i])
	    
	isPalindrome=True
	'''
	pop the top character from stack
	dequeue the first character from queue
	compare both the characters
	''' 
	for i in range(l // 2):
	    if obj.popCharacter()!=obj.dequeueCharacter():
	        isPalindrome=False
	        break
	#finally print whether string s is palindrome or not.
	if isPalindrome:
	    print("The word, "+s+", is a palindrome.")
	else:
	    print("The word, "+s+", is not a palindrome.")    