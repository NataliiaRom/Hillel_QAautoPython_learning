# connect to Postgres DB

import psycopg2

conn = psycopg2.connect(
    dbname="hillel_2025",
    user="postgres",
    password="postgres",
    host="localhost",
    port = "5432"
)

print("Connected to DB")