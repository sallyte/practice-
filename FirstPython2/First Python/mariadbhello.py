import mysql.connector

# 데이터베이스에 연결
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7081",
    database="classicmodels",
    charset='utf8mb4',  
    collation = 'utf8mb4_general_ci'
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM customers")
rows = cursor.fetchall()  # 모든 결과 가져오기

for row in rows:
    print(row)
'''
    query = "INSERT INTO your_table (column1, column2) VALUES (%s, %s)"
values = ("value1", "value2")
cursor.execute(query, values)
connection.commit()  # 변경 사항을 저장

query = "UPDATE your_table SET column1 = %s WHERE column2 = %s"
values = ("new_value", "value_condition")
cursor.execute(query, values)
connection.commit()

query = "DELETE FROM your_table WHERE column1 = %s"
value = ("value_to_delete",)
cursor.execute(query, value)
connection.commit()'''