# lecture-6: booleans and conditionsals

# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
    # Any empty mapping. For example, {}.

# to get the memory location of an element , we use the id method
# a = 7
# print(id(a)) -> print outs address of object a.

# is Vs ==
a = [1,2,3]
b = [1,2,3]
print(a == b) # true -> as both list cantains same elements.
print(a is b) # false -> is operators check whether a and b are same objects in memory or not.

c = [4,5,6]
d = c
print(c == d) # true -> as both list cantains same elements.
print(c is d) # true -> both the list share same memory address if we assign one list to another. *important*/
