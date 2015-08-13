from string import atof
import re

d = dict()
f = open('dns.log')
for line in f.readlines():
    content = line.strip().split()
    if content[20] != '-':
        a = content[20].split(',')
        for element in a:
            r = re.search('(\d+\.\d+\.\d+\.\d+)', element)
            if r:
                value = str(content[8])
                key = r.group()
                d[key] = value

#for key in d.keys():
#    print 'key=%s, value=%s' % (key, d[key])
b = open('b.txt')
for line in b.readlines():
    content = line.strip().split()
    print str(content[0]),d.get(content[0],None)

f.close()
b.close()
       
