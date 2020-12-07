# demonstrate hashtable usage

logs = ['88 99 200', '88 99 300', '99 32 100', '12 12 15']
threshold = 2


counts = {}
result_list = []



for line in logs:
    first = line.split(' ')[0]
    second = line.split(' ')[1]
    if first == second:
        if first in counts.keys():
            counts[first] += 1
            counts[first] += 1
        else:
            counts[first] = 1
            counts[second] = 1
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