'''Complete the skip_elements function to return every other element from the list, 
this time using a list comprehension to generate the new list based on the previous one, 
where elements in odd positions are skipped.'''
def skip_elements(elements):
	return [element for element in elements [0:len(elements):2]] 

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']