import sqlite3
import datetime
from models import Book, Student
def add_book():
    print("--- Yeni Kitap Ekle ---")
    title = input("Kitabın Adı: ")
    author = input("Yazarın Adı: ")
    category = input("Kategori: ")

    if title == "" or author == "" or category == "":
        print("Hata: Kitap adı, yazar ve kategori alanları boş bırakılamaz!")
        return
    try:
        total_count = int(input("Toplam Adet: "))
    except ValueError:
        print("Hata: Toplam adet için lütfen sadece sayı girin!")
        return
    available_count = total_count

    yeni_kitap = Book(title, author, category, total_count, available_count)

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO books (title, author, category, total_count, available_count) VALUES (?, ?, ?, ?, ?))", (yeni_kitap.title, yeni_kitap.author, yeni_kitap.category, yeni_kitap.total_count, yeni_kitap.available_count))
    conn.commit()
    conn.close()
    print(f"'{yeni_kitap.title}' kütüphaneye başarıyla eklendi!")

def list_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    kitaplar = cursor.fetchall()
    for kitap in kitaplar:
        print(f"ID: {kitap[0]}")
        print(f"Kitap: {kitap[1]}")
        print(f"Yazar: {kitap[2]}")
        print(f"Kategori: {kitap[3]}")
        print(f"Toplam Adet: {kitap[4]}")
        print(f"Raftaki Adet: {kitap[5]}")
    conn.close()

def add_student():
    name = input("Öğrencinin Adı: ")
    try:
        student_no = int(input("Öğrenci Numarası: "))
    except ValueError:
        print("Hata: Öğrenci Numarası için lütfen sadece sayı giriniz!")
        return
    department = input("Bölüm: ")
    if name == "" or department == "":
        print("Hata: Öğrenci Adı ve Bölüm alanları boş bırakılamaz!")
        return

    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE student_no = ?", (student_no,))
    mevcut_ogrenci = cursor.fetchone()
    if mevcut_ogrenci:
        print("Hata: Bu numaraya sahip bir öğrenci sisteme zaten kayıtlı!")
        conn.close()
        return
    yeni_ogrenci = Student(name,student_no, department)
    cursor.execute("INSERT INTO students (name, student_no, department) VALUES (?,?,?)", (yeni_ogrenci.name, yeni_ogrenci.student_no, yeni_ogrenci.department))
    conn.commit()
    conn.close()
    print(f"'{yeni_ogrenci.name}' isimli öğrenci sisteme başarıyla eklendi!")

def list_students():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    ogrenciler = cursor.fetchall()
    for ogrenci in ogrenciler:
        print(f"ID: {ogrenci[0]}\nAd Soyad: {ogrenci[1]}\nNumara: {ogrenci[2]}\nBölüm: {ogrenci[3]}")
        print("-" * 20)
    conn.close()

def borrow_book():
    try:
        student_no = int(input("Öğrenci Numarası: "))
    except ValueError:
        print("Hata: Öğrenci Numarası için lütfen sadece sayı giriniz!")
        return
    try:
        book_ID = int(input("Kitap ID: "))
    except ValueError:
        print("Hata: Kitap ID için lütfen sadece sayı giriniz!")
        return
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE student_no = ?", (student_no,))
    ogrenci = cursor.fetchone()
    if not ogrenci:
        print("Hata: Öğrenci bulunamadı!")
        conn.close()
        return

    cursor.execute("SELECT * FROM books WHERE ID = ?", (book_ID,))
    kitap = cursor.fetchone()
    if not kitap:
        print("Hata: Kitap bulunamadı!")
        conn.close()
        return

    if kitap[5] == 0:
        print("Maalesef bu kitabın tüm nüshaları şu an ödünç verilmiş durumda!")
        conn.close()
        return

    cursor.execute("UPDATE books SET available_count = available_count - 1 WHERE ID = ?", (book_ID,))
    bugun = str(datetime.date.today())
    durum = "Ödünç Alındı"
    cursor.execute("INSERT INTO borrow_records (book_ID, student_ID, borrow_date, status) VALUES (?, ?, ?, ?)",(book_ID, ogrenci[0], bugun, durum))
    conn.commit()
    conn.close()
    print(f"Başarılı: {kitap[1]} adlı kitap, {ogrenci[1]} isimli öğrenciye ödünç verildi!")

def return_book():
    try:
        student_no = int(input("Öğrenci Numarası: "))
    except ValueError:
        print("Hata: Öğrenci Numarası için lütfen sadece sayı giriniz!")
        return
    try:
        book_ID = int(input("Kitap ID: "))
    except ValueError:
        print("Hata: Kitap ID için lütfen sadece sayı giriniz!")
        return
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE student_no = ?", (student_no,))
    ogrenci = cursor.fetchone()

    if not ogrenci:
        print("Hata: Öğrenci bulunamadı!")
        conn.close()
        return
    cursor.execute("SELECT * FROM borrow_records WHERE student_ID = ? AND book_ID = ? AND status = 'Ödünç Alındı'",(ogrenci[0], book_ID))
    islem_kaydi = cursor.fetchone()
    if not islem_kaydi:
        print("Hata: Bu kitabın bu öğrenci tarafından ödünç alındığına dair aktif bir kayıt bulunamadı!")
        conn.close()
        return

    cursor.execute("UPDATE books SET available_count = available_count + 1 WHERE ID = ?", (book_ID,))
    bugun = str(datetime.date.today())
    cursor.execute("UPDATE borrow_records SET return_date = ?, status = 'İade Edildi' WHERE ID = ?",(bugun, islem_kaydi[0]))
    conn.commit()
    conn.close()
    print(f"Başarılı: {book_ID} ID'li kitap, {ogrenci[1]} isimli öğrenciden teslim alındı ve rafa eklendi!")


def search_book():
    aranacak_kelime = input("Aramak istediğiniz kitap adı veya yazar adını giriniz!")
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    arama_terimi = f"%{aranacak_kelime}%"
    cursor.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ?", (arama_terimi, arama_terimi))
    bulunan_kitaplar = cursor.fetchall()
    if not bulunan_kitaplar:
        print(f"Hata: Aradığınız kriterlerde kitap bulunamadı.")
    else:
        for kitap in bulunan_kitaplar:
            print(f"{kitap[1]} - {kitap[2]}")

    conn.close()


def show_student_books():
    try:
        student_ID = int(input("Öğrenci ID giriniz: "))
    except ValueError:
        print("Hata: Lütfen sadece sayı giriniz!")
        return
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    sql_sorgusu = """
    SELECT students.name, books.title 
    FROM borrow_records 
    JOIN students ON borrow_records.student_ID = students.ID 
    JOIN books ON borrow_records.book_ID = books.ID 
    WHERE borrow_records.student_ID = ? AND borrow_records.status = 'Ödünç Alındı'
    """

    cursor.execute(sql_sorgusu, (student_ID,))
    aktif_kitaplar = cursor.fetchall()

    if not aktif_kitaplar:
        print("Bilgi: Bu öğrencinin üzerinde iade edilmemiş aktif bir kitap bulunmamaktadır.")
    else:
        ogrenci_adi = aktif_kitaplar[0][0]
        print(f"\n{ogrenci_adi} adlı öğrencinin aldığı kitaplar:")

        sayac = 1
        for kayit in aktif_kitaplar:
            kitap_adi = kayit[1]
            print(f"{sayac} - {kitap_adi}")
            sayac += 1
    conn.close()







