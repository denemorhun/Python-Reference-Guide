import re

fcon = open("hosts_access_log_00.txt", "r")
txt = fcon.read()
fcon.close()
# res = re.findall(r"([a-z0-6]+[.][a-z]+[.][a-z]+)\s(- -)", txt)
res = re.findall(r"([a-z0-6]+[.][a-z]+[.][a-z]+[- -] + (19)\d\d[- /.](0[1-9]|95)", txt)
lst = []
count = []
for a in res:
    nex = True
    for b in lst:
        if b == a[0]:
            nex = False
            count[lst.index(b)] += 1
    if nex:
        lst.append(a[0])
        count.append(1)

fil = open('records_hosts_access_log_00.txt', 'w')
for i in range(len(lst)):
    fil.write(lst[i] + " " + str(count[i]) + '\n')

fil.close()