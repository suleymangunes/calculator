import math

def sayi_al(mesaj):
    while True:
        try:
            return float(input(mesaj))
        except ValueError:
            print("Hata: Lütfen geçerli bir sayı girin!")

while True:
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")
    print("5. Kare Al")
    print("6. Karekök Al")

    secim = input("Bir işlem seçin: ")
    
    # eğer kullanıcı 1 e basarsa iki sayi alınır
    # bu iki sayı toplanır ve konsolda yazdırılır
    if secim == "1":
        sayi1 = sayi_al("Birinci sayıyı girin: ")
        sayi2 = sayi_al("İkinci sayıyı girin: ")
        print("Sonuç:", sayi1 + sayi2)
    elif secim == "2":
        sayi1 = sayi_al("Birinci sayıyı girin: ")
        sayi2 = sayi_al("İkinci sayıyı girin: ")
        print("Sonuç:", sayi1 - sayi2)
    elif secim == "3":
        sayi1 = sayi_al("Birinci sayıyı girin: ")
        sayi2 = sayi_al("İkinci sayıyı girin: ")
        print("Sonuç:", sayi1 * sayi2)
    elif secim == "4":
        sayi1 = sayi_al("Birinci sayıyı girin: ")
        sayi2 = sayi_al("İkinci sayıyı girin: ")
        print("Sonuç:", sayi1 / sayi2)
    elif secim == "5":
        sayi1 = sayi_al("Sayıyı girin: ")
        print("Sonuç", sayi1 * sayi1)
    elif secim == "6":
        sayi1 = sayi_al("Sayıyı girin: ")
        print("Sonuç", math.sqrt(sayi1))
    else:
        print("Lütfen geçerli bir seçim yapın.(1-4)")



