import pyautogui
import time

print("""   __ _                 _             _     _      
  / _| |               | |           | |   | |     
 | |_| | ___   ___   __| |  ___  __ _| | __| |_ __ 
 |  _| |/ _ \ / _ \ / _` | / __|/ _` | |/ _` | '__|
 | | | | (_) | (_) | (_| | \__ \ (_| | | (_| | |   
 |_| |_|\___/ \___/ \__,_| |___/\__,_|_|\__,_|_|   
                                                  """)

print("developer = Ahmet Parmaksızoğlu")
print("https://github.com/ahmetpar1")

d0 = str(input("SALDIRIDA KULLANILACAK KELİMEYİ GİRİN >>> "))
d1 = int(input("KAÇTANE KELİME GÖNDERSİN >>> "))
d2 = -1
print("5 saniye sonra başlıycak")
time.sleep(5)

while(True):
    d2 += 1
    if d2 != d1:
        pyautogui.typewrite(d0)
        pyautogui.press('enter')

    else:
        quit()
