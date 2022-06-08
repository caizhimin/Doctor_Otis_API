import azure.cosmos.cosmos_client as cosmos_client
import inspect
import time

DS_QA_cosmos_url = 'https://cosmos-ds-dre-dev-china-001.documents.azure.com:443/'
DS_QA_master_key = 'ZdnspmAuIP2MV8aFG7m8gKn3Ceo01sRBN0NlU58pSep0nbYVjFOX0CJX9i9UGHPgI2aQCgtdU4VXo0cSLEFG4g=='


def get__function_name():
    """获取正在运行函数(或方法)名称"""
    return inspect.stack()[1][3]


class Cosmos:
    def __init__(self, url="", key="", database_id=""):

        self.client = cosmos_client.CosmosClient(url, {'masterKey': key})
        self.database = self.client.get_database_client(database_id)

    def insert(self, container_id, data):
        """
        新增不需要插入id主键， 会自动生成
        :param database_id:
        :param container_id:
        :param data: 需要插入的字典
        :return:
        """
        result = None
        try:
            container = self.database.get_container_client(container_id)
            result = container.create_item(data)
        except Exception as ex:
            result = None
        return result

    def update(self, container_id, replace_data):
        """
        update必须指定id主键
        :param database_id:
        :param container_id:
        :param replace_data: 需要更新的全文字典
        :return:
        """
        container = self.database.get_container_client(container_id)
        return container.upsert_item(replace_data)

    def query(self, container_id, fields=None, query_params=None,
              order_by=None, desc=False, offset=0, limit=None, cross_partition=True):
        """
        :param database_id:
        :param container_id:
        :param fields: 需要查询的字段, tuple类型, 空值默认为全部查询，
        :param query_params:  查询条件，dict类型, 空值默认为无条件,
        :param order_by: 排序字段, 空值默认无排序
        :param desc: 是否倒序, 默认顺序，True为倒序，False为顺序
        :param offset: 偏移 int类型
        :param limit: 截断 int类型
        :param cross_partition: 是否跨分区查询，默认True支持，False不支持
        :return:items
        """
        if fields:
            map_fields = tuple(map(lambda x: container_id + '.' + x, fields))
            fields_str = ', '.join(map_fields)
            sql = 'SELECT %s FROM %s' % (fields_str, container_id)
        else:
            sql = 'SELECT * FROM %s' % container_id
        if query_params:
            sql += ' WHERE '
            for k, v in query_params.items():
                if isinstance(v, str):
                    sql += '%s.%s = "%s" and ' % (container_id, k, v)
                if isinstance(v, int):
                    sql += '%s.%s = %s and ' % (container_id, k, v)
        if sql.endswith('and '):
            sql = sql[:-5]
        if order_by:
            sql += ' ORDER BY %s.%s' % (container_id, order_by)
            if desc:
                sql += ' DESC'
        if limit:
            sql += ' OFFSET %s LIMIT %s' % (offset, limit)
            print(sql)
        container = self.database.get_container_client(container_id)
        items = container.query_items(sql, enable_cross_partition_query=cross_partition)
        return list(items)

    def query_by_raw(self, container_id, raw_sql, parameters=None, partition_key=None, cross_partition=True):
        container = self.database.get_container_client(container_id)
        items = container.query_items(raw_sql, parameters=None, partition_key=partition_key,
                                      enable_cross_partition_query=cross_partition)
        return list(items)

    def deleteItem(self, container_id, data, partition_key=None):
        container = self.database.get_container_client(container_id)
        container.delete_item(data, partition_key)

    def check_unit_offline_three_days(self, unit_number):
        """
        检查电梯三天内是否离线
        :param unit_number:
        :return:
        """
        query = cosmos.query('COLLECTION_DSLOG_MASTER', fields=('GWToCloud', 'GWToCloudChangeTime'),
                             query_params={'UnitNumber': unit_number})[0]
        GWToCloud = str(query.get('GWToCloud'))
        GWToCloudChangeTime = query.get('GWToCloudChangeTime')
        now = int(time.time())
        if GWToCloudChangeTime and (GWToCloud == '1') and ((now - GWToCloudChangeTime) >= 3 * 24 * 3600):
            return True
        else:
            return False


cosmos = Cosmos(DS_QA_cosmos_url, DS_QA_master_key, 'DoctorOtis')


