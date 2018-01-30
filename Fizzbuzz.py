#Ispisi brojeve od 1 do 100, ako je %3 pisi 'Fizz', ako %5 'Buzz' i ako je oboje onda 'FizzBuzz'
#ideja sa: http://www.codinghorror.com/blog/2007/02/why-cant-programmers-program.html
#29.10.2011


def main():
	for i in range(1, 101):
		tekst = str(i) * (bool((i%3)) and bool((i%5))) + bool(not(i%3)) * 'Fizz' + bool(not(i%5)) * 'Buzz'
		print tekst
	return 0	
	
	
def bla_bla():
	for i in range(1, 101):
		if not (i % 3) and not (i % 5):
			print "FizzBuzz"
		elif not (i % 3):
			print "Fizz"
		elif not (i % 5):
			print "Buzz"
		else:
			print i
	return 0
	
if __name__ == '__main__':
	main()