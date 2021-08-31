from collections import Counter

values = [47, 95, 88, 73, 88, 84]

total = sum(values)
value_counter = len(values)

values.sort()

if value_counter % 2 == 0:
    median1 = values[value_counter//2]
    median2 = values[value_counter//2 - 1]
    median = (median1 + median2)/2
else:
    median = values[value_counter//2]

data = Counter(values)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

if len(mode) == value_counter:
    get_mode = "No mode found"
else:
    get_mode = "Mode is / are: " + ', '.join(map(str, mode))


print('The Sum of the values is: ', total)

print('The Count of the values is: ', value_counter)

print('The Mean of the values is: ', total/value_counter)

print('The Median of the values is: ', median)

print('The Mode of the values is: ', get_mode)



