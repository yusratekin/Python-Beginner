""""
***************
vize ve final notunu heaplama
***************

"""
vize1 = int(input("Vize1:"))
vize2 = int(input("Vize2:"))
final1 = int(input("Final:"))

genel_not = vize1 * 3 / 10 + vize2 * 3 / 10 + final1 * 4 / 10

if (genel_not >= 90):
    print("AA Geçti.")
elif (genel_not >= 85):
    print("BA Geçti.")
elif (genel_not >= 80):
    print("BB Geçti.")
elif (genel_not >= 75):
    print("CB Geçti.")
elif (genel_not >= 70):
    print("CC Geçti.")
elif (genel_not >= 65):
    print("DC Geçti.")
elif (genel_not >= 60):
    print("DD Geçti.")
elif (genel_not >= 55):
    print("FD Geçti.")
elif (genel_not >= 50):
    print("Kaldı.")
else:
    print("FF")
    
