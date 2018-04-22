
from pprint import pprint
import csv
import getpass
import pymysql
import sys

def insert_record(record, conn):
    cursor=conn.cursor()
    cursor.execute('delete from passenger_data where indexx = %s',(record['index']))
    try:
        cursor.execute('insert into routes values (%s, %s)',(record['route_id'], record['route_name']))
    except:
        pass
    try:
        cursor.execute('insert into stops values (%s, %s)',(record['stop_id'],record['stop_name']))
    except:
        pass
    try:
        cursor.execute('insert into vehicles values (%s)',(record['vehicle_id']))
    except:
        pass
    if record['ons'] and record ['offs'] != '':
        cursor.execute('insert into passenger_data values (%s,%s,%s,%s,%s,%s,%s,%s)',(record['index'],record['date'],record['route_id'],record['direction'],record['stop_id'],record['ons'],record['offs'],record['vehicle_id']))
    elif record['ons'] != '':
        cursor.execute('insert into passenger_data values (%s,%s,%s,%s,%s,%s,%s,%s)',(record['index'],record['date'],record['route_id'],record['direction'],record['stop_id'],record['ons'],0,record['vehicle_id']))
    elif record['offs'] != '':
        cursor.execute('insert into passenger_data values (%s,%s,%s,%s,%s,%s,%s,%s)',(record['index'],record['date'],record['route_id'],record['direction'],record['stop_id'],0,record['offs'],record['vehicle_id']))
    else:
        cursor.execute('insert into passenger_data values (%s,%s,%s,%s,%s,%s,%s,%s)',(record['index'],record['date'],record['route_id'],record['direction'],record['stop_id'],0,0,record['vehicle_id']))

    conn.commit()


if __name__=='__main__':
    infile = sys.argv[1]
    db = sys.argv[2]
    host = sys.argv[3]
    user = sys.argv[4]
    #pw= getpass.getpass(f'Password for {user}@{host}: ')
    print(f'Importing data from {infile} into {db} database on {host}...')
    conn = pymysql.connect(host=host, user=user, db=db, cursorclass=pymysql.cursors.DictCursor)
    with open(infile) as fin:
        reader= csv.DictReader(fin)
        for record in reader:
            insert_record(record, conn)
    print('Done.')
