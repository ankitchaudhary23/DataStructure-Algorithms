## Accessing Values in Lists :
# 			Use square brackets for slicing along with index or indicies

## List Methods:

# 1. index():
#		- list.index(element, start, end)
# 		- returns index of the given element (1st occurenec) in the list

# 2. append():
#		- list.append(item / list)
#		- adds a single item on the end of the list
#		- doesn't return any value (returns None)

# 3. extend():
#		- list.extend(iterable)
#		- adds all the elements of an iterable (list, tuple, string, etc) to end of the list. 
#		- modifies original list. Returns None.

# 4. insert():
#		- list.insert(i, element / tuple)
#		- inserts an element to the list at the specified index
#		- Returns None. Updates current list.

# 5. remove():
#		- list.remove(elem)
#		- removes 1st macthing element from list.
#		- Returns None. Throw ValueError if elem doesn't exist

# 6. popp():
# 		- list.pop(index)
#		- removes item at given index from list. Default index is -1
#		- returns removed item. Throw IndexError exception if index not in range.

# 7. count():
#		- list.count(element/ tuple / list)
#		- returns # of times the specified element appears in list

# 8. reverse():

# 9. sort():
#		- list.sort(reverse = True/False, key = optional)

# 10. copy()
# 11. clear()
