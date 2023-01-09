
import streamlit as st

col1,col2,col3=st.columns(3)

with col1:
    a=st.selectbox("Kullanacağınız ürünü seçiniz...",["Un","Yağ","Şeker"])
with col2:
    b=st.number_input("Kaç CUP kullanacaksınız?")
with col3:
    if a=="Un":
        sonuccup=(b*140)
        sonuctablespoon=(b*8.75)
    elif a=="Yağ":
        sonuccup=(b*225)
        sonuctablespoon=(b*15)

    elif a=="Şeker":
        sonuccup=(b*200),
        sonuctablespoon=(b*5)


    c=st.header("Kullanmanız gereken :"+format(sonuccup) +"GRAM")
    d=st.subheader("Veya :"+format(sonuctablespoon) +"YEMEK KAŞIĞI")