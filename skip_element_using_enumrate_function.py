'''Try out the enumerate function for yourself in this quick exercise.
 Complete the skip_elements function to return every other element from the list, 
 this time using the enumerate function to check if an element is on an even position or an odd position.'''

#The enumerate() function takes a list as a parameter and returns a tuple for each element in the list. The first value of the tuple is the index and the second value is the element itself.

def skip_elements(elements):
     new_list=[]
     for index, element in enumerate(elements):
         if index % 2 == 0:
             new_list.append(element)
     return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']