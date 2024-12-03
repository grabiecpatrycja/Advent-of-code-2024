from collections import Counter

left = []
right = []

with open("input_1.txt") as file:
    for line in file:
        l, r = line.split('   ')
        left.append(int(l))
        right.append(int(r.rstrip()))

left.sort()
right.sort()

#part_1
total_distance = 0
for i, e in enumerate(left):
    total_distance += abs(e-right[i])

print(total_distance)

#part_2
right_counter = Counter(right)
right_set = set(right)

similarity_score = 0
for element in left:
    if element in right_set:
        similarity_score += element * right_counter[element]

print(similarity_score)
