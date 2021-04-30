import sqlite3

# Establist con/cur connections
con = sqlite3.connect('example.db')
cur = con.cursor()

# Create a table
cur.execute("CREATE TABLE students (name text, age real, state text)")

# Save (commit) the changes
con.commit() 

# Insert into db
cur.execute("INSERT INTO students VALUES ('Yael', 34, 'Maryland')")

cur.execute("INSERT INTO students VALUES ('Steve', 34, 'Texas')")
cur.execute("INSERT INTO students VALUES ('Sarah', 14, 'California')")
cur.execute("INSERT INTO students VALUES ('Matt', 22, 'Arizona')")
cur.execute("INSERT INTO students VALUES ('Kevin', 12, 'Washington')")
cur.execute("INSERT INTO students VALUES ('Ariel', 26, 'Florida')")
cur.execute("INSERT INTO students VALUES ('Darryl', 39, 'Georgia')")

# Get from database
for row in cur.execute("SELECT * FROM students"):
    print(row)

rows = list()
for row in cur.execute("SELECT * FROM students"):
    rows.append(row)

    # [('Yael', 34.0, 'Maryland'), ('Steve', 34.0, 'Texas'), ('Sarah', 14.0, 'California'), ('Matt', 22.0, 'Arizona'), ('Kevin', 12.0, 'Washington'), ('Ariel', 26.0, 'Florida'), ('Darryl', 39.0, 'Georgia')]

print(rows)
print(row[0][0]) # 'Yael'


# Update from database
print("before")

res = list()
for row in cur.execute("SELECT * FROM students WHERE name = 'Yael'"):
    res.append(row)

print(res[0][0])

cur.execute("UPDATE students SET name = 'YaEL' WHERE name = 'Yael'")
con.commit()

print("after")
res = list()
for row in cur.execute("SELECT * FROM students WHERE name = 'Yael'"):
    res.append(row)

print(res[0][0])

# Delete from database
cur.execute("DELETE FROM students WHERE name = 'Kevin'")
con.commit()

# Close connection
con.close()