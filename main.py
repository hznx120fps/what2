import sqlite3
conn = sqlite3.connect("university.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS students (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               age INTEGER,
               major TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS courses (
               course_id INTEGER PRIMARY KEY AUTOINCREMENT,
               course_name TEXT,
               instructor TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS student_courses (
               student_id INTEGER,
               course_id INTEGER,
               FOREIGN KEY (student_id) REFERENCES students(id),
               FOREIGN KEY (course_id) REFERENCES courses(id),
               PRIMARY KEY (student_id, course_id)
               )''')


while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Вихід")

    choice = input("Оберіть опцію(1-7)")
    if choice == "1":
        name = input("Введіть ім'я студента: ")
        age = int(input("Введіть вік студента: "))
        major = input("Введіть спеціальність студента: ")

        cursor.execute('''INSERT INTO students (name, age, major) VALUES (?,?,?)''', (name, age, major))
        conn.commit()

    elif choice == "2":
        course_name = input("Введіть назву курсу: ")
        instructor = input("Введіть викладача курсу: ")

        cursor.execute('''INSERT INTO courses (course_name, instructor) VALUES (?,?)''', (course_name, instructor))
        conn.commit()

    elif choice == "3":
        cursor.execute('''SELECT * FROM students''')
        students = cursor.fetchall()

        if not students:
            print("404 not found")
        else:
            for student in students:
                print(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Major: {student[3]}")
    
    elif choice == "4":
        cursor.execute('''SELECT * FROM courses''')
        courses = cursor.fetchall()

        if not courses:
            print("404 not found")
        else:
            for course in courses:
                print(f"ID: {course[0]}, Name: {course[1]}, Instructor: {course[2]}")

    elif choice == "5":
        course_id = int(input("Введіть ID курсу: "))
        student_id = int(input("Введіть ID студента: "))

        cursor.execute('''INSERT INTO student_courses (student_id, course_id) VALUES (?,?)''', (student_id, course_id))
        conn.commit()

    elif choice == "6":
        course_id = int(input("Введіть ID курсу: "))
        cursor.execute('''SELECT students.id, students.name FROM students, student_courses
                       WHERE students.id = student_courses.student_id''')

    elif choice == "7":
        break

    else:
        print("Error! Enter number 1-7")

conn.close()