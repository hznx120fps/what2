import sqlite3
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY,
            name TEXT,
            class_name TEXT)""")

cur.execute("""CREATE TABLE IF NOT EXISTS grades(
            id INTEGER PRIMARY KEY,
            student_id INTEGER,
            subject TEXT,
            grade INTEGER,
            FOREIGN KEY(student_id) REFERENCES students(id))""")

students = [
    (1, "Anna", "10-A"),
    (2, "Bohdan", "10-A"),
    (3, "Marta", "10-B"),
    (4, "Ivan", "10-B")
]

grades = [
    (1,1,"Math",10),
    (2,1,"SQL",12),
    (3,2,"Math",8),
    (4,2,"SQL",9),
    (5,3,"Math",11),
    (6,3,"SQL",10),
    (7,4,"Math",7),
    (8,4,"SQL",12),
]

cur.executemany("INSERT INTO students VALUES (?,?,?)", students)
cur.executemany("INSERT INTO grades VALUES (?,?,?,?)", grades)

cur.execute("CREATE INDEX idx_student_id ON grades(student_id)")

print("inner join")
for row in cur.execute("""SELECT students.name, grades.subject, grades.grade FROM students
                       INNER JOIN grades on students.id = grades.student_id"""):
    print(row)

print("agg + group by")
for row in cur.execute("""SELECT students.name, AVG(grades.grade) AS avg_grade, COUNT(grades.id) AS subjects_count
                       FROM students LEFT JOIN grades ON students.id = grades.student_id GROUP BY students.name"""):
    print(row)

print("min + max")
for row in cur.execute("""SELECT subject, MAX(grade) AS max_grade, MIN(grade) AS min_grade FROM grades
                       GROUP BY subject"""):
    print(row)