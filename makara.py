isim_lower = isim.lower()

if isim_lower == "cemre":
    st.success("SENİ ÇOOOOK SEVİYOORUMM ❤️")
    st.markdown("[🎧 Şarkıya Git](https://www.youtube.com/watch?v=rtOvBOTyX00&list=RDrtOvBOTyX00&start_radio=1)")
elif isim_lower == "mete":
    st.info("🎶 Şarkıya yönlendiriliyorsunuz...")
    st.markdown("[🎧 Şarkıya Git](https://www.youtube.com/watch?v=LU5FrAKJmYQ&list=RDLU5FrAKJmYQ&start_radio=1)")
elif isim_lower == "metehan":
    st.warning("Şarkıya Yönlen.. ahh Travmam tetiklendi ERROORR!! De..De..DEDEEM 😅")
    st.markdown("[😵‍💫 Şarkıya Git](https://www.youtube.com/watch?v=sr6w-6tBTDk&list=RDsr6w-6tBTDk&start_radio=1)")
elif isim_lower == "batu" or isim_lower == "batuhan":
    st.warning("Şarkıya gitmek için linke tıklayınız.")
    st.markdown("[💛💙 Şarkıya Git](https://www.youtube.com/watch?v=NJ2TkBrWA04&list=RDNJ2TkBrWA04&start_radio=1)")
else:
    st.error("İsminize göre şarkı bulunamadı :(")




