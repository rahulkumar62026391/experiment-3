from mysql.connector import connect

conn = connect(
    host="localhost",
    user="root",
    password="wrogn",
    database="teacher"
)

cur = conn.cursor()

cur.execute("""
    create view faculty as select id, name, dept_name from instructor;
""")

conn.commit()
conn.close()
print("faculty view created successfully")