# coding=utf-8
__author__ = 'zhangteng'

from db import DB
from config import HMySQL
import time

conn = DB(HMySQL())

day_l = ['20170701','20170702','20170703','20170704','20170705','20170706','20170707','20170708','20170709','20170710','20170711','20170712','20170713','20170714','20170715','20170716','20170717','20170718','20170719','20170720','20170721','20170722','20170723','20170724','20170725','20170726','20170727','20170728','20170729','20170730','20170731','20170801','20170802','20170803','20170804','20170805','20170806','20170807','20170808','20170809','20170810','20170811','20170812','20170813','20170814','20170815','20170816','20170817','20170818','20170819','20170820','20170821','20170822','20170823','20170824','20170825','20170826','20170827','20170828','20170829','20170830','20170831','20170901','20170902','20170903','20170904','20170905','20170906','20170907','20170908','20170909','20170910','20170911','20170912','20170913','20170914','20170915','20170916','20170917','20170918','20170919','20170920','20170921','20170922','20170923','20170924','20170925','20170926','20170927','20170928','20170929','20170930','20171001','20171002','20171003','20171004','20171005','20171006','20171007','20171008','20171009','20171010','20171011','20171012','20171013','20171014','20171015','20171016','20171017','20171018','20171019','20171020','20171021','20171022']

for day in day_l:
    begin = time.time()
    update_sql = "UPDATE dw_student_behavior SET event_time = unix_timestamp(event_time_fstr) * 1000 WHERE day='%s'" % day
    result = conn.execute(update_sql)
    end = time.time()
    print(day, "rows ", result.rowcount, "cost", end-begin)
