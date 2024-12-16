from typing import Any

def all_thing_is_obj(object: any) -> int:

	class_to_know = type(object)
	if isinstance(object, str):
		print(f"{object} is in the kitchen : {class_to_know}")
		return 42
	if isinstance(object, int):
		print("Type not found")
		return 42
	print(f"{type(object).__name__.capitalize()} : {class_to_know}")
	return 42