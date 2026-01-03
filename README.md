# BLM101 – Bilgisayar Mühendisliğine Giriş  
## Dönem Projesi

---

##  Öğrenci Bilgileri
- **Ad Soyad:** Sümeyra Muslu  
- **Öğrenci Numarası:** 2025360859055  
- **Bölüm:** Bilgisayar Mühendisliği  
- **Ders:** BLM101 – Bilgisayar Mühendisliğine Giriş  
- **Dersi Veren:** Prof. Dr. Turgay Tugay Bilgin  

---

## Proje Konusu
**Veri Depolama ve Sayısal Sistemler**  
**Çok Fonksiyonlu Taban Dönüştürücü (Python)**

---

##  YouTube Video Linki
🔗 https://www.youtube.com/XXXXXXXXXXX  
*(Video, sunum anlatımı ve Python kodunun çalıştırılmasını içermektedir.)*

---

##  Proje Açıklaması

Bu projede, onluk (decimal) tabanda girilen bir sayının kullanıcı seçimine bağlı olarak  
**ikilik (binary)** veya **onaltılık (hexadecimal)** tabana dönüştürülmesi amaçlanmıştır.  
Ayrıca girilen sayının bilgisayar belleğinde **8-bitlik hücreler (byte)** halinde  
nasıl temsil edildiği konsol çıktısı olarak gösterilmektedir.

Proje kapsamında Python dilinde, **hazır dönüşüm fonksiyonları (bin, hex)** kullanılmadan,  
tamamen matematiksel işlemler ve döngüler yardımıyla taban dönüşümleri gerçekleştirilmiştir.

---

##  Kullanılan Teknolojiler
- **Programlama Dili:** Python  
- **Harici Kütüphane:** Yok  
- Python’un standart giriş/çıkış yapıları ve döngü mekanizmaları kullanılmıştır.

---

##  Programın Çalışma Mantığı

1. Kullanıcıdan onluk tabanda pozitif bir sayı alınır.
2. Kullanıcıya bir menü sunulur:
   - İkilik (Binary) dönüşüm
   - Onaltılık (Hexadecimal) dönüşüm
3. Seçime göre ilgili dönüşüm fonksiyonu çalıştırılır.
4. Dönüşüm sonucu ekrana yazdırılır.
5. Sayının ikilik gösterimi kullanılarak 8-bitlik bellek görünümü oluşturulur.

---

##  Algoritma Açıklaması

###  Onluktan İkiliğe Dönüşüm
- Sayı 2’ye bölünür.
- Kalanlar kaydedilir.
- Bölüm 0 olana kadar işlem devam eder.
- Kalanlar tersten okunarak ikilik sayı elde edilir.

###  Onluktan Onaltılığa Dönüşüm
- Sayı 16’ya bölünür.
- Kalanlar 0–9 ve A–F karakterleriyle eşleştirilir.
- Bölüm 0 olana kadar işleme devam edilir.
- Kalanlar tersten birleştirilir.

###  Bellek (8-bit) Gösterimi
- İkilik sayı 8 bitin katı olacak şekilde başına 0 eklenerek tamamlanır.
- Her 8 bitlik grup, bellekte bir byte’ı temsil edecek şekilde ekrana yazdırılır.

---

##  Programın Çalıştırılması

1. Python yüklü bir ortamda proje klasörü açılır.
2. Aşağıdaki komut çalıştırılır:
   ```bash
   python proje1.py
