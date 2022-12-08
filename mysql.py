import pymysql
from pymysql.cursors import SSDictCursor

class Commn:
    def __init__(self):
        self.conn = pymysql.connect('localhost','root','123456','woniusal',charse='utf8')
        self.cursor = self.conn.cursor() #默认游标类型返回的数据为：（（），（），（））
        self.cursor = self.conn.cursor(SSDictCursor) #使用SSDictCursor的游标来获取数据，此时数据库返回的数据类型为字典，{{}，{}，{}}
