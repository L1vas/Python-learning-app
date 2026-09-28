import sqlite3

conn = sqlite3.connect("data/python_coach.db")
cursor = conn.cursor()

# Get all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("=== TABLES ===")
for t in tables:
    print(t[0])

# Get schema for each table
print("\n=== SCHEMA ===")
for t in tables:
    tname = t[0]
    cursor.execute(f"PRAGMA table_info({tname})")
    cols = cursor.fetchall()
    print(f"\n{tname}:")
    for col in cols:
        print(f"  {col}")

# Get lessons
print("\n=== LESSONS ===")
cursor.execute("SELECT id, title FROM lessons")
lessons = cursor.fetchall()
for l in lessons:
    print(f"  {l[0]}: {l[1]}")

# Get exercises
print("\n=== EXERCISES ===")
cursor.execute("SELECT id, lesson_id, instructions FROM exercises")
exercises = cursor.fetchall()
for e in exercises:
    print(f"  {e[0]} (lesson {e[1]}): {e[2][:60]}...")

# Check users table
print("\n=== USERS ===")
cursor.execute("SELECT id, username FROM users")
users = cursor.fetchall()
print(f"  {len(users)} users")

conn.close()
