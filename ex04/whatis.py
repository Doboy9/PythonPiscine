import sys

try:
	assert len(sys.argv) == 2, "more than one argument is provided"
	number = int(sys.argv[1])
	if(number % 2 == 0):
		print("I'm even")
	else:
		print("I'm odd")
except AssertionError as e:
	print(f"AssertionError: {e}")
except ValueError:
	print("AssertionError: argument is not an integer")