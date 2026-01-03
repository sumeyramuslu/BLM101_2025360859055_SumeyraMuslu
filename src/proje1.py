# Çok Fonksiyonlu Taban Dönüştürücü
# Bu program onluk tabandaki sayıları ikilik veya onaltılık tabana çevirir
# ve bellekteki 8-bitlik görünümünü gösterir.
# Hazır Python fonksiyonları (bin, hex) kullanılmamıştır.


def onluktan_ikilige(sayi):
    # Bu fonksiyon, verilen onluk sayıyı ikilik tabana çevirir
    if sayi == 0:
        return "0"

    ikilik = ""

    # Sayı 2'ye bölünerek kalanlar tersten birleştirilir
    while sayi > 0:
        kalan = sayi % 2
        ikilik = str(kalan) + ikilik
        sayi //= 2

    return ikilik


def onluktan_onaltiliga(sayi):
    # Bu fonksiyon, verilen onluk sayıyı onaltılık tabana çevirir
    if sayi == 0:
        return "0"

    rakamlar = "0123456789ABCDEF"
    onaltilik = ""

    # Sayı 16'ya bölünerek kalanlar harf karşılığı ile birleştirilir
    while sayi > 0:
        kalan = sayi % 16
        onaltilik = rakamlar[kalan] + onaltilik
        sayi //= 16

    return onaltilik


def bellek_gorunumu_yazdir(ikilik_dizisi):
    # Bu fonksiyon, sayının bellekteki 8-bitlik kutucuklar halinde görünümünü yazdırır

    # İkilik gösterim 8 bitin katı olacak şekilde başına 0 eklenir
    if len(ikilik_dizisi) % 8 != 0:
        eksik = 8 - (len(ikilik_dizisi) % 8)
        ikilik_dizisi = ("0" * eksik) + ikilik_dizisi

    print("\n--- Bellek Görünümü (8-bitlik Kutucuklar) ---")
    for i in range(0, len(ikilik_dizisi), 8):
        parca = ikilik_dizisi[i:i+8]
        print("| " + " | ".join(parca) + " |")


def ana_menu():
    # Programın ana çalışma fonksiyonu

    print("--- Çok Fonksiyonlu Taban Dönüştürücü ---")
    onluk_sayi = int(input("Onluk tabanda pozitif bir sayı giriniz: "))

    if onluk_sayi < 0:
        print("Lütfen pozitif bir onluk sayı giriniz.")
        return

    print("\n1- İkilik (Binary) Dönüşümü")
    print("2- Onaltılık (Hexadecimal) Dönüşümü")
    secim = input("Seçiminiz: ")

    if secim == "1":
        ikilik_sonuc = onluktan_ikilige(onluk_sayi)
        print("\nİkilik Gösterim:", ikilik_sonuc)
        bellek_gorunumu_yazdir(ikilik_sonuc)

    elif secim == "2":
        onaltilik_sonuc = onluktan_onaltiliga(onluk_sayi)
        print("\nOnaltılık Gösterim:", onaltilik_sonuc)
        bellek_gorunumu_yazdir(onluktan_ikilige(onluk_sayi))

    else:
        print("Geçersiz seçim yaptınız.")


# Programı çalıştır
ana_menu()
