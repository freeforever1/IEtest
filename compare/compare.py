from string import atof

f= open('conn.log')
x = 0
for line in f.readlines():
    x += 1
    content = line.strip().split()
    if content[6] == 'tcp' and content[8] != '-':
        orig_bytes = int(content[9])
        resp_bytes = int(content[10])
        if orig_bytes > resp_bytes:
            #print x,str(content[2]),int(content[3]),str(content[4]),int(content[5]),str(content[7]),str(content[8]),int(content[9]),int(content[10])
            print str(content[4])
       
