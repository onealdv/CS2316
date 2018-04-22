import csv, getpass, pymysql, sys
from datetime import datetime

def insert_record(record, conn):
    cursor = conn.cursor()
    try:
        cursor.execute("insert into routes values (%s, %s)",
                       (record['route_id'], record['route_name']))
    except pymysql.IntegrityError as e:
        if e.args[0] == 1062:
            pass
        else:
        	raise

    try:
        cursor.execute("insert into stops values (%s, %s)",
                       (record['stop_id'], record['stop_name']))
    except pymysql.IntegrityError as e:
        if e.args[0] == 1062:
            pass
        else:
        	raise

    try:
        cursor.execute("insert into vehicles values (%s)",
                       (record['vehicle_id']))
    except pymysql.IntegrityError as e:
        if e.args[0] == 1062:
            pass
        else:
        	raise

    try:
        cursor.execute("insert into passenger_data values (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (record['index'],
                        datetime.strptime(record['date'],"%m/%d/%Y").date(),
                        record['route_id'], record['direction'],
                        record['stop_id'],
                        record['ons'] if record['ons'] else 0,
                        record['offs'] if record['offs'] else 0,
                        record['vehicle_id']))
    except pymysql.IntegrityError as e:
        if e.args[0] == 1062:
            pass
        else:
        	raise

    conn.commit()

if __name__ == "__main__":
    csv_file = sys.argv[1]
    db = sys.argv[2]
    host = sys.argv[3]
    user = sys.argv[4]
    pw = getpass.getpass()

    conn = pymysql.connect(host= host, user= user, password= pw, db= db,
                           charset= "utf8mb4",
                           cursorclass= pymysql.cursors.DictCursor)
    with open(csv_file) as fin:
        for record in csv.DictReader(fin):
            insert_record(record, conn)
    conn.close()
    print(f"{db} populated.")
