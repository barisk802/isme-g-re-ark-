import webbrowser

print("""
İsmine Göre Hangi Şarkısın
""")

while True:
    işlem=input("Lütfen İsminizi Giriniz :")

    if işlem=="Cemre":
        print("Şarkıya Yönlendiriliyorsunuz Lütfen Bekleyiniz...(SENİ ÇOOOOK SEVİYOORUMM)")
        webbrowser.open("https://www.youtube.com/watch?v=rtOvBOTyX00&list=RDrtOvBOTyX00&start_radio=1")
    elif işlem=="Mete":
        print("Şarkıya Yönlendiriliyorsunuz Lütfen Bekleyiniz...")
        webbrowser.open("https://www.youtube.com/watch?v=LU5FrAKJmYQ&list=RDLU5FrAKJmYQ&start_radio=1")
    elif işlem=="Metehan":
        print("Şarkıya Yönlen.. ahh Travmam tetiklendi ERROORR!! De..De..DEDEEM")
        webbrowser.open("https://www.youtube.com/watch?v=sr6w-6tBTDk&list=RDsr6w-6tBTDk&start_radio=1")

    else:
        print("İsminize göre şarkı bulunamadı :(")
        break