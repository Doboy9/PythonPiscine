ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}




ft_list[1] = "World"
#Changing the array normally



ft_tuple = (ft_tuple[0], "France")
# TypeError: 'tuple' object does not support item assignment, so we need to create a new one


ft_set.remove("tutu!")
ft_set.remove("Hello")
ft_set.add("Angouleme")
ft_set.add("Hello")
# TypeError: 'set' object is not subscriptable, so we need to remove and add a new one
# Working as a stack so we need to get all out before changing the value



ft_dict["Hello"] = "42Angouleme"
#Functioning like map in c++, so we change the value associated with the key



print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
