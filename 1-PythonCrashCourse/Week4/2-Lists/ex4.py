# Try out the enumerate function for yourself in this quick exercise. 
# Complete the skip_elements function to return every other element from the list, 
# this time using the enumerate function to check if an element is on an even position 
# or an odd position.

def skip_elements(elements):
    new_list = []
    for index, element in enumerate(elements):
    #    print(index, element)
        if index%2 == 0:
            new_list.append(element)
    #print new_list
    return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']