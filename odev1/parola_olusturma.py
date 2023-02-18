turkce_karakter="ÇĞİÖŞÜçğıöşü"
rakam="0123456789"
buyuk_harfler="ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ"
kucuk_harfler="abcçdefgğhıijklmnoöpqrsştuüvwxyz"
while True:
    girdi = input("sifrenizi giriniz:")
    sayac = len(girdi)
    kontrol = True

    if 7 <= sayac <= 11:
        for i in range(0, 10):
            if girdi.startswith(str(i)) or girdi.endswith(str(i)):
                kontrol =False
        if kontrol ==False:
            print("sifreniz sayi ile baslayip sayi ile bitemeyeceği icin gecersizdir.")
            continue

        for i in girdi:
            if girdi.count(i) > 1:
                kontrol = False
        if kontrol == False:
            print("sifre icinde tekrarlayan karakter bulunmamalidir.")
            continue

        for i in girdi:
            if girdi.count(" ") > 0:
                kontrol = False
        if kontrol == False:
            print("sifre icinde bosluk karakteri bulunmamalidir.")
            continue

        girdi.islower()
        if girdi.islower() ==True:
            print("sifrenizde en az 1 adet buyuk harf bulunmalidir.")
            continue

        girdi.isupper()
        if girdi.isupper() ==True:
            print("sifrenizde en az 1 adet kucuk harf bulunmalidir.")
            continue

        girdi.isalnum()
        if girdi.isalnum() ==True:
            print("sifrenizde en az 1 adet alfanumerik olmayan karakter bulunmalidir.")
            continue

        for harf in girdi:
            if harf in turkce_karakter:
                kontrol =False
        if kontrol ==False:
            print("sifrenizde turkce karakter bulunmamalidir.")
            continue

        for karakter in girdi:
            if karakter in rakam:
                kontrol =False
        if kontrol ==True:
            print("sifrenizde en az 1 adet sayi bulunmalidir.")
            continue

        print("sifreniz basari ile olusturuldu.")
        exit()
    else:
        print("olusturacaginiz sifre en az 8 en fazla 12 karakterden olusmalidir.")
        continue
