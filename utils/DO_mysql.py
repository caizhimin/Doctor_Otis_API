import pymysql

host = "do-api-database-vegctujtkpkfg.mysql.database.azure.com"
user = "cai@do-api-database-vegctujtkpkfg"
password = "1Q2w3e4r"
database = "do_api"


def get_unit_oil(unit_number):
        """
        满油规格213ml， 2/3为142ml, 不得低于1/3  71ml
        :param unit_number:
        :return:
        """
        conn = pymysql.connect(host=host, user=user, password=password, database=database,
                               charset='utf8')
        cursor = conn.cursor()
        sql = "select oil from elevator_master_data where unit_number='%s'" % unit_number
        cursor.execute(sql)
        data = cursor.fetchone()
        cursor.close()
        conn.close()
        if data:
            return data[0]
        else:
            return 0


def reset_unit_oil(unit_number):
    """
    重设油杯容量为142ml
    :param unit_number:
    :return:
    """
    conn = pymysql.connect(host=host, user=user, password=password, database=database,
                           charset='utf8')
    cursor = conn.cursor()
    update_sql = "UPDATE elevator_master_data SET oil = 142 WHERE unit_number='%s'" % unit_number
    try:
        cursor.execute(update_sql)
        conn.commit()
    except:
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


