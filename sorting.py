## Insert your code here...
## A quick note on mutable types and operating in-place
my_list = [5, 5, 5, 5, 5]

def my_func(some_list):
    some_list[1] = 999

# Note that the function doesn't return anything, and here we don't assign any new variables either
my_func(my_list)
print(my_list)

my_list = [5, 5, 5, 5, 5]

def my_func(some_list):
    new_list = some_list.copy()
    new_list[1] = 999
    return new_list

my_new_list = my_func(my_list)
print(my_list)  # Now the same as before
print(my_new_list)

##
my_list = [5, 5, 5, 5, 5]

def my_func(some_list):
    new_list = some_list.copy()
    new_list[1] = 999
    return new_list

my_new_list = my_func(my_list)
print(my_list)  # Now the same as before
print(my_new_list)
