# read logs and print by order based on threshold

logs = ['1 2 50', '1 7 70', '1 3 20', '2 2 17']
threshold = 2
counts = {}
result_list = []
for line in logs:
    first = line.split(' ')[0]
    second = line.split(' ')[1]
    if first == second:
        if first in counts.keys():
            counts[first] += 1
        else:
            counts[first] = 1
    else:
        if first in counts.keys():
            counts[first] += 1
        else:
            counts[first] = 1
        if second in counts.keys():
            counts[second] += 1
        else:
            counts[second] = 1
for item in counts.items():
    if item[1] >= threshold:
        result_list.append(item[0])
result_list.sort()
print(result_list)