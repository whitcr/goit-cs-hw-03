import random

from faker import Faker
from psycopg2 import connect, errors

fake = Faker()

conn = connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="1111",
)
cur = conn.cursor()

for _ in range(10):
    fullname = fake.name()
    email = fake.email()
    try:
        cur.execute(
            "INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email)
        )
    except errors.UniqueViolation:
        print(f"Така пошта вже є")

for user_id in range(1, 11):
    for _ in range(random.randint(1, 5)):
        title = fake.sentence()
        description = fake.text()
        status_id = random.randint(1, 3)
        cur.execute(
            "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
            (title, description, status_id, user_id),
        )

conn.commit()
cur.close()
conn.close()
