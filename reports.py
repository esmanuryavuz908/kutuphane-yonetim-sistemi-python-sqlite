import sqlite3
import datetime
def show_overdue_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    sql_sorgusu = """
     SELECT students.name, books.title, borrow_records.borrow_date 
     FROM borrow_records 
     JOIN students ON borrow_records.student_ID = students.ID 
     JOIN books ON borrow_records.book_ID = books.ID 
     WHERE borrow_records.status = 'Ödünç Alındı'
     """

    cursor.execute(sql_sorgusu)
    odunc_alinanlar = cursor.fetchall()
    bugun = datetime.date.today()
    for kayit in odunc_alinanlar:
        ogrenci_adi = kayit[0]
        kitap_adi = kayit[1]
        alinma_tarihi_metin = kayit[2]
        alinma_tarihi = datetime.datetime.strptime(alinma_tarihi_metin, "%Y-%m-%d").date()
        gecen_gun = (bugun - alinma_tarihi).days
        if gecen_gun > 15:
            print(f"- {ogrenci_adi}, '{kitap_adi}' adlı kitabı {gecen_gun} gündür elinde tutuyor. (Gecikmiş!)")
    conn.close()

def most_borrowed_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    sql_sorgusu = """
    SELECT books.title, COUNT(borrow_records.book_ID) 
    FROM borrow_records 
    JOIN books ON borrow_records.book_ID = books.ID 
    GROUP BY books.title 
    ORDER BY COUNT(borrow_records.book_ID) DESC
    """
    cursor.execute(sql_sorgusu)
    populer_kitaplar = cursor.fetchall()

    if not populer_kitaplar:
        print("Bilgi: Sistemde henüz ödünç verilmiş hiç kitap kaydı bulunmuyor.")
    else:
        print("\n--- En Çok Ödünç Verilen Kitaplar ---")

        sayac = 1

        for kayit in populer_kitaplar:
            kitap_adi = kayit[0]
            odunc_sayisi = kayit[1]

            print(f"{sayac} - {kitap_adi} | {odunc_sayisi} kez ödünç verildi")

            sayac += 1
    conn.close()
def show_categories():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT category FROM books")
    tum_kategoriler = cursor.fetchall()
    benzersiz_kategoriler = set()
    for kayit in tum_kategoriler:
        benzersiz_kategoriler.add(kayit[0])
        print("\n--- Sistemdeki Benzersiz Kategoriler ---")
        for kayit in benzersiz_kategoriler:
            print("kategori")
    conn.close()
