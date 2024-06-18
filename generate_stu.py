from faker import Faker
import random

fake = Faker('zh_CN')  # 使用中文数据
Faker.seed(0)
existing_ids = set()
cnt=5000
i=0
with open("student2.txt",'a',encoding='utf-8') as f:
    while i<cnt:
        while True:
            sno1 = f'{random.randint(10000000, 99999999)}'
            sno2 = f'{random.randint(10000000, 99999999)}'
            sno = sno1+sno2
            if sno not in existing_ids:
                existing_ids.add(sno)
                i+=1
                break

        sname = fake.name()
        sex = random.choice(['男', '女'])
        bdate = fake.date_of_birth(minimum_age=18, maximum_age=22).strftime('%Y-%m-%d')
        height = random.uniform(1.5, 2.0)
        dorm1 = random.choice(['东', '西'])
        dorm2 = f'{random.randint(1, 20)}'
        dorm3=random.randint(100, 999)
        dorm = f'{dorm1}{dorm2}舍{dorm3}'
        line=f'{sno}${sname}${sex}${bdate}${height:.2f}${dorm}\n'
        # print(line)
        f.write(line)
