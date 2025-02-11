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
    print("7. Logaritma (e tabanında)")

    secim = input("Bir işlem seçin: ")
    
    # eğer kullanıcı 1 e basarsa iki sayi alınır
    # bu iki sayı toplanır ve konsolda yazdırılır
    if secim == "1":
        sayi1 = sayi_al("Birinci sayıyı girin: ")
        sayi2 = sayi_al("İkinci sayıyı girin: ")
        print("Sonuç:", sayi1 + sayi2)
    # eğer kullanıcı 2 ye basarsa iki sayı alınır
    # birinci sayıdan ikinci sayı çıkarılır ve konsolda yazdırılır
    elif secim == "2":
        sayi1 = sayi_al("Birinci sayıyı girin: ")
        sayi2 = sayi_al("İkinci sayıyı girin: ")
        print("Sonuç:", sayi1 - sayi2)
    # eğer kullanici 3 e basarsa iki sayı alinir
    # bu iki sayi carpilir ve konsola yazdirilir
    elif secim == "3":
        sayi1 = sayi_al("Birinci sayıyı girin: ")
        sayi2 = sayi_al("İkinci sayıyı girin: ")
        print("Sonuç:", sayi1 * sayi2)
    # eğer kullanici 4 e basarsa iki sayi alinir
    # ilk sayı ikinci sayıya bölünür ve konsolda yazdirilir
    elif secim == "4":
        sayi1 = sayi_al("Birinci sayıyı girin: ")
        sayi2 = sayi_al("İkinci sayıyı girin: ")
        print("Sonuç:", sayi1 / sayi2)
    # eğer kullanici 5 e basarsa bir sayi alinir
    # bu sayinin karesi alınır ve konsolda yazdırılır
    elif secim == "5":
        sayi1 = sayi_al("Sayıyı girin: ")
        print("Sonuç", sayi1 * sayi1)
    # eğer kullanici 6 ya basarsa bir sayi alinir
    # bu sayinin kareköku alinir ve konsolda yazdirilir
    elif secim == "6":
        sayi1 = sayi_al("Sayıyı girin: ")
        print("Sonuç", math.sqrt(sayi1))
    elif secim == "7":
        sayi1 = sayi_al("Sayıyı girin: ")
        print("Sonuç", math.log(sayi1))
    else:
        print("Lütfen geçerli bir seçim yapın.(1-4)")



