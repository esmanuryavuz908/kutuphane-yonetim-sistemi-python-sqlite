import sqlite3
def create_tables():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS books(ID INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, category TEXT, total_count INTEGER, available_count, INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS students(ID INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, student_no INTEGER, department TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS borrow_records(ID INTEGER PRIMARY KEY AUTOINCREMENT, book_ID INTEGER, student_ID INTEGER, borrow_date TEXT, return_date TEXT, status TEXT)")
    conn.commit()
    conn.close()