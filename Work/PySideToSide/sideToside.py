import os

#with open('B.txt', 'r') as sec:
    #log = sec.read()
    #start = log.index('  "tests": [{')
    #end = log.index('  }],')

    #with open('new.txt', 'w') as wr:
        #wr.write(m[start:end])
        
f = open("B.txt", 'r').read()
result = open("Newest.txt", 'w')
result.write(f[f.index('[{'):f.index('  "suites"')])

result.close()
