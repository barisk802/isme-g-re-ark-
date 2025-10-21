import streamlit as st

st.title("🎵 İsmine Göre Hangi Şarkısın?")

# Kullanıcıdan isim al
isim = st.text_input("Lütfen İsminizi Giriniz:")

# İsimleri küçük harfe çevirerek karşılaştırma yap
isim_lower = isim.lower()

# İsim-şarkı-veri sözlüğü
sarkilar = {
    "cemre": {
        "mesaj": "SENİ ÇOOOOK SEVİYOORUMM ❤️",
        "link": "https://www.youtube.com/watch?v=rtOvBOTyX00&list=RDrtOvBOTyX00&start_radio=1",
        "seviyemi": st.success
    },
    "mete": {
        "mesaj": "🎶 Şarkıya yönlendiriliyorsunuz...",
        "link": "https://www.youtube.com/watch?v=LU5FrAKJmYQ&list=RDLU5FrAKJmYQ&start_radio=1",
        "seviyemi": st.info
    },
    "metehan": {
        "mesaj": "Şarkıya Yönlen.. ahh Travmam tetiklendi ERROORR!! De..De..DEDEEM 😅",
        "link": "https://www.youtube.com/watch?v=sr6w-6tBTDk&list=RDsr6w-6tBTDk&start_radio=1",
        "seviyemi": st.warning
    },
    "batu": {
        "mesaj": "Şarkıya gitmek için linke tıklayınız.",
        "link": "https://www.youtube.com/watch?v=NJ2TkBrWA04&list=RDNJ2TkBrWA04&start_radio=1",
        "seviyemi": st.warning
    },
    "batuhan": {
        "mesaj": "Şarkıya gitmek için linke tıklayınız.",
        "link": "https://www.youtube.com/watch?v=NJ2TkBrWA04&list=RDNJ2TkBrWA04&start_radio=1",
        "seviyemi": st.warning
    }
}

# Buton tıklanınca çalışacak kısım
if st.button("Şarkıyı Bul"):
    if isim_lower in sarkilar:
        data = sarkilar[isim_lower]
        data["seviyemi"](data["mesaj"])  # st.success / st.info / st.warning
        st.markdown(f"[🎧 Şarkıya Git]({data['link']})")
    else:
        st.error("İsminize göre şarkı bulunamadı :(")



