#1. Kullanıcıdan adını ve soyadını ayrı ayrı alıp, tam adını ekrana yazdıran program.
ad = input("Adınızı girin: ")
soyad = input("Soyadınızı girin: ")
print("Tam adınız:", tam_ad)

#2.İki sayının toplamı, farkı ve çarpımı
x = 10
y = 5
print(x + y)
print(x - y)
print(x * y)

#3.Kullanıcının yaşını alıp, 18 yaşından büyük olup olmadığını True/False olarak gösteren program
yas = input("lütfen yaşınızı girin")
sonuç = int(yas)<19
print(sonuç)

#4.Dikdörtgenin alanını ve çevresini hesaplayan program
kisa kenar = int(input("Kısa kenarı girin: "))
uzun kenar = int(input("Uzun kenarı girin: "))
alan = kisa_kenar * uzun kenar
cevre = 2 * (kisa kenar + uzun kenar)
print("Alan:", alan)
print("Çevre:", cevre)

#5. Girilen bir sayının pozitif olup olmadığını kontrol eden program.
sayi = int(input("Bir sayı girin: "))
pozitif_mi = 10 > 0
print("Sayı pozitif mi?", pozitif_mi)

#6.Kullanıcıdan bir kelime alıp kelimenin ilk 3 harfini ve son 2 harfini yazdıran program.
x = "seyma"
y = "seyma"
print(x[0:3])
print(y[-2:])

#7.İki sayının ortalamasını hesaplayıp, sonucu ondalıklı sayı olarak gösteren program.
sayi1 = int(input("sayı1"))
sayi2 = int(input("sayı2"))
sayi_1 = sayi1 * 0.4
sayi_2 = sayi2 * 0.6
ortalama = sayi_1 + sayi_2
print(ortalama)

#8.Kullanıcının girdiği iki sayının her ikisinin de çift sayı olup olmadığını kontrol eden program
sayi1 = int(input("1. sayıyı girin: "))
sayi2 = int(input("2. sayıyı girin: "))
if sayi1 % 2 == 0 or sayi2 % 2 == 0
print("Her iki sayı da çift mi?", sonuç)

#9.Girilen bir metnin uzunluğunu ve büyük harfe çevrilmiş halini ekrana yazdıran program
metin = input("Bir metin girin: ")
uzunluk = len(metin)
buyuk_harf = metin.upper()
print("Metnin uzunluğu:", uzunluk)
print("Büyük harf hali:", buyuk_harf)

#10.Dairenin alanını hesaplayan program (pi = 3.14)
pi = 3.14
yaricap = int(input("Dairenin yarıçapını girin: "))
alan = pi * (yaricap ** 2)
print("Dairenin alanı:", alan)

#11.İki sayının eşit olup olmadığını ve birincinin ikinciden büyük olup olmadığını gösteren program
sayi1 = int(input("1. sayıyı girin: "))
sayi2 = int(input("2. sayıyı girin: "))
esit_mi = (sayi1 == sayi2)
birinci_buyuk_mu = (sayi1 > sayi2)
print("İki sayı eşit mi?", esit_mi)
print("Birinci sayı ikinciden büyük mü?", birinci_buyuk_mu)

#12.Bir sayının hem 3’e hem de 5’e tam bölünüp bölünmediğini kontrol eden program
sayi = int(input("Bir sayı girin: "))
a = (sayi % 3 == 0) and (sayi % 5 == 0)
print("Sayı hem 3'e hem de 5'e tam bölünüyor mu?", a)


