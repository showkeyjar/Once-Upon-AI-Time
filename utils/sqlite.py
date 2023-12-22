import sqlite3
import pandas as pd
from zhconv import convert
# https://github.com/gumblex/zhconv
"""
读取sqlite中的资料
"""

def query_raw(sql):
    result = None
    conn = sqlite3.connect('db/latest.db')
    cur = conn.cursor()
    try:
        # 查询
        cur.execute(sql)
        result = cur.fetchall()  # 返回一个列表套元组或空列表，例如[(3, 'eth', 81, 81, 81, 1639553167), (4, 'eth', 81, 81, 81, 1639553169), ...]
        conn.commit()
    except Exception as e:
        print(str(e))
    finally:
        cur.close()
        conn.close()
    return result


def pd_query(sql):
    df = None
    conn = sqlite3.connect('db/latest.db')
    try:
        df = pd.read_sql_query(sql, conn)
    except Exception as e:
        print(str(e))
    finally:
        conn.close()
    return df


def get_author_info(author, dynasty):
    result = None
    author_hant = convert(author, 'zh-hant')
    dynasty_hant = convert(dynasty, 'zh-hant')
    sql = f"""SELECT b.* FROM BIOG_MAIN b left join 
    DYNASTIES d on b.c_dy = d.c_dy
    WHERE b.c_name_chn = '{author_hant}' and d.c_dynasty_chn='{dynasty_hant}'
    """
    df_result = pd_query(sql)
    if len(df_result)>0:
        result = df_result.iloc[0].to_dict()
    return result

