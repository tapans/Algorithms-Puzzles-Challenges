import sys

def divide(dividend, divisor):
	max_num = sys.maxsize
	min_num = -max_num - 1
	if divisor == 0:
		return max_num
	if divisor == -1 and dividend == min_num: 
		return max_num

	neg = True if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0) else False
	dividend, divisor = abs(dividend), abs(divisor)
	quotient = 0
	while dividend >= divisor:
		exp = 0
		while dividend >= (divisor << exp):
			exp += 1
		dividend = dividend - (divisor << (exp - 1))
		quotient = quotient + (1 << (exp - 1))
	return -quotient if neg else quotient

if __name__ == '__main__':
	if len(sys.argv) > 2:
		print(divide(int(sys.argv[1]), int(sys.argv[2])))
	else:
		print(divide(50, 3))
