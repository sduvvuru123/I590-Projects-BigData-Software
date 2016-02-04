import sys

a=int(sys.argv[1])

def fizzbuzz(num):

	for x in range(1, num):
		if x % 2 == 0 and x % 3 ==0: print "fizzbuzz"
		elif x % 2 == 0: print "fizz"
		elif x % 3 == 0: print "buzz"
		else: print x

fizzbuzz(a)
