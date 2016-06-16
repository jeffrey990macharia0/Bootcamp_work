def prime_number(n):
	x=[]
	primes=[]
	for value in range(n):
		if (value < 2): return False
		if (value == 2): primes.append(value)
		if (value % 2 == 0): return False
		for factor in range(3, 1+int(round(value**0.5)), 2):
        		if (value % factor == 0):
           			 return False
		primes.append(value)
		
	for i in primes:
		print i
prime_number(8)
