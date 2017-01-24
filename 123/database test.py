import sqlite3

def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value = '0'
    return float(value)

conn = sqlite3.connect('food.db')
curs = conn.cursor()

curs.execute('''
CREATE TABLE food(
id TEXT PRIMARY KEY,
desc TEXT,
water FLOAT,
kcal FLOAT,
)

''')

query = 'INSERT INTO food VALUES(?,?,?)'



conn.commit()
conn.close()
