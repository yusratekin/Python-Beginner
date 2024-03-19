print("""********************
faktöriyel bulma

çıkmak için q'ya basın
**********************""")

sayı = int(input("Sayı:"))

i = 1
toplam = 0
while (i < sayı):
    if (sayı % i == 0):
        toplam += i
    i += 1

if (toplam == sayı):
    print(sayı, "mükemmel bir sayıdır.")
else:
    print(sayı, "mükemmel bir sayı değildir.")



sayı = input("Sayı:")
basamak_sayisi = len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0

gecici_sayi = sayı

while (gecici_sayi > 0):
    
    basamak = gecici_sayi % 10
    
    toplam += basamak ** basamak_sayisi
    
    gecici_sayi //= 10
    
if (toplam == sayı):
    print(sayı,"bir armstrong sayısısdır.")
else:
    print(sayı,"bir armstrong sayısı değildir.")
    





for i in range(1,11):
    print("************************")
    for j in range(1,11):

        print("{} x {} = {}".format(i,j,i*j))
        


toplam = 0

while True:

    sayı = input("Sayı:")

    if (sayı== "q"):
        break
    sayı = int(sayı)

    toplam += sayı

print("Girdiğiniz Sayıların Toplamı:",toplam)





