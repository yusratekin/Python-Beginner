import random
import time
rastgele_sayi = random.randint(1,40)
tahmin_hakki = 7
while True:
    
    tahmin = int(input("Tahmininiz: "))
    
    if(tahmin < rastgele_sayi):
        print("Bilgiler Sorgulanıyor....")
        time.sleep(1)
        
        
        print("Daha büyük bir sayı söyleyiniz....")
        
        tahmin_hakki -= 1
    elif (tahmin > rastgele_sayi):
        print("Bilgiler Sorgulanıyor.....")
        time.sleep(1)
        
        print("Daha düşük bir sayı söyleyiniz....")
            
        tahmin_hakki -= 1
    else:
        print("Bilgiler Sorgulanıyor....")
        time.sleep(1)
        print("Tebrikler!  Sayınız",rastgele_sayi)
        break
    if(tahmin_hakki == 0):
        print("Tahmin hakkınız biti....")
        print("Sayınız:" , rastgele_sayi)
        break