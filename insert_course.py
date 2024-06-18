import psycopg2
from psycopg2 import sql, Error

try:
    conn = psycopg2.connect(
        dbname='mydb',
        user='lzy',
        password='zzz-1234-aaa',
        host='127.0.0.1',
        port='5432'
    )
    print("已连接数据库"+'mydb')
except Error as e:
    print(f"连接失败!!!: {e}")
    exit(1)  # 退出程序

try:
    cur = conn.cursor()

    try:
        with open('course.txt', 'r') as f:
            while True:
                line = f.readline()
                if not line.strip():
                    break  # 空行，文件已经结束
                try:
                    items = line.split()
                    cno = items[0]
                    cname = items[1]
                    period = items[2]
                    credit = items[3]
                    teacher = items[4]
                    cur.execute(
                        f"INSERT INTO course (cno, cname, period, credit,teacher) VALUES (\'{cno}\', \'{cname}\', {period}, {credit}, \'{teacher}\')")
                    print("已插入数据")
                except Error as e:
                    print(f"插入失败: {e}")
    except FileNotFoundError as e:
        print(f"students.txt打开失败: {e}")
        exit(1)

    # 提交事务
    try:
        conn.commit()
        print("事务提交成功")
    except Error as e:
        print(f"事务提交失败: {e}")

    # 关闭游标和连接
    cur.close()
    conn.close()
except Error as e:
    print(f"游标创建失败: {e}")
