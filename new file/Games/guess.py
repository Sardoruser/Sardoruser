import random


Tahminlar = 0
guess = 0

ism = input("Salom, 'Guess Game'ga Xush kelibsiz!Iltimos, o'yinni boshlash uchun ismingizni kiriting: ")
print("\nSalom, "+ism+"! Men hozir 1️⃣ dan 💯 gacha bulgan raqamlardan birini o'ylayman.\nSizda 🔟 ta urinishingiz buladi men o'ylagan raqamni topish uchun.👈")

raqam = random.randint(1, 100)

while Tahminlar < 10:
    if ism == "PASSWORD":#You can set your password here if you want
        print(raqam)
        
    guess = int(input("Tahmin qiling(Yoki 'stop' deb yozing): "))
    if guess == "stop":
            break
        
    if guess == 'PASSWORD':
        print("Oh,PASSWORD, here is number: "+str(raqam))
        break    
    
    try:
        guess = int(guess)
    except ValueError:
        print("Noto'g'ri kiritim. Iltimos raqam yoki 'stop' deb kiriting.")
        continue
    
    if guess == raqam:
        break
    
    Tahminlar = Tahminlar + 1
    
    if guess < raqam:
        if raqam - guess <= 2:
            print("Sizning tahminingiz o'zroq kichik.😯")
        elif raqam - guess <= 5:
            print("Sizning tahminingiz kichik.😐")
        else:
            print("Sizning tahminingiz juda kichik.")

    if guess > raqam:
        if guess - raqam <= 2:
            print("Sizning tahminingiz o'zroq katta.😯")
        elif guess - raqam <= 5:
            print("Sizning tahminingiz katta.😐")
        else:
            print("Sizning tahminingiz juda katta.")

if guess == raqam:
    Tahminlar = str(Tahminlar)
    print("Ajoyib, " + ism + "! Siz men o'ylagan raqamni " + Tahminlar + " urinishda topdingiz.🤩")

if guess != raqam:
    raqam = str(raqam)    
    print("Afsus, Men o'ylagan raqam " + raqam + " edi.😢")