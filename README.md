# Akıllı Kütüphane ve Öğrenci Takip Sistemi

## Proje Amacı
Bu proje, bir okul kütüphanesinin temel operasyonlarını dijitalleştirmek amacıyla geliştirilmiştir. Kullanıcılar sistem üzerinden kitap ve öğrenci ekleyebilir, ödünç alma/iade etme işlemlerini yürütebilir ve geciken kitaplar ile kütüphane istatistiklerini raporlayabilir.

## Kullanılan Teknolojiler
* Python (OOP, Fonksiyonel Programlama, Veri Yapıları - List, Set, Dictionary)
* SQLite3 (Veritabanı Yönetimi ve Gelişmiş SQL Sorguları - JOIN, GROUP BY, COUNT, LIKE)
* datetime (Zaman ve Gecikme Hesaplamaları)
* PyCharm (Geliştirme Ortamı)

## Veritabanı Yapısı
Projede 3 temel tablo kullanılmıştır:
1. **books:** Kütüphanedeki kitapların detaylarını (ad, yazar, kategori, stok) tutar.
2. **students:** Öğrenci bilgilerini (ad, no, bölüm) barındırır.
3. **borrow_records:** Öğrencilerin hangi kitabı ne zaman aldığını ve iade durumlarını takip eder.

## Özellikler
* Sınıf (Class) yapısı kullanılarak Nesne Yönelimli Programlama (OOP) mantığıyla veri işleme.
* Kategori tekrarlarını önlemek için Set (Küme) veri yapısı kullanımı.
* Hatalı veri girişlerini (harf/sayı karışıklığı) önleyen try-except kontrolleri.
* 15 günü geçen gecikmiş kitapların tarih matematiği ile otomatik tespiti.
* En çok okunan kitapların analizi ve istatistiksel raporlaması.

## Kurulum Adımları
1. Proje dosyalarını bilgisayarınıza indirin.
2. Python ortamınızın kurulu olduğundan emin olun.
3. Terminal veya komut satırında proje dizinine gidin.
4. `python main.py` komutunu çalıştırarak sistemi başlatın. Veritabanı (`library.db`) ilk çalıştırılmada otomatik olarak oluşturulacaktır.