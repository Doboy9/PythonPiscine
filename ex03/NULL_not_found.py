import math

def NULL_not_found(object: any) -> int:
	null_to_know = type(object)
	if object is None:
		print(f"Nothing: None {null_to_know}")
	elif object == 0 and type(object) is int:
		print(f"Zero: 0 {null_to_know}")
	elif isinstance(object, float) and math.isnan(object):
		print(f"Cheese: nan {null_to_know}")
	elif isinstance(object, str) and object == '':
		print(f"Empty: {null_to_know}")
	elif isinstance(object, bool) and object == False:
		print(f"Fake: {null_to_know}")
	else:
		print("Type not found")
	return 1
