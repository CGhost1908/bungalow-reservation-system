# 🏠 Bungalow Rezervasyon Sistemi

Flask tabanlı profesyonel bungalow/tatil evi rezervasyon yönetim platformu. Admin paneli, email bildirimleri, takvim görünümü ve tam veri validasyonu ile birlikte gelir.

## ✨ Özellikler

- 🔐 **Güvenli Admin Paneli**: Oturum yönetimi ve password hashing
- 📅 **İnteraktif Takvim**: FullCalendar entegrasyonu, renkli tarih gösterimi
- 📧 **Email Bildirimleri**: Otomatik rezervasyon ve durum değişikliği bildirimleri
- ✅ **Akıllı Validasyon**: Email, telefon, tarih ve çakışma kontrolü
- 👥 **Admin Dashboard**: İstatistikler, beklemede rezervasyonlar, onaylanmış tarihler
- 🌍 **Çok Bungalov Desteği**: Her bungalov için ayrı tarih yönetimi
- 📱 **Responsive Tasarım**: Mobile-friendly arayüz

## 🚀 Kurulum

### 1. Gereksinimler

- Python 3.8+
- pip paket yöneticisi

### 2. Bağımlılıkları Kurun

```bash
pip install -r requirements.txt
```

### 3. Ortam Değişkenlerini Ayarlayın

`.env.example` dosyasından `.env` dosyası oluşturun:

```bash
cp .env.example .env
```

`.env` dosyasını düzenleyin:

```env
# Email Configuration
EMAIL_SENDER=your-email@gmail.com
EMAIL_PASSWORD=your-app-password-16-chars
ADMIN_EMAIL=admin@example.com

# Flask Secret Key
SECRET_KEY=your-random-secret-key-here

# Admin Credentials
ADMIN_USERNAME=admin
ADMIN_PASSWORD=admin123
```

#### Gmail Kurulumu

1. Google Account'ta [2-Step Verification](https://support.google.com/accounts/answer/185839) aktif edin
2. [App Passwords](https://myaccount.google.com/apppasswords) sayfasında Google Account için şifre oluşturun
3. App Password'ü `.env` dosyasında `EMAIL_PASSWORD` olarak ayarlayın

Detaylı talimatlar için: [EMAIL_SETUP.md](EMAIL_SETUP.md)

### 4. Uygulamayı Başlatın

```bash
python app.py
```

Tarayıcıda açın: `http://localhost:5000`

## 📖 Kullanım

### 👤 Müşteri

1. Ana sayfadan "Rezervasyon Yap"ı tıklayın
2. Bilgilerinizi doldurun:
   - Ad Soyad
   - Email
   - Telefon
   - Giriş/Çıkış Tarihleri
   - Bungalov Seçimi
   - Misafir Sayısı
   - Notlar (opsiyonel)
3. Forma gönderin
4. Admin onayını bekleyin (email ile bilgilendirileceksiniz)

### 🔐 Admin Panel

Admin paneline erişim: `http://localhost:5000/admin`

**Varsayılan Kimlik Bilgileri:**
- Kullanıcı Adı: `admin`
- Şifre: `admin123`

**⚠️ Üretim Ortamında Değiştirin!**

#### Admin Paneli Özellikleri

- **Beklemede**: Onay bekleyen rezervasyonlar
- **Onaylanan**: Onaylanan rezervasyonlar
- **Tümü**: Tüm rezervasyonlar
- **Takvim**: Bungalov başına tarih görünümü ve müşteri isimleri

## 🏗️ Proje Yapısı

```
bungalow-main/
├── app.py                          # Ana Flask uygulaması
├── requirements.txt                # Python bağımlılıkları
├── reservations.json              # Rezervasyon veritabanı
├── .env                           # Ortam değişkenleri (gizli)
├── .env.example                   # .env şablonu
├── README.md                      # Bu dosya
├── EMAIL_SETUP.md                 # Email kurulum rehberi
├── ADMIN_SETUP.md                 # Admin paneli rehberi
│
├── templates/                     # HTML şablonları
│   ├── index.html                 # Ana sayfa
│   ├── bungalows.html            # Bungalov listesi
│   ├── gallery.html              # Galeri
│   ├── reservation.html          # Rezervasyon formu
│   ├── admin_login.html          # Admin giriş
│   └── admin_panel.html          # Admin dashboard
│
└── static/                        # Statik dosyalar
    ├── style.css                  # Ana stil
    ├── script.js                  # Ana script
    └── images/                    # Resim dosyaları
```

## 🔌 API Endpoints

### Rezervasyon

- `POST /api/reservation` - Yeni rezervasyon oluştur
- `GET /api/reservations` - Tüm rezervasyonları getir
- `GET /api/reservations/pending` - Beklemede olan rezervasyonlar
- `POST /api/reservations/<id>/approve` - Rezervasyonu onayla
- `POST /api/reservations/<id>/reject` - Rezervasyonu reddet

### Takvim

- `GET /api/booked-dates` - Tüm dolu tarihler
- `GET /api/bungalow-dates/<bungalow>` - Belirli bungalov için tarihler

## 🔒 Güvenlik

- ✅ Werkzeug ile password hashing
- ✅ CSRF koruması session'lar ile
- ✅ Input validation (email, telefon, tarih)
- ✅ Date conflict checking
- ✅ Environment variables'da hassas veriler
- ✅ UUID-based reservation IDs

### Üretim Ayarları

```python
# app.py içinde:
app.run(debug=False)  # Debug mode kapatın
```

## 🐛 Sorun Giderme

### Email Gönderilmiyor

1. `.env` dosyasını kontrol edin
2. Gmail 2FA ve App Password aktif mi?
3. Terminal'de hata mesajlarını kontrol edin
4. `python test_email.py` çalıştırarak test edin

### Admin Paneline Giremiyorum

1. `.env` dosyasında `ADMIN_USERNAME` ve `ADMIN_PASSWORD` kontrol edin
2. Browser cache'i temizleyin
3. Cookies'i silin: Ayarlar > Çerezler > tümünü sil

### Tarih Çakışmaları

Sistem her bungalov için ayrı tarih kontrolü yapar. Eğer hala sorun yaşıyorsanız `reservations.json` dosyasında statüsü "rejected" olan eski rezervasyonları silebilirsiniz.

## 📊 Veri Yapısı

### Rezervasyon Nesnesi

```json
{
  "id": "uuid-string",
  "name": "Müşteri Adı",
  "email": "email@example.com",
  "phone": "05301234567",
  "checkIn": "2024-12-25",
  "checkOut": "2024-12-30",
  "guests": 4,
  "bungalow": "Bungalov Adı",
  "notes": "Opsiyonel notlar",
  "status": "pending/approved/rejected",
  "timestamp": "2024-12-16T10:30:00",
  "approved_date": "2024-12-16T10:35:00",
  "rejected_date": null
}
```

## 🚧 Gelecek Geliştirmeler

- [ ] SQLite/PostgreSQL veritabanı entegrasyonu
- [ ] WhatsApp bildirimleri
- [ ] Fiyatlandırma ve ödeme sistemi
- [ ] Email şablonları özelleştirme
- [ ] Massal işlemler (export, import)
- [ ] Tarih aralığı kopyalama
- [ ] Unit tests

## 📝 Lisans

Bu proje özel kullanım için oluşturulmuştur.

## 👨‍💻 Destek

Sorunlar veya öneriler için lütfen iletişime geçin:
- Email: admin@example.com
- Admin: Berkay Şeyman

---

**Sürüm**: 1.0.0  
**Son Güncelleme**: Aralık 2024
