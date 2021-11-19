import csv
import sqlite3

connection = sqlite3.connect('pokemon.db')
cursor = connection.cursor()
create_table = """CREATE TABLE IF NOT EXISTS tbl_pokemon(
                id INTEGER,
                name TEXT,
                type_1 TEXT,
				type_2 TEXT,
				total INTEGER,
                hp INTEGER,
                attack INTEGER,
                defense INTEGER,
                sp_attack INTEGER,
                sp_defense INTEGER,
                speed INTEGER,
                generation INTEGER,
                legendary INTEGER
            )
            """

cursor.execute(create_table)
file = open('pokemon.csv')
contents = csv.reader(file)
next(contents, None)

delete_all = "DELETE FROM tbl_pokemon"
rows = cursor.execute(delete_all)

insert_records = "INSERT INTO tbl_pokemon (id, name, type_1, type_2, total, hp, attack, defense, sp_attack, sp_defense, speed, generation, legendary) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
cursor.executemany(insert_records, contents)

select_all = "SELECT * FROM tbl_pokemon"
rows = cursor.execute(select_all).fetchall()

for r in rows:
    print(r)

connection.commit()
connection.close()
