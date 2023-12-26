'''
● Terazinin sağ ve sol kefesinde yük olmadan başlanacak.
● Ağırlık yerleştirmeye sol kefeden başlanacak.
● Her defasında rastgele bir ağırlık (0-50 aralığında) üretilecek ve hafif tarafa konulacak.
● Hafif taraf daha ağır olduğu anda denge yönü değişecek.
● Denge yönü 10 defa değişinceye kadar kefe ağırlıklarının değişimlerini ekrana yazınız?
'''

import random

left_pan = 0
right_pan = int(random.random() * 50)

for i in range(10):
    if left_pan > right_pan:
        right_pan += int(random.random() * 50)
    else:
        left_pan += int(random.random() * 50)
    if left_pan > right_pan:
        conclusion = "Sol"
    elif left_pan < right_pan:
        conclusion = "Sag"
    else:
        conclusion = "Denge"


    print(f"{i + 1}. tur: Sol {left_pan}, Sag {right_pan}")


print(f"Son durum: {conclusion}")






