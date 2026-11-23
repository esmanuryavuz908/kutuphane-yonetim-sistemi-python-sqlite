import services
import database
import reports
def main_menu():
    while True:
        print("\n" + "=" * 50)
        print("    AKILLI KÜTÜPHANE VE ÖĞRENCİ TAKİP SİSTEMİ    ")
        print("=" * 50)
        print("1 - Yeni Kitap Ekle")
        print("2 - Tüm Kitapları Listele")
        print("3 - Yeni Öğrenci Ekle")
        print("4 - Tüm Öğrencileri Listele")
        print("5 - Kitap Ödünç Ver")
        print("6 - Kitap İade Al")
        print("7 - Kitap Ara")
        print("8 - Öğrencinin Kitaplarını Göster")
        print("9 - Geciken Kitapları Göster")
        print("10 - En Çok Ödünç Verilen Kitaplar")
        print("0 - Çıkış")
        print("=" * 50)

        secim = input("Lütfen yapmak istediğiniz işlemi seçin (0-6): ")

        if secim == '1':
            services.add_book()
        elif secim == '2':
            services.list_books()
        elif secim == '3':
            services.add_student()
        elif secim == '4':
            services.list_students()
        elif secim == '5':
            services.borrow_book()
        elif secim == '6':
            services.return_book()
        elif secim == '7':
            services.search_book()
        elif secim == '8':
            services.show_student_books()
        elif secim == '9':
            reports.show_overdue_books()
        elif secim == '10':
            reports.most_borrowed_books()
        elif secim == '0':
            print("\nSistemden çıkılıyor. İyi günler dileriz!")
            break
        else:
            print("\nHata: Lütfen sadece menüdeki numaralardan (0-6) birini tuşlayın!")

if __name__ == "__main__":
                main_menu()


