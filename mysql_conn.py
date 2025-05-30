import mysql.connector
conn = mysql.connector.connect(
    host="172.22.124.105", #need to update host ip from WSL wvery time when we start new session'''
    user="Mahi",
    password="Mahi@1992",
    database="collage"
)
cursor = conn.cursor()
cursor.execute("select database();")
result = cursor.fetchone()
print("connected to database:", result)
cursor.close()
conn.close()