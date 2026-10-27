# Clear TV Islamic (Edisi Indonesia)

<p><b>Bahasa Indonesia</b> · <a href="README.ms.md">Bahasa Melayu</a> · <a href="README.en.md">English</a> · <a href="docs/INSTALL.md">Panduan Lengkap (Docs)</a></p>

**Ubah Google TV atau Android TV Anda menjadi super cepat, bersih bebas iklan, dengan jadwal sholat akurat standar Kemenag RI, kumandang adzan otomatis, screensaver ayat Al-Qur'an, serta galeri masjid megah Nusantara dan dunia.**

Clear TV Islamic membersihkan aplikasi bawaan yang berat (*bloatware*) dan pelacak iklan dari TV Anda secara nirkabel melalui Wi-Fi — **tanpa perlu root, 100% aman, dan dapat dikembalikan seperti semula kapan saja**. Tampilan beranda TV yang penuh banner iklan digantikan dengan desain kaca modern (*frosted glass*) yang ringan, tenang, dan bernuansa Islami.

---

## 🌟 Fitur Utama

- **🚀 Ringan & Bebas Iklan:** Semua iklan bawaan, video autoplay promosi Google TV, serta layanan latar belakang pabrikan dimatikan. TV bekerja jauh lebih responsif dan hemat RAM.
- **🕌 Jadwal Sholat Standar Kemenag RI:**
  - Menampilkan 5 waktu sholat resmi (**Subuh, Dzuhur, Ashar, Maghrib, Isya**) tepat di bawah jam utama.
  - Dilengkapi perhitungan **Waktu Ihtiyat (Pengaman +2 s.d. +4 menit)** khas Kementerian Agama RI agar 100% sinkron dengan aplikasi adzan di HP dan masjid setempat.
  - Tanggal Hijriah resmi (misal: *16 Jumadil Awal 1448*) dan hitung mundur menuju waktu sholat berikutnya (*"Dzuhur dalam 45 mnt"*).
- **📢 Kumandang Adzan Otomatis:**
  - Saat waktu sholat tiba, suara adzan otomatis berkumandang (`azan.mp3`, dan `azan-subuh.mp3` khusus waktu Subuh).
  - **Tampil di atas semua aplikasi:** Jika Anda sedang menonton YouTube, Netflix, atau siaran TV, banner adzan elegan akan muncul di sepertiga bawah layar dan menjeda video. Cukup tekan tombol apa saja di remote untuk mematikan suara adzan seketika.
- **🕋 Galeri 23 Masjid Megah (Dunia & Nusantara):**
  - Berganti otomatis setiap 30 menit dengan transisi lembut (*cross-fade*).
  - **10 Masjid Ikonik Indonesia:** Masjid Raya Al-Jabbar (Bandung), Masjid Istiqlal (Jakarta), Masjid Raya Baiturrahman (Aceh), Masjid Agung Sumedang, Masjid Agung Jawa Tengah (Semarang), Masjid Islamic Center Samarinda, Masjid Raya Sumatera Barat (Padang), Masjid Raya Al-Mashun (Medan), Masjid Nasional Al-Akbar (Surabaya), dan Masjid Menara Kudus.
  - **13 Masjid Terkenal Dunia:** Masjidil Haram, Ka'bah, Masjid Nabawi, Masjid Quba, Masjid Kristal, Masjid Sultan Ahmed (Blue Mosque Turki), Kubah As-Sakhrah (Palestina), Masjid Faisal (Pakistan), dll.
- **✨ Screensaver Islami (ClockDream):**
  - Saat TV tidak digunakan, layar otomatis menampilkan jam analog emas elegan, kalender Hijriah, kartu jadwal sholat, serta ayat-ayat suci Al-Qur'an lengkap dengan terjemahan resmi Kemenag RI.
- **🧹 Bersih Otomatis Setiap 15 Hari:** TV membersihkan file sampah cache secara mandiri saat siaga tanpa menyentuh data login akun Anda.

---

## 📺 Kompatibilitas Perangkat

Dapat berjalan pada hampir semua perangkat dengan sistem operasi **Android TV atau Google TV (Android 8 Oreo hingga Android 14+)**:
- **Smart TV:** TCL, Xiaomi Mi TV / TV A2, Realme TV, Coocaa, Polytron, Sony Bravia, Hisense, Sharp, dll.
- **TV Box / Dongle:** Google Chromecast with Google TV, Xiaomi Mi Box / TV Stick, Mecool, Realme Stick, dsb.

*(Catatan: TV yang menggunakan OS tertutup seperti Samsung Tizen atau LG webOS memerlukan Android TV Box / Chromecast yang dicolokkan ke port HDMI).*

---

## 🛠️ Panduan Pemasangan Cepat (Tutorial Langkah demi Langkah)

Pemasangan dilakukan dari komputer/laptop (Windows, Mac, atau Linux) yang terhubung ke jaringan Wi-Fi yang sama dengan TV.

### Langkah 1: Aktifkan Debugging Nirkabel di TV

1. Nyalakan TV Anda, buka menu **Setelan (Settings)** ⚙️ $\rightarrow$ **Sistem (System)** $\rightarrow$ **Tentang (About)**.
2. Gulir ke bawah ke menu **Android TV OS Build** (Nomor Build), lalu **tekan tombol OK di remote sebanyak 7 kali berturut-turut** hingga muncul notifikasi *"Anda sekarang adalah seorang pengembang!"*.
3. Kembali ke menu **Sistem**, sekarang akan muncul menu baru: **Opsi Pengembang (Developer Options)**.
4. Buka menu tersebut, lalu aktifkan **USB Debugging** (dan **Network Debugging** jika tersedia).
5. Cari tahu alamat IP TV Anda di menu **Setelan** $\rightarrow$ **Jaringan & Internet** (contoh: `192.168.1.7`).

---

### Langkah 2: Siapkan Terminal di Komputer

Buka terminal (PowerShell di Windows, atau Terminal di Mac/Linux), lalu masuk ke direktori repositori ini:

```bash
cd Z:\github\cleartv-Islamic
```

Siapkan virtual environment Python (hanya perlu sekali di awal):

**Di Windows (PowerShell):**
```powershell
python -m venv tools\venv
.\tools\venv\Scripts\pip install -r tools\requirements.txt
```

**Di Mac / Linux:**
```bash
python3 -m venv tools/venv
./tools/venv/bin/pip install -r tools/requirements.txt
```

---

### Langkah 3: Uji Koneksi ke TV

Setel variabel alamat IP TV Anda, lalu jalankan tes deteksi (*probe*):

**Di Windows (PowerShell):**
```powershell
$env:TV_HOST = "192.168.1.7"     # Ganti dengan IP TV Anda
.\tools\venv\Scripts\python.exe tools\tv.py --probe
```

> **PENTING:** Saat pertama kali menghubungkan, layar TV Anda akan memunculkan dialog pop-up konfirmasi: *"Izinkan USB Debugging dari komputer ini?"*. Centang kotak **"Selalu izinkan dari komputer ini"**, lalu klik **OK** menggunakan remote TV.

---

### Langkah 4: Matikan Iklan & Bloatware TV (Debloat)

Sebelum menonaktifkan aplikasi bawaan, simpan daftar cadangan aplikasi yang ada di TV Anda:

```powershell
.\tools\venv\Scripts\python.exe tools\tv.py "pm list packages -u" > backup-aplikasi-tv.txt
```

Nonaktifkan launcher berat Google TV dan layanan iklan bawaan pabrikan (contoh perintah untuk TCL / Google TV):

```powershell
# Matikan launcher iklan Google TV
.\tools\venv\Scripts\python.exe tools\tv.py "pm disable-user --user 0 com.google.android.apps.tv.launcherx"
.\tools\venv\Scripts\python.exe tools\tv.py "pm disable-user --user 0 com.google.android.tungsten.setupwraith"

# Matikan promo pabrikan (contoh: TCL)
.\tools\venv\Scripts\python.exe tools\tv.py "pm disable-user --user 0 com.tcl.waterfall.overseas"
.\tools\venv\Scripts\python.exe tools\tv.py "pm disable-user --user 0 com.tcl.dashboard"
```

*(Daftar debloat siap pakai untuk berbagai merk TV tersedia di folder `examples/`).*

---

### Langkah 5: Pasang APK Launcher Clear TV Islamic

Pasang file APK siap pakai yang sudah diterjemahkan ke Bahasa Indonesia (`dist/clear-tv-islamic.apk`):

```powershell
# Kirim dan pasang APK
.\tools\venv\Scripts\python.exe tools\tv.py --push dist\clear-tv-islamic.apk /data/local/tmp/app.apk
.\tools\venv\Scripts\python.exe tools\tv.py "pm install -r /data/local/tmp/app.apk"

# Jadikan sebagai Launcher Beranda Default
.\tools\venv\Scripts\python.exe tools\tv.py "cmd package set-home-activity com.gathin.tvhome/.MainActivity"

# Berikan izin agar adzan bisa muncul di atas YouTube / Netflix
.\tools\venv\Scripts\python.exe tools\tv.py "appops set com.gathin.tvhome SYSTEM_ALERT_WINDOW allow"
```

---

### Langkah 6: Kirim Tema, Wallpaper Masjid & Jadwal Sholat

Kirim aset tema Islami (suara adzan, database jadwal sholat, galeri 23 masjid, dan konfigurasi) ke TV:

```powershell
.\tools\venv\Scripts\python.exe tools\b64push.py themes\islamik\solat-SMD01.json /sdcard/Android/data/com.gathin.tvhome/files/solat-SMD01.json
.\tools\venv\Scripts\python.exe tools\push_new_masjid.py
```

Setel screensaver Islami sebagai screensaver default TV:
```powershell
.\tools\venv\Scripts\python.exe tools\tv.py "settings put secure screensaver_components com.gathin.tvhome/.ClockDream"
```

Nyalakan launcher di layar TV Anda:
```powershell
.\tools\venv\Scripts\python.exe tools\tv.py "am start -n com.gathin.tvhome/.MainActivity"
```

Selesai! TV Anda kini tampil tenang, anggun, bebas iklan, dan bernuansa Islami.

---

## 📍 Menyesuaikan Kota Jadwal Sholat (Kota Lain di Indonesia)

Secara bawaan repositori ini telah dikonfigurasi untuk wilayah **Sumedang Utara, Jawa Barat** (kode zona `SMD01`).

Jika Anda ingin mengubah ke kota Anda sendiri:
1. Buka file [`tools/fetch_sumedang.py`](tools/fetch_sumedang.py).
2. Ubah titik koordinat `latitude` dan `longitude` sesuai kota Anda (misal: Jakarta `-6.2088, 106.8456`, Surabaya `-7.2575, 112.7521`, Medan `3.5952, 98.6722`).
3. Jalankan script tersebut untuk men-generate file `solat-KODECOTA.json`.
4. Ubah `"prayer_zone": "KODECOTA"` di file [`themes/islamik/config.json`](themes/islamik/config.json).
5. Kirim file JSON tersebut ke TV menggunakan `tools/b64push.py`.

---

## 🎮 Panduan Navigasi Remote TV

- **Menggeser Posisi Aplikasi di Dock/Beranda:**
  Arahkan sorotan ke aplikasi yang ingin dipindah, **tekan dan tahan tombol OK di remote**. Menu kaca akan muncul, pilih **Move**. Gunakan tombol panah kiri/kanan untuk memindahkan posisi aplikasi, lalu tekan **OK** untuk meletakkan.
- **Pindah Port HDMI / Antena Siaran:**
  Klik tombol kapsul **Inputs** di pojok kanan atas beranda. Menu kaca daftar HDMI 1, HDMI 2, AV, dan TV Digital akan terbuka otomatis.
- **Mematikan Suara Adzan:**
  Jika adzan sedang berbunyi dan Anda ingin segera menghentikannya (misalnya saat ada panggilan telepon), cukup **tekan tombol apa saja di remote TV**.
- **Aplikasi Rekomendasi (SmartTube):**
  Untuk menonton YouTube tanpa iklan video sponsor, Anda dapat memasang aplikasi SmartTube (`org.smarttube.stable`) yang dapat berjalan selaras dan lancar dengan launcher ini.

---

## 🔄 Cara Mengembalikan TV ke Semula (Restore / Rollback)

Jika suatu saat Anda ingin menjual TV atau mengembalikan launcher asli pabrikan, Anda dapat membatalkan semua perubahan dengan mudah melalui terminal:

```powershell
# Aktifkan kembali launcher bawaan pabrik
.\tools\venv\Scripts\python.exe tools\tv.py "pm enable com.google.android.apps.tv.launcherx"
.\tools\venv\Scripts\python.exe tools\tv.py "pm enable com.google.android.tungsten.setupwraith"

# Hapus launcher Clear TV Islamic jika diinginkan
.\tools\venv\Scripts\python.exe tools\tv.py "pm uninstall com.gathin.tvhome"
```

Semua data akun, setelan gambar, Wi-Fi, dan remote TV Anda tetap utuh seperti sedia kala.

---

## 📜 Lisensi & Penghargaan

- **Basis Proyek:** Dikembangkan dari [CleanYourTV](https://github.com/Gathin23/cleanyourtv) © Gathin, lisensi MIT.
- **Jadwal & Data Falak:** Mengacu pada hisab Kementerian Agama Republik Indonesia (Bimas Islam) via AlAdhan API dengan toleransi pengaman (*ihtiyat*).
- **Mushaf & Terjemahan:** Teks Al-Qur'an rasm Utsmani dan terjemahan resmi Departemen Agama / Kemenag RI via [quran.com](https://quran.com).
- **Foto Masjid:** Bersumber dari kontributor sukarela di [Wikimedia Commons](https://commons.wikimedia.org/) dengan lisensi bebas (Creative Commons / Public Domain). Masing-masing nama fotografer tercantum di pojok layar saat foto ditampilkan.
- **Rekaman Adzan:** Adzan Makkah & Madinah, Ustaz Asri Ibrahim (Rabbani), dan Adzan Subuh Merdu.
