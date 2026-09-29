# Email Setup Guide - Bungalow Reservation System

## 📧 Email Notification System

Sistem, yeni rezervasyonlar geldiğinde admin'e email gönderir ve onay/reddedilme durumunda müşteriyi emaille bilgilendirir.

## 🔧 Kurulum Adımları

### 1. Gmail Hesabı Hazırlama

**Adım 1: Gmail'de 2-Faktörlü Kimlik Doğrulamayı Etkinleştirin**
- Google hesabınıza giriş yapın: https://myaccount.google.com/
- Sol menüden "Güvenlik" seçeneğine tıklayın
- "2-Adımlı Doğrulamayı" etkinleştirin (telefon numarası gereklidir)

**Adım 2: App Password Oluşturun**
- https://myaccount.google.com/apppasswords adresine gidin
- Uygulamayı seçin: "Mail"
- Cihazı seçin: "Windows Bilgisayar" (veya sizin cihazınız)
- 16 karakterlik bir şifre oluşturulacak, bu şifreyi kopyalayın

### 2. Çevresel Değişkenleri Ayarlama

#### Windows PowerShell Yöntemi

```powershell
# Ortam değişkenlerini ayarla
[System.Environment]::SetEnvironmentVariable("EMAIL_SENDER", "your-email@gmail.com", [System.EnvironmentVariableTarget]::User)
[System.Environment]::SetEnvironmentVariable("EMAIL_PASSWORD", "your-app-password-16-chars", [System.EnvironmentVariableTarget]::User)
[System.Environment]::SetEnvironmentVariable("ADMIN_EMAIL", "admin@bungalow.com", [System.EnvironmentVariableTarget]::User)

# Sonra PowerShell'i yeniden başlat
```

#### .env Dosyası Yöntemi (Daha Kolay)

1. Proje klasöründe `.env` dosyası oluşturun:

```bash
EMAIL_SENDER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password-16-chars
ADMIN_EMAIL=admin@bungalow.com
```

2. Python'da okumak için `python-dotenv` yükleyin:

```bash
pip install python-dotenv
```

3. `app.py`'nin başına şunu ekleyin:

```python
from dotenv import load_dotenv
load_dotenv()
```

### 3. Test Etme

```python
# app.py'nin sonunda test kodu çalıştırabilirsiniz
if __name__ == '__main__':
    # Test email gönderme
    test_reservation = {
        'name': 'Test Kullanıcı',
        'email': 'test@example.com',
        'phone': '5551234567',
        'checkIn': '2024-12-25',
        'checkOut': '2024-12-27',
        'guests': '2',
        'bungalow': 'Akasya',
        'notes': 'Test rezervasyonu'
    }
    
    send_admin_reservation_notification(test_reservation)
    app.run(debug=True)
```

## 📧 Email Şablonları

### Admin'e Gelen Email
- **Başlık**: 🔔 Yeni Rezervasyon: [Misafir Adı]
- **İçerik**: 
  - Misafir bilgileri (Ad, Email, Telefon)
  - Rezervasyon detayları (Tarih, Bungalov, Gece Sayısı)
  - Admin paneline onay/reddetme linki

### Müşteriye Gelen Email (Onaylandığında)
- **Başlık**: ✅ Rezervasyonunuz Onaylandı!
- **İçerik**:
  - Onay bilgisi
  - Rezervasyon detayları
  - İletişim bilgileri

### Müşteriye Gelen Email (Reddedildiğinde)
- **Başlık**: ❌ Rezervasyonunuz Reddedildi
- **İçerik**:
  - Reddedilme bilgisi
  - Yeniden deneme önerisi
  - İletişim bilgileri

## 🔒 Güvenlik Notları

⚠️ **ÖNEMLİ:**
- `.env` dosyasını **asla** GitHub'a commit etmeyin
- `.gitignore`'a `.env` ekleyin
- App Password'ü kimseyle paylaşmayın
- Production'da daha güvenli bir email hizmeti kullanın (SendGrid, Mailgun, vb.)

## 🐛 Sorun Giderme

### "SMTPAuthenticationError" hatası
- App Password'ün doğru olduğundan emin olun
- Gmail'de 2-faktörlü kimlik doğrulamayı kontrol edin
- Hesabın "Düşük güvenlik uygulamalarına izin ver" seçeneğini kontrol edin

### Email gönderilmiyor
- İnternet bağlantınızı kontrol edin
- Firewall/Antivirus ayarlarını kontrol edin
- Gmail logs: https://myaccount.google.com/security-checkup

### "Connection refused" hatası
- SMTP_SERVER ve SMTP_PORT ayarlarını kontrol edin
- Bazı ağlar SMTP port 587'yi engelleyebilir, port 465'i deneyin

## 📝 Gelecek İyileştirmeler

- [ ] Email şablonlarını özelleştirilebilir hale getir
- [ ] HTML yerine Markdown email şablonları
- [ ] Email gönderme başarısız olsa da form submit edilebilir
- [ ] Batch email gönderimi (toplu mesajlar)
- [ ] Email gönderme logları
- [ ] WhatsApp notification desteği

## Kod Referansı

Email gönderme fonksiyonları:

```python
send_email(to_email, subject, html_body)
send_admin_reservation_notification(reservation)
send_customer_confirmation_email(reservation, approved=True/False)
```
