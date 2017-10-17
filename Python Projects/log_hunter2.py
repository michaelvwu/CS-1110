# Michael Wu (mvw5mf)

import re

def read_log(filename):
    log = []
    datafile = open(filename, 'r')
    for line in datafile:
        line = line.strip()
        log.append(line)
    datafile.close()


    return log

datafiletwo = open("access.log", "r")

cav = 0
wahoo = 0

for line in datafiletwo:
    line = line.strip()
    if line.startswith("172.25"):
        cav += 1
    elif line.startswith("172.27"):
        wahoo +=1

print("Cavalier", cav)
print("Wahoo", wahoo)


basket = open("access.log", 'r')

hunter = re.findall(r'(https?://\S+)', basket)
print(hunter)





