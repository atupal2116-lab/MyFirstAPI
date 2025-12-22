from fastapi import FastAPI
import random
import string

# Fabrikamızın tabelasını asıyoruz
app = FastAPI()

# 1. Karşılama Kapısı (Ana Sayfa)
@app.get("/")
def ana_sayfa():
    return {"mesaj": "Şifre Üretici API'sine Hoş Geldiniz! /docs adresine giderek deneyin."}

# 2. Üretim Hattı (Şifre Yapan Makine)
@app.get("/generate")
def sifre_uret(uzunluk: int = 12, rakam_var_mi: bool = True, sembol_var_mi: bool = True):
    """
    Bu fonksiyon isteğe göre güçlü bir şifre üretir.
    """
    
    # Harfleri al (a-z, A-Z)
    karakterler = string.ascii_letters 
    
    if rakam_var_mi:
        karakterler += string.digits  # 0-9 ekle
        
    if sembol_var_mi:
        karakterler += "!@#$%^&*()_+"  # Sembolleri ekle
        
    # Karıştır ve seç
    sifre = "".join(random.choice(karakterler) for _ in range(uzunluk))
    
    # Paketi teslim et
    return {
        "sifre": sifre,
        "uzunluk": uzunluk,
        "guvenlik": "Cok Yuksek"
    }