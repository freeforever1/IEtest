from string import atof

s=set([])
f = open('compare.txt')
for line in f.readlines():
    content = line.strip().split()
    if content[0].startswith('192.168.') == 0:
        s.add(content[0]+"\n")
f.close()
f=open('b.txt', 'w')
lines=list(s)
f.writelines(lines)
f.close()



       
