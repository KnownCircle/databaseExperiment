import random
import numpy as np
mean = 80
std_dev = 15
lower_bound = 0
upper_bound = 100

cnos=set()
snos=set()
sc=set()
times=200000
with open('course2.txt','r',encoding='utf-8') as c:
    while True:
        line = c.readline().strip()
        if not line:
            break
        cnos.add(line.split('$')[0])

with open('students5.txt','r',encoding='utf-8') as s:
    while True:
        line = s.readline().strip()
        if not line:
            break
        snos.add(line.split('$')[0])

with open('sc2.txt', 'w', encoding='utf-8') as f:
    for _ in range(times):
        while True:
            cno=random.choice(list(cnos))
            sno=random.choice(list(snos))
            if (cno,sno) not in sc:
                sc.add((cno,sno))
                while True:
                    grade=np.random.normal(mean, std_dev)
                    if grade>=lower_bound and grade<=upper_bound:
                        break
                write_line=f'{sno}${cno}${grade:.1f}\n'
                f.write(write_line)
                break


