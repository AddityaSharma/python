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

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------- #

# lecture-7: Loops and iterations

# for loop:
nums = [1,2,3,4,5]

# kind of for_each loop in c++
for x in nums:
    print(x)

# range -> [0, 10)
for i in range(10):  # single argument specifies the end point(exclusive)
    print(i)

# range -> [1, 11)
for i in range(1, 11):  # first argument specifes the start point(inclusive), second argument the end point(exclusive)
    print(i)


# while loop:
x = 0
while x < 10:
    print(x)
    x += 1
    
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------- #














