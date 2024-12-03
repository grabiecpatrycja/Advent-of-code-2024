data= []
with open("input_2.txt") as file:
    for line in file:
        lst = line.rstrip().split(' ')
        data.append(list(map(int, lst)))

#part_1
safe_1 = 0
for lst in data:
    sort_lst = sorted(lst)
    if lst == sort_lst or lst == sort_lst[::-1]:
        for index, element in enumerate(lst[:-1]):
            diff = abs(element - lst[index+1])
            if diff not in [1, 2, 3]:
                break
        else:
            safe_1 += 1

print(safe_1)

#part_2
def different_element(lst):
    sort_lst = sorted(lst)
    different_element =[a for a, b in zip(lst, sort_lst) if a!=b]
    return different_element

safe_2 = 0
for lst in data:
    one_removed = False
    if len(different_element(lst)) == 2:
        elements = different_element(lst)
        lst.remove(elements[0])
        one_removed = True
            
    sort_lst = sorted(lst)
    if lst == sort_lst or lst == sort_lst[::-1]:
        for index, element in enumerate(lst[:-1]):
            diff = abs(element - lst[index+1])
            if diff > 3:
                break
            elif one_removed == False and diff == 0:
                one_removed = True
        else:
            safe_2 += 1

print(safe_2)
