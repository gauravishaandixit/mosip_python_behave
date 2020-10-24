import mysql.connector
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="ishaan",
  database = 'mosip'
)

cur = db.cursor()
'''
sql = 'insert into users values (%s, %s, %s, %s, %s, %s, %s, %s, %s)'
val = ('Subarna', 'Kanti', 'male', '1996-03-20','12345@gmail.com', '1234','abcdef.com','kolkata','active')
cur.execute(sql, val)
db.commit()
print(cur.rowcount, 'row inserted')
'''
cur.execute('select * from users where email = %s', ['1234@gmail.com'])
rows = cur.fetchall()
print(rows)
cur.execute('desc users')
columnNames = [row[0] for row in cur.fetchall()]
print(columnNames)