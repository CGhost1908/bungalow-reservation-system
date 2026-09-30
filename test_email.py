#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load environment variables
load_dotenv()

EMAIL_SENDER = os.environ.get('EMAIL_SENDER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL')

print("=" * 60)
print("📧 EMAIL KONFIGÜRASYON TESTİ")
print("=" * 60)

# Check configuration
print(f"\n1️⃣  Konfigürasyon Kontrol:")
print(f"   EMAIL_SENDER: {EMAIL_SENDER}")
print(f"   EMAIL_PASSWORD: {'*' * 10}... (gizli)")
print(f"   ADMIN_EMAIL: {ADMIN_EMAIL}")

if not EMAIL_SENDER or not EMAIL_PASSWORD or not ADMIN_EMAIL:
    print("\n❌ HATA: Email konfigürasyonu eksik!")
    print("   Lütfen .env dosyasını kontrol edin.")
    exit(1)

print(f"\n2️⃣  Gmail SMTP Bağlantısı Test:")
try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    print("   ✅ SMTP sunucusuna bağlandı")
    
    server.starttls()
    print("   ✅ TLS güvenliği başlatıldı")
    
    server.login(EMAIL_SENDER, EMAIL_PASSWORD)
    print("   ✅ Gmail'e giriş yapıldı")
    
    server.quit()
    print("\n✅ BAŞARILI! Email sistem çalışıyor.")
    
except smtplib.SMTPAuthenticationError:
    print("   ❌ Kimlik doğrulaması başarısız!")
    print("\n   🔧 Çözümler:")
    print("   1. Gmail'de 2-Faktörlü Kimlik Doğrulamayı aç")
    print("   2. https://myaccount.google.com/apppasswords'ten App Password oluştur")
    print("   3. .env dosyasında EMAIL_PASSWORD olarak kopyala")
    exit(1)
    
except Exception as e:
    print(f"   ❌ Bağlantı hatası: {str(e)}")
    print("\n   🔧 Kontrol Et:")
    print("   1. İnternet bağlantısı var mı?")
    print("   2. Firewall/Antivirus SMTP 587 portunu engelliyor mu?")
    print("   3. Gmail hesabı doğru mu?")
    exit(1)

print("\n" + "=" * 60)
