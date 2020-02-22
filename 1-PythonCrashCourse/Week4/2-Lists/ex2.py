def skip_elements(elements):
	# code goes here
    newList = []
    for i in elements:
        if elements.index(i) % 2 == 0:
            newList.append(elements[elements.index(i)])
    return newList

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

