import re
import xlwt
import sqlite3
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

url = "https://movie.douban.com/top250?start="

def open_url(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}
    # data = bytes(urllib.parse.urlencode({"1":"2"}),encoding="utf-8")
    rep = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(rep)
    html = response.read().decode("utf-8")
    return  html

move_name = re.compile(r'<img alt="(.*?)"',re.S)
move_link = re.compile(r'<a href="(.*?)"',re.S)
move_average = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>',re.S)
move_data = []

def get_data():
    for i in range(10):
        link = url + str(i*25)
        html = open_url(link)
        # print(link)
        bs = BeautifulSoup(html,"html.parser")
        # content = bs.select('div[class="item"]')
        content = bs.find_all('div',class_='item')
        for datas in content:
            data = []
            datas = str(datas)
            data_1 = re.findall(move_name,datas)
            # print(data_1)
            data_2 = re.findall(move_link, datas)
            # print(data_2)
            data_3 = re.findall(move_average, datas)
            # print(data_3)
            data.append(data_1)
            data.append(data_2)
            data.append(data_3)
            move_data.append(data)
    move_data.sort(key=lambda x:eval(x[-1][0]),reverse=True)
    # print(move_data)
    return move_data

def write_excel():
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet("move_data",cell_overwrite_ok=True)
    for i in range(len(move_data)):
        worksheet.write(i,0,move_data[i][0])
        worksheet.write(i,1,"https://yun.tv920.com/?url="+move_data[i][1][0])
        worksheet.write(i,2, move_data[i][2])
    workbook.save("move.xls")
    print("数据写入完成!")

sql1 = '''
    create table move(
        name varchar ,
        link varchar ,
        average real 
);
'''
sql2 = '''
    drop table move;
'''
def write_sql():
    conn = sqlite3.connect("move.db")
    cur = conn.cursor()
    try:
        cur.execute(sql1)
    except:
        cur.execute(sql2)
    finally:
        cur.execute(sql1)
        for i in range(1,len(move_data)):
            sql = '''
                insert into move values ('{}','{}','{}');
            '''.format(move_data[i][0][0],move_data[i][1][0],move_data[i][2][0])
            # print(move_data[i][0][0],move_data[i][1][0],move_data[i][2][0])
            cur.execute(sql)
    conn.commit()
    conn.close()
    print("写入数据成功！")

if __name__ == '__main__':
    get_data()
    # write_excel()
    write_sql()