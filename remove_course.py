with open("course1.txt",'r',encoding='utf-8') as f:
    with open('course2.txt','w',encoding='utf-8') as f2:
        cnos=set()
        while True:
            line=f.readline().strip()
            if not line:
                break
            words=line.split('$')
            cno=words[0]
            if cno not in cnos:
                cnos.add(cno)
                f2.write(line+'\n')
            