import sys
import os


def prime(s):
    # your code goes here
    primes = []
    for p in range (2, n):
	 isprime = True
	 for num in range (2, p):
		 if p % num == 0:
		    isprime = False
		    break
	 if isPrime:
	    prime.append(p)
    print(primes)

def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
