from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import random
import string
import qrcode
from io import BytesIO

app = FastAPI()

# --- 1. ANA SAYFA ---
@app.get("/")
def ana_sayfa():
    return {"mesaj": "Gelişmiş API'ye Hoş Geldiniz! /docs adresine gidin."}

# --- 2. ŞİFRE ÜRETİCİ (Eski Özellik) ---
@app.get("/generate")
def sifre_uret(uzunluk: int = 12, rakam_var_mi: bool = True, sembol_var_mi: bool = True):
    karakterler = string.ascii_letters 
    if rakam_var_mi:
        karakterler += string.digits
    if sembol_var_mi:
        karakterler += "!@#$%^&*()_+"
        
    sifre = "".join(random.choice(karakterler) for _ in range(uzunluk))
    
    return {
        "sifre": sifre,
        "uzunluk": uzunluk,
        "guvenlik": "Cok Yuksek"
    }

# --- 3. QR KOD ÜRETİCİ (YENİ ÖZELLİK!) ---
@app.get("/qrcode")
def qr_uret(metin: str = "https://google.com"):
    """
    Verilen metni QR Koda dönüştürür ve RESİM olarak döner.
    """
    # 1. QR Kodu oluştur
    img = qrcode.make(metin)
    
    # 2. Resmi bir dosya gibi hafızaya kaydet (Diske değil, RAM'e)
    buffer = BytesIO()
    img.save(buffer)
    buffer.seek(0)
    
    # 3. Resmi cevap olarak fırlat
    return StreamingResponse(buffer, media_type="image/png")