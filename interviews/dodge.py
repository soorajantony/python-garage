num_array = [97, 42, 11,34, 65, 66,23, 38, 69, 12]

new_array = []

for i in range(1,len(num_array)):
    for j in num_array:
        if num_array[i] +1 == j:
            new_array.append(num_array[i])
            new_array.append(j)

print(new_array)



