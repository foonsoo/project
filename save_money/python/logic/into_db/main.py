import glob2
import os
import pymysql
import pandas as pd

ford_excel_1 = glob2.glob('/data/mail/*.xlsx')
db_host = os.environ['db_host']
db_user = os.environ['db_user']
db_pass = os.environ['db_pass']
db_name = os.environ['db_name']

def insert_db():
    conn = pymysql.connect(host=db_host,user=db_user,password=db_pass,db=db_name,charset='utf8')
    cur = conn.cursor()
    sql = "insert into usage (id, date, franchisee, used) value (%s, %s, %s, %s)"
    for file in ford_excel_1:
        df = pd.read_excel(file,skiprows=[0,1,2])
        df_v1 = pd.read_excel(file,usecols = [1,2,3,4,9],skiprows=[0,1],skipfooter=2)
        list_value = []
        for index in df_v1.iterrows():
            if index[1]["가맹점"] == "서비스":
                pass
            elif str(index[1][2]) == "nan":
                pass
            elif str(index[1][2]) == "\xa0":
                pass
            elif index[1]["가맹점"] == "할인":
                pass
            elif index[1]["가맹점"] == "청구할인":
                pass
            else:
                if index[1]["이용카드"] == "000":
                    list_value.append((1, index[1][0], index[1][3], int(index[1][4].replace(',',''))))
                else:
                    list_value.append((2, index[1][0], index[1][3], int(index[1][4].replace(',',''))))
        cur.executemany(sql, list_value) ## 일괄 적재
        conn.commit()
    conn.close()

if __name__ == "__main__":
    insert_db()