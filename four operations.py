print ("""*******************
Hesap Makinesi Pogramı

işlemler;

1. Toplama İşlemi

2.Çıkarna İşlemi

3.Çarpma İşlemi

4.Bölme İşlemi
***********************
""")
a = int(input("Birinci sayı:"))
b = int(input("İkinci sayıyı:"))

islem = input("İşlemi Giriniz:")
if islem =="1":
    print("{} ile {} in toplamı {} dir".format(a,b,a+b))

elif islem =="2":
    print("{} ile {} in farkı {} dir".format(a,b,a - b))
elif islem =="3":
    print("{} ile {} in carpımı {} dir".format(a,b,a * b))
elif islem == "4":
    print("{} ile {} in bolumu {} dir".format(a, b, a / b))

else:
    print("Geçersiz işlem.........")















