import random

karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sayi = int(input ("kaç karakter istiyorsunuz?"))
parola=""
for i in range(sayi):
    parola+=random.choice(karakter)
print("oluşturulan parola", parola)
