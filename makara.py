import streamlit as st
import webbrowser

st.title("🎵 İsmine Göre Hangi Şarkısın")

isim = st.text_input("Lütfen İsminizi Giriniz:")

if st.button("Şarkıyı Bul"):
    if isim == "Cemre":
        st.info("Şarkıya yönlendiriliyorsunuz... (SENİ ÇOOOOK SEVİYOORUMM 💖)")
        webbrowser.open("https://www.youtube.com/watch?v=rtOvBOTyX00&list=RDrtOvBOTyX00&start_radio=1")
    elif isim == "Mete":
        st.info("Şarkıya yönlendiriliyorsunuz...")
        webbrowser.open("https://www.youtube.com/watch?v=LU5FrAKJmYQ&list=RDLU5FrAKJmYQ&start_radio=1")
    elif isim == "Metehan":
        st.warning("Şarkıya yönlen... ahh Travmam tetiklendi ERROORR!! De..De..DEDEEM 😵‍💫")
        webbrowser.open("https://www.youtube.com/watch?v=sr6w-6tBTDk&list=RDsr6w-6tBTDk&start_radio=1")
    else:
        st.error("İsminize göre şarkı bulunamadı 😔")
