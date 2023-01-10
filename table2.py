import csv
import sqlite3

conn = sqlite3.connect('base.db')
cur = conn.cursor()

with open('clothes.csv') as csvfile:
    reader = list(csv.reader(csvfile, delimiter=';'))
    for r in reader[1:]:
        cur.execute(f"INSERT INTO clothes(id, image_name) VALUES ({r[0]}, {r[1]})")
        conn.commit()


with open('weatherid.csv') as csvfile:
    reader = list(csv.reader(csvfile, delimiter=';'))
    for r in reader[1:]:
        cur.execute(f"INSERT INTO weatherid(id2, image_name) VALUES ({r[0]}, '{r[1]}')")
        conn.commit()


with open('weather.csv') as csvfile:
    reader = list(csv.reader(csvfile, delimiter=';'))

    for r in reader[1:]:
        print(r[0], r[1])
        cur.execute(f'INSERT INTO weather(id2) VALUES ({r[1]})')
        conn.commit()


with open('temp.csv') as csvfile:
    reader = list(csv.reader(csvfile, delimiter=';'))

    for r in reader[1:]:
        print(r[0], r[1], r[2])
        cur.execute(f'INSERT INTO temp(temp_mn, temp_mx) VALUES ({r[1]}, {r[2]})')
        conn.commit()


with open('style.csv') as csvfile:
    reader = list(csv.reader(csvfile, delimiter=';'))

    for r in reader[1:]:
        print(r[0], r[1])
        cur.execute(f'INSERT INTO style(style) VALUES ("{r[1]}")')
        conn.commit()


with open('transport.csv') as csvfile:
    reader = list(csv.reader(csvfile, delimiter=';'))

    for r in reader[1:]:
        print(r[0], r[1])
        cur.execute(f'INSERT INTO transport(transport) VALUES ("{r[1]}")')
        conn.commit()


with open('description.csv') as csvfile:
    reader = list(csv.reader(csvfile, delimiter=';'))

    for r in reader[1:]:
        print(r[0], r[1])
        cur.execute(f'INSERT INTO description(id, description) VALUES ({r[0]}, {r[1]})')
        conn.commit()