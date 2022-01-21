import pymysql
import configparser
import logging

# 定义日志格式
logging.basicConfig(level=logging.WARN, format='%(asctime)s %(levelname)s %(message)s', filename='machine.log')


class DBMysql(object):
    def __init__(self, **kwargs):
        # if not db:
        #     raise RuntimeError('数据库配置错误！')
        cf = configparser.ConfigParser(allow_no_value=True)
        try:
            cf.read('db.ini')
            self.host = cf.get('db', 'host')
            self.password = cf.get('db', 'password')
            self.user = cf.get('db', 'user')
            self.database = cf.get('db', 'database')
            self.port = cf.getint('db', 'port')
            self.charset = cf.get('db', 'charset')
            self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                        port=self.port, charset=self.charset, **kwargs)
        except Exception as e:
            # print('数据库错误：',e)
            logging.error('数据库错误：{}'.format(e))
        else:
            self.cursor = self.conn.cursor()
            logging.info('数据库连接正常')

    def __del__(self):
        if self.conn is not None:
            self.cursor.close()  # 关闭游标
            self.conn.close()  # 关闭连接
            logging.info('退出数据库连接...')

    # 查询数据函数，并返回查询条数
    def query(self, sql, args=None):
        data = ''
        count = 0
        try:
            self.cursor.execute(sql, args)
            # print('传入的sql:',select_all_sql)
        except Exception as e:
            logging.error('数据库错误：{}'.format(e))
        else:
            data = self.cursor.fetchall()  # 获取所有查询记录
            count = self.cursor.rowcount
            self.conn.commit()
            logging.info('执行成功！{}'.format(self.cursor.rowcount))
        return count, data

    # 不返回查询数量的函数
    def query_single(self, sql, args=None):
        data = ''
        print(args)
        try:
            self.cursor.execute(sql, args)
            # print('传入的sql:',select_all_sql)
        except Exception as e:
            logging.error('数据库错误：{}'.format(e))
        else:
            data = self.cursor.fetchall()  # 获取所有查询记录
            # count = self.cursor.rowcount
            self.conn.commit()
            logging.info('执行成功！{}'.format (self.cursor.rowcount))
            # print('DB',data)
        return data

    def alter(self, sql, args=None):
        # 修改、插入、删除数据
        try:
            self.cursor.execute(sql, args)
        except Exception as e:
            logging.error('数据库错误：{}'.format(e))
            self.conn.rollback()
        else:
            self.conn.commit()  # 提交记录
            #
            logging.info('-->{} 条记录执行成功！'.format(self.cursor.rowcount))
        return self.cursor.rowcount

    def alter_many(self, sql1, sql2, args1, args2):
        # 修改、插入、删除数据 多条记录
        try:
            self.cursor.execute(sql1, args1)
            self.cursor.execute(sql2, args2)
        except Exception as e:
            logging.error('数据库错误：{}'.format(e))
            self.conn.rollback()
        else:
            self.conn.commit()  # 提交记录

            logging.info('-->{} 条记录执行成功！'.format(self.cursor.rowcount))
        return self.cursor.rowcount

    def alter_multi(self, sql, args=None):
        # 修改、插入、删除数据
        try:
            self.cursor.executemany(sql, args)
            # print(args)
        except Exception as e:
            logging.error('数据库错误：{}'.format(e))
            self.conn.rollback()
        else:
            self.conn.commit()  # 提交记录

            logging.info('-->{} 条记录执行成功！'.format(self.cursor.rowcount))
        return self.cursor.rowcount
