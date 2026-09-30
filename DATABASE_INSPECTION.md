# SQLite Database İnceleme Rehberi

## 🔍 Database'i İncelemek için 3 Yol

### 1️⃣ Python Script (En Kolay) ⭐ **ÖNERİLEN**

```bash
python inspect_db.py
```

**Avantajları:**
- ✅ Kurulum yok (sadece Python gerekli)
- ✅ Güzel formatted çıktı
- ✅ Türkçe mesajlar
- ✅ İstatistikler
- ✅ Detaylı görünüm

**Örnek Çıktı:**
```
================================================================================
📊 DATABASE ÖZETİ
================================================================================

✅ Tablolar (1):
   - reservations: 0 satır

================================================================================
📋 REZERVASYONLAR
================================================================================

❌ Hiç rezervasyon yok!
```

---

### 2️⃣ Windows CMD Script

```bash
inspect_db.bat
```

**Avantajları:**
- ✅ Native Windows
- ✅ Ekstra kurulum yok
- ✅ Hızlı

**Gereksinimler:**
- SQLite3 command line tool (Windows'ta bundled)

---

### 3️⃣ VS Code SQLite Extension (Premium) 💎

#### Kurulum:

1. **VS Code Extensions'ı aç** (Ctrl+Shift+X)
2. **"SQLite" ara**
3. "SQLite" extension'ını (alexcvzz tarafından) kur
   
   ![image](https://user-images.githubusercontent.com/..../extension.png)

4. **Database'i aç:**
   - File Explorer'da `reservations.db` dosyasına sağ tıkla
   - "Open Database" seç
   - Left sidebar'da "SQLite Explorer" paneli açılır

5. **Sorgular çalıştır:**
   - Extension'da SQL sorguları yazıp Ctrl+Shift+P > "SQLite: Run Query"

#### Örnek Sorgular:

```sql
-- Tüm rezervasyonları göster
SELECT * FROM reservations;

-- Statüs'e göre özet
SELECT status, COUNT(*) as count FROM reservations GROUP BY status;

-- Bungalov başına özetler
SELECT bungalow, COUNT(*) as count FROM reservations GROUP BY bungalow;

-- Onaylı rezervasyonlar
SELECT name, email, bungalow, checkIn, checkOut FROM reservations WHERE status = 'approved';
```

---

## 🔗 Direct SQLite Commands (Terminal'de)

```bash
# Database'e bağlan (interactive shell)
sqlite3 reservations.db

# SQL sorgu çalıştır
sqlite3 reservations.db "SELECT * FROM reservations;"

# Column mode'da göster (daha güzel)
sqlite3 reservations.db ".mode column" ".headers on" "SELECT * FROM reservations;"

# Tüm tabloları listele
sqlite3 reservations.db ".tables"

# Tablo schema'sını göster
sqlite3 reservations.db ".schema reservations"

# CSV olarak export et
sqlite3 reservations.db ".mode csv" ".headers on" "SELECT * FROM reservations;" > reservations.csv
```

---

## 💾 Veri Tabanı Dosyaları

- **reservations.db** - Aktif SQLite database
- **reservations.json.backup** - Eski JSON backup (eğer migration yapıldıysa)

---

## ✅ Database Kontrol Listesi

- [ ] `reservations.db` dosyası var mı?
- [ ] Tables mevcut mu? (`sqlite3 reservations.db ".tables"`)
- [ ] Veri bulunuyor mu? (`python inspect_db.py`)
- [ ] Indexes oluşmuş mu? (otomatik oluşturulmalı)

---

## 🆘 Sorun Giderme

**Problem:** "sqlite3 is not recognized"
```bash
# Çözüm: Python'dan kullan
python inspect_db.py
```

**Problem:** "No such table"
```bash
# Çözüm: Uygulamayı çalıştır database'i initialize etsin
python app.py
# (Ctrl+C ile durdur)
```

**Problem:** "ModuleNotFoundError: No module named 'tabulate'"
```bash
# Çözüm: Şimdilik inspect_db.py tabulate'siz de çalışıyor
python inspect_db.py
```

---

## 📚 Faydalı Linkler

- [SQLite Official](https://www.sqlite.org/)
- [VS Code SQLite Extension](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite)
- [SQLite CLI Tutorial](https://www.sqlitetutorial.net/sqlite-tutorial/sqlite-command-line-shell/)

---

**Son Güncelleme:** 16 Aralık 2024
