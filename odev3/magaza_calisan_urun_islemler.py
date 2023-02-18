personel = []
urun = {}
per_id = 101


def per_bilgi_al():  # personel bilgisi almak için
    global personel
    global per_id
    syc = int(input("Personel sayısı giriniz:"))
    print(end="\n")
    for i in range(syc):
        personel.append(list())  # liste içinde liste oluşturarak personel bilgisi girmek için
        personel[i].append(per_id + i)
        ad = input("Personelin Adı:")
        personel[i].append(ad)
        soyad = input("Personelin Soyadı:")
        personel[i].append(soyad)
        cocuk_sayisi = int(input("Çocuk Sayısı:"))
        personel[i].append(cocuk_sayisi)
        maas = int(input("Maaşı:"))
        personel[i].append(maas)
        print(end="\n")

def urun_bilgi_al():  #ürün bilgisi almak için
    global urun
    syc = int(input("Ürün sayısı giriniz:"))
    print(end="\n")
    for i in range(1, syc+1):
        sozluk = dict()
        urun_ad = input("Ürün Adı:")
        sozluk["Urun_Adi"] = urun_ad
        marka = input("Ürün Markası:")
        sozluk["Urun_Markasi"] = marka
        urun_adeti = int(input("Ürün Adeti:"))
        sozluk["Urun_Adeti"] = urun_adeti
        urun_fiyat = int(input("Ürün Fiyatı:"))
        sozluk["Urun_Fiyati"] = urun_fiyat
        urun[i] = sozluk
        print(end="\n")

def bilgi_ekle():
    def per_bilgi_ekle():
        global personel
        global per_id
        sayac = 0

        for i in range(len(personel)):
            sayac += 1
        syc = int(input("Eklemek istediğiniz personel sayısını giriniz:"))

        for i in range(sayac, sayac+syc):
            print(end="\n")
            personel.append(list())         #liste içinde liste oluşturarak personel bilgisi eklemek için
            personel[i].append(per_id+i)
            ad = input("Personel Adı:")
            personel[i].append(ad)
            soyad = input("Personelin Soyadı:")
            personel[i].append(soyad)
            cocuk_sayisi = int(input("Çocuk Sayısı:"))
            personel[i].append(cocuk_sayisi)
            maas = int(input("Maaşı:"))
            personel[i].append(maas)

    def urun_bilgi_ekle():
        global urun
        sayac = 0
        for i in range(len(urun)):
            sayac += 1
        syc = int(input("Eklemek istediğiniz ürün sayısı giriniz:"))
        print(end="\n")
        for i in range(1, syc+1):
            sozluk = dict()             #sözlük içinde sözlük oluşturarak ürün bilgisi eklemek için
            urun_ad = input("Ürün Adı:")
            sozluk["Urun_Adi"] = urun_ad
            marka = input("Ürün Markası:")
            sozluk["Urun_Markasi"] = marka
            urun_adeti = int(input("Ürün Adeti:"))
            sozluk["Urun_Adeti"] = urun_adeti
            urun_fiyat = int(input("Ürün Fiyatı:"))
            sozluk["Urun_Fiyati"] = urun_fiyat
            urun[sayac+i] = sozluk

    print(end="\n")
    while True:
        print("1:Personel Bilgisi Ekleme   2:Ürün Bilgisi Ekleme  3:Ekleme İşleminden Çıkış")
        secim2 = int(input("Seçiminizi giriniz:"))
        if secim2 == 1:
            per_bilgi_ekle()
            print(end="\n")
        elif secim2 == 2:
            urun_bilgi_ekle()
            print(end="\n")
        elif secim2 == 3:
            print(end="\n")
            break
        else:
            print("Yanlış bir seçim yaptınız.")
            print(end="\n")
            continue

def bilgi_ara():
    def per_bilgi_ara():
        global personel
        aranan = input("Aramak istediğiniz personel adını giriniz:")
        sayac = 0
        ad = []
        for i in range(len(personel)):
            if personel[i][1] == aranan:
                sayac += 1
                ad.append(personel[i])

        if sayac > 0:
            for i in range(len(ad)):
                print("Personel Id:{}    Personel Adı:{:15}  Personel Soyadı:{:15}  Çocuk Sayısı:{:2}    Maaşı:{:6}".format(
                    ad[i][0], ad[i][1], ad[i][2], ad[i][3], ad[i][4]))
        else:
                print("{} isminde bir personel yoktur.".format(aranan))

    def urun_bilgi_ara():
        global urun
        aranan = input("Aramak istediğiniz ürünün adını giriniz:")
        sayac = 0
        ad = {}
        for i in range(1, len(urun)+1):
            if urun[i]["Ürün Adı"] == aranan:
                sayac += 1
                sozluk = dict()
                sozluk["Urun_Adi"] = urun[i]["Urun_Adi"]
                sozluk["Urun_Markasi"] = urun[i]["Urun_Markasi"]
                sozluk["Urun_Adeti"] = urun[i]["Urun_Adeti"]
                sozluk["Urun_Fiyati"] = urun[i]["Urun_Fiyati"]
                ad[i] = sozluk

        if sayac > 0:
            for i in ad.keys():
                print("Ürün Numarası:{:2}    Ürün Adı:{:15}  Ürünün Markası:{:15}  Ürün Adeti:{:2}    Ürün Fiyatı:{}".format(
                    i, ad[i]["Urun_Adi"], ad[i]["Urun_Markasi"], ad[i]["Urun_Adeti"], ad[i]["Urun_Fiyati"]))
        else:
            print("Mağazada {} isminde ürün bulunmamaktadır.".format(aranan))

    print(end="\n")
    while True:
        print("1:Personel Bilgisi Arama   2:Ürün Bilgisi Arama  3:Arama İşleminden Çıkış")
        secim2 = int(input("Seçiminizi giriniz:"))
        if secim2 == 1:
            per_bilgi_ara()
            print(end="\n")
        elif secim2 == 2:
            urun_bilgi_ara()
            print(end="\n")
        elif secim2 == 3:
            print(end="\n")
            break
        else:
            print("Yanlış bir seçim yaptınız.")
            print(end="\n")
            continue

def bilgi_guncelle():
    def per_bilgi_guncelle():
        global personel
        global per_id
        print("Personel idileri 101 den başlayarak ardışık olarak artmaktadır. ")
        aranan = int(input("Bilgisini güncellemek istediğiniz personelin idisini giriniz:"))
        sayac = 0
        for i in range(len(personel)):
            if personel[i][0] == aranan:
                sayac += 1
                a = i
        if sayac > 0:
            print("1:Personel Adı  2:Personel Soyadı  3:Çocuk Sayısı  4:Maaşı   ")
            secim = int(input("Güncellemek istediğiniz bilgi için seçiminizi giriniz:"))
            if secim == 1:
                guncel_ad = input("Personelin Adı:")
                personel[a][1] = guncel_ad
            if secim == 2:
                guncel_soyad = input("Personelin Soyadı:")
                personel[a][2] = guncel_soyad
            elif secim == 3:
                guncel_cs = int(input("Personelin Çocuk Sayısı:"))
                personel[a][3] = guncel_cs
            elif secim == 4:
                guncel_maas = int(input("Personelin Maaşı:"))
                personel[a][4] = guncel_maas
            else:
                print("Yanlış bir seçim yaptınız.")
        else:
            print("Girdiğiniz personel idisi bulunmamaktadır.")

    def urun_bilgi_guncelle():
        global urun
        print("Ürün numaraları 1 den başlayarak ardışık olarak artmaktadır.")
        aranan = int(input("Güncellemek istediğiniz ürünün numarasını giriniz:"))
        sayac = 0
        for i in range(1, len(urun) + 1):
            if i == aranan:
                sayac += 1
                print("1:Ürün Adı  2:Ürünün Markası  3:Ürün Adedi  4:Ürün Fiyatı")
                secim = int(input("Güncellemek istediğiniz bilgi için seçiminizi giriniz:"))
                if secim == 1:
                    guncel_urunad = input("Ürün Adı:")
                    urun[i]["Urun_Adi"] = guncel_urunad
                elif secim == 2:
                    guncel_marka = input("Ürün Markası:")
                    urun[i]["Urun_Markasi"] = guncel_marka
                elif secim == 3:
                    guncel_adet = int(input("Ürün Adeti:"))
                    urun[i]["Urun_Adeti"] = guncel_adet
                elif secim == 4:
                    guncel_fiyat = int(input("Ürün Fiyatı:"))
                    urun[i]["Urun_Fiyati"] = guncel_fiyat
                else:
                    print("Yanlış bir seçim yaptınız.")
        if sayac == 0:
            print("Girdiğiniz ürün numarası bulunmamaktadır.")

    print(end="\n")
    while True:
        print("1:Personel Bilgisi Güncelle   2:Ürün Bilgisi Güncelle  3:Güncelleme İşleminden Çıkış")
        secim2 = int(input("Seçiminizi giriniz:"))
        if secim2 == 1:
            per_bilgi_guncelle()
            print(end="\n")
        elif secim2 == 2:
            urun_bilgi_guncelle()
            print(end="\n")
        elif secim2 == 3:
            print(end="\n")
            break
        else:
            print("Yanlış bir seçim yaptınız.")
            print(end="\n")
            continue
def bilgi_sil():
    def per_bilgi_sil():
        global personel
        print("Personel idileri 101 den başlayarak ardışık olarak artmaktadır. ")
        aranan = int(input("Bilgisini silmek istediğiniz personelin idisini giriniz:"))
        sayac = 0
        for i in range(len(personel)):
            if personel[i][0] == aranan:
                del (personel[i])
                sayac += 1
        if sayac == 0:
            print("Girdiğiniz personel idisi bulunmamaktadır.")

    def urun_bilgi_sil():
        global urun
        print("Ürün numaraları 1 den başlayarak ardışık olarak artmaktadır.")
        aranan = int(input("Silmek istediğiniz ürünün numarasını giriniz:"))
        sayac = 0
        for i in range(1, len(urun) + 1):
            if i == aranan:
                del (urun[i])
                sayac += 1
        if sayac == 0:
            print("Girdiğiniz ürün numarası bulunmamaktadır.")

    print(end="\n")
    while True:
        print("1:Personel Bilgisi Silme   2:Ürün Bilgisi Silme  3:Silme İşleminden Çıkış")
        secim2 = int(input("Seçiminizi giriniz:"))
        if secim2 == 1:
            per_bilgi_sil()
            print(end="\n")
        elif secim2 == 2:
            urun_bilgi_sil()
            print(end="\n")
        elif secim2 == 3:
            print(end="\n")
            break
        else:
            print("Yanlış bir seçim yaptınız.")
            print(end="\n")
            continue

def zam_hesapla():
    global personel
    for i in range(len(personel)):
        if 1 <= personel[i][2] < 3:
            personel[i][3] += (personel[i][2] * 100)
        elif 3 <= personel[i][2] < 5:
            personel[i][3] += (personel[i][2] * 150)
        elif 5 <= personel[i][2]:
            personel[i][3] += (personel[i][2] * 200)
        else:
            pass
def kar_hesapla():
    global urun
    kar = 0.0
    for i in range(1, len(urun)+1):
        if 50 <= urun[i]["Urun_Fiyati"] < 2000:
            kar = urun[i]["Urun_Fiyati"] * urun[i]["Urun_Adeti"] * 2 / 100
        elif 2000 <= urun[i]["Urun_Fiyati"] < 4000:
            kar = urun[i]["Urun_Fiyati"] * urun[i]["Urun_Adeti"] * 5 / 100
        elif 4000 <= urun[i]["Urun_Fiyati"] < 6000:
            kar = urun[i]["Urun_Fiyati"] * urun[i]["Urun_Adeti"] * 8 / 100
        elif 6000 <= urun[i]["Urun_Fiyati"] < 8000:
            kar = urun[i]["Urun_Fiyati"] * urun[i]["Urun_Adeti"] * 10 / 100
        elif 8000 <= urun[i]["Urun_Fiyati"] < 10000:
            kar = urun[i]["Urun_Fiyati"] * urun[i]["Urun_Adeti"] * 15 / 100
        elif 10000 <= urun[i]["Urun_Fiyati"]:
            kar = urun[i]["Urun_Fiyati"] * urun[i]["Urun_Adeti"] * 20 / 100
        else:
            pass
        print("{}. üründen elde edilen kar:{}".format(i, kar))
    print(end="\n")

def menu():
    global personel
    global urun
    per_bilgi_al()
    urun_bilgi_al()
    print(end="\n")
    print("ELEKTRONİK EŞYA MAĞAZASI")
    while True:
        print(end="\n\n")
        print("MENÜ", "-----", "1:Bilgi Ekleme", "2:Bilgi Arama", "3:Bilgi Güncelleme", "4:Bilgi Silme", "5:Zam Hesaplama", "6:Kar Hesaplama", "0:Çıkış", sep="\n")
        islem = int(input("Yapmak istediğiniz işlemi seçiniz:"))
        print(end="\n\n")
        if islem == 1:
            bilgi_ekle()
        elif islem == 2:
            bilgi_ara()
        elif islem == 3:
            bilgi_guncelle()
        elif islem == 4:
            bilgi_sil()
        elif islem == 5:
            zam_hesapla()
        elif islem == 6:
            kar_hesapla()
        elif islem == 0:
            break
        else:
            print("Yanlış işlem girdiniz.")
    print("Personel Listesi")
    print()
    for i in range(len(personel)):
        print("Personel Id:{}    Personel Adı:{:15}  Personel Soyadı:{:15}  Çocuk Sayısı:{:2}    Maaşı:{:6} ".format(
            personel[i][0], personel[i][1], personel[i][2], personel[i][3], personel[i][4]))

    print(end="\n\n")
    print("Ürün Listesi")
    print()
    for urun_nu in urun.keys():
        print("Ürün Numarası:{:3}    Ürün Adı:{:15}  Ürünün Markası:{:15}  Ürün Adeti:{:4}    Ürün Fiyatı{}".format(
            urun_nu, urun[urun_nu]["Urun_Adi"], urun[urun_nu]["Urun_Markasi"], urun[urun_nu]["Urun_Adeti"],
            urun[urun_nu]["Urun_Fiyati"]))

    dosya1 = open("19010011020.txt", "w")
    print("Personel Listesi", file=dosya1)
    for i in range(len(personel)):
        print(personel[i][0], file=dosya1, end="   ")
        print(personel[i][1], file=dosya1, end="   ")
        print(personel[i][2], file=dosya1, end="   ")
        print(personel[i][3], file=dosya1, end="   ")
        print(personel[i][4], file=dosya1)
    print(file=dosya1)
    print("Urun Listesi", file=dosya1)
    for urun_nu in urun.keys():
        print(urun_nu, file=dosya1, end="   ")
        print(urun[urun_nu]["Urun_Adi"], file=dosya1, end="   ")
        print(urun[urun_nu]["Urun_Markasi"], file=dosya1, end="   ")
        print(urun[urun_nu]["Urun_Adeti"], file=dosya1, end="   ")
        print(urun[urun_nu]["Urun_Fiyati"], file=dosya1)
    dosya1.close()
menu()

