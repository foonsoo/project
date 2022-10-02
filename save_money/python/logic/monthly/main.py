import os
import pymysql
import datetime
import calendar

# 월간 데이터 마트 구성을 위한 코드 

db_host = os.environ['db_host']
db_user = os.environ['db_user']
db_pass = os.environ['db_pass']
db_name = os.environ['db_name']
today = datetime.datetime.now()
two_month_ago = today.date() - datetime.timedelta(days=60)
two_month_ago_year = str(two_month_ago.strftime("%Y"))+"년"
two_month_ago_month = str(two_month_ago.strftime("%m"))+"월"
tma = two_month_ago_year+two_month_ago_month
last_day_check = calendar.monthrange(two_month_ago.year, two_month_ago.month)[1]
conn = pymysql.connect(host=db_host,user=db_user,password=db_pass,db=db_name,charset='utf8')
a = ["101","102","103","104","105","106","107"]


def monthly_card_ym():
    for i in a:
        cur = conn.cursor()
        cur.execute("select sum(a.amount_used) from card_usage as a WHERE used_date BETWEEN %s AND %s AND card_id = '1' AND category_code = %s", (two_month_ago.replace(day=1), two_month_ago.replace(day=last_day_check),i))
        result = cur.fetchone()
        if result[0] == None:
            continue
        else:
            if i == "101":
                cur.execute("insert into monthly_card (년월, 분류, 총합, card_id) value (%s, %s, %s, %s)", (tma, '생활비', int(result[0]), 1))
            elif i == "102":
                cur.execute("insert into monthly_card (년월, 분류, 총합, card_id) value (%s, %s, %s, %s)", (tma, '고정비', int(result[0]), 1))
            elif i == "103":
                cur.execute("insert into monthly_card (년월, 분류, 총합, card_id) value (%s, %s, %s, %s)", (tma, '경조사비', int(result[0]), 1))
            elif i == "104":
                cur.execute("insert into monthly_card (년월, 분류, 총합, card_id) value (%s, %s, %s, %s)", (tma, '여행비', int(result[0]), 1))
            elif i == "105":
                cur.execute("insert into monthly_card (년월, 분류, 총합, card_id) value (%s, %s, %s, %s)", (tma, '세금', int(result[0]), 1))
            elif i == "107":
                cur.execute("insert into monthly_card (년월, 분류, 총합, card_id) value (%s, %s, %s, %s)", (tma, '외식비', int(result[0]), 1))
            else:
                cur.execute("insert into monthly_card (년월, 분류, 총합, card_id) value (%s, %s, %s, %s)", (tma, '기타', int(result[0]), 1))
            conn.commit()

def monthly_card_sj():
    for i in a:
        cur = conn.cursor()
        cur.execute("select sum(a.amount_used) from card_usage as a WHERE used_date BETWEEN %s AND %s AND card_id = '2' AND category_code = %s", (two_month_ago.replace(day=1), two_month_ago.replace(day=last_day_check),i))
        result = cur.fetchone()
        if result[0] == None:
            continue
        else:
            if i == "101":
                cur.execute("insert into monthly_card (년월, 분류, 총합, card_id) value (%s, %s, %s, %s)", (tma, '생활비', int(result[0]), 2))
            elif i == "102":
                cur.execute("insert into monthly_card (년월, 분류, 총합, card_id) value (%s, %s, %s, %s)", (tma, '고정비', int(result[0]), 2))
            elif i == "103":
                cur.execute("insert into monthly_card (년월, 분류, 총합, card_id) value (%s, %s, %s, %s)", (tma, '경조사비', int(result[0]), 2))
            elif i == "104":
                cur.execute("insert into monthly_card (년월, 분류, 총합, card_id) value (%s, %s, %s, %s)", (tma, '여행비', int(result[0]), 2))
            elif i == "105":
                cur.execute("insert into monthly_card (년월, 분류, 총합, card_id) value (%s, %s, %s, %s)", (tma, '세금', int(result[0]), 2))
            elif i == "107":
                cur.execute("insert into monthly_card (년월, 분류, 총합, card_id) value (%s, %s, %s, %s)", (tma, '외식비', int(result[0]), 2))
            else:
                cur.execute("insert into monthly_card (년월, 분류, 총합, card_id) value (%s, %s, %s, %s)", (tma, '기타', int(result[0]), 2))
            conn.commit()

if __name__ == "__main__":
    monthly_card_ym()
    monthly_card_sj()