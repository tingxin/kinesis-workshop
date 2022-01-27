import time
import json
import pymysql.cursors
from pysqler import Insert
import setting
from mysql import get_conn
from mock import gen


conn = get_conn()
creator = gen()

for item in creator:
    try:
        command = Insert("`{0}`".format(setting.Focus_TB))
        item = gen
        for key in item:
            command.put(key, item[key])

        print("mock: {0}".format(item))
        with conn.cursor() as cursor:
            sql = str(command)
            cursor.execute(sql)
            conn.commit()

    except Exception as e:
        print(e)
        time.sleep(60)
        conn.close()
        conn = get_conn()
