

Tentu, saya akan buatkan file `README.md` yang lengkap dan profesional untuk proyek Anda. File ini akan menjelaskan cara setup, cara penggunaan, dan fitur-fitur dari kode yang Anda berikan.

---

# Sistem Interaksi Tangan & Validasi Wajah dengan MediaPipe

Proyek ini adalah aplikasi computer vision real-time yang dikembangkan dengan Python, menggunakan library OpenCV dan MediaPipe. Aplikasi ini memungkinkan pengguna untuk berinteraksi dengan objek di layar menggunakan gerakan tangan setelah wajah mereka terdeteksi dan divalidasi di posisi yang tepat.

Sistem ini bekerja dengan dua langkah utama:
1.  **Validasi Wajah:** Pengguna harus memposisikan wajah mereka di dalam sebuah oval yang ada di tengah layar.
2.  **Interaksi Tangan:** Setelah wajah valid, pengguna bisa menggunakan ujung jari telunjuk untuk menyentuh kotak-kotak berwarna yang akan memicu pemutaran file suara (nada musik).

![Contoh Aplikasi](https://via.placeholder.com/1280x720.png?text=Face+Alignment+and+Hand+Interaction+Demo)

*(Ganti dengan screenshot atau GIF dari aplikasi Anda yang sedang berjalan)*

## 🚀 Fitur

-   **Validasi Wajah Real-time:** Menggunakan MediaPipe Face Mesh untuk mendeteksi wajah dan memastikan pengguna berada di posisi yang ditentukan.
-   **Deteksi Tangan & Landmark:** Melacak gerakan tangan dan 21 landmark pada setiap tangan dengan MediaPipe Hands.
-   **Interaksi Berbasis Kotak:** 5 kotak interaktif dengan warna dan posisi berbeda yang dapat dipicu dengan jari telunjuk.
-   **Pemutaran Suara:** Memutar file MP3 yang berbeda (Do, Re, Mi, Fa, Sol) saat kotak yang sesuai disentuh.
-   **Visual Feedback:** Memberikan umpan balik visual secara real-time, seperti perubahan warna oval, penanda posisi jari, dan penyorotan kotak yang dipilih.
-   **Anti-Spam Suara:** Logika cerdas untuk memastikan setiap suara hanya diputar sekali saat jari memasuki area kotak, mencegah pemutaran berulang-ulang.

## 📋 Prasyarat

Sebelum memulai, pastikan Anda telah menginstal hal-hal berikut:

-   Python 3.7 atau lebih tinggi
-   Pip (Manajer paket Python)
-   Kamera Web (Webcam) yang terpasang dan berfungsi

## 🛠️ Cara Setup Proyek

Ikuti langkah-langkah di bawah ini untuk mengatur dan menjalankan proyek ini di komputer Anda.

### Langkah 1: Clone Repository

Pertama, clone repository ini ke komputer lokal Anda menggunakan Git:

```bash
git clone https://github.com/username/nama-repo-anda.git
cd nama-repo-anda
```

*(Ganti `username/nama-repo-anda` dengan URL repository Anda)*

### Langkah 2: Buat Lingkungan Virtual (Sangat Direkomendasikan)

Menggunakan lingkungan virtual akan mengisolasi dependensi proyek Anda dari sistem global.

**Untuk Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Untuk macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Langkah 3: Instal Dependensi

Setelah lingkungan virtual aktif, instal semua library yang diperlukan dengan perintah berikut:

```bash
pip install opencv-python mediapipe numpy playsound==1.2.2
```
> **Catatan:** Versi `playsound==1.2.2` seringkali lebih stabil dan kompatibel. Jika mengalami masalah, Anda bisa mencoba versi lain atau library alternatif seperti `pygame.mixer`.

### Langkah 4: Siapkan File Suara

Kode ini membutuhkan 5 file suara dengan format `.mp3`. Buatlah folder (atau letakkan di direktori utama proyek) dan pastikan Anda memiliki file-file dengan nama **persis** seperti di bawah ini:

-   `do.mp3`
-   `re.mp3`
-   `mi.mp3`
-   `fa.mp3`
-   `sol.mp3`

Pastikan file-file ini berada di **direktori yang sama dengan file Python Anda**, atau Anda bisa memodifikasi variabel `AUDIO_FILENAMES` dalam kode untuk menyesuaikan path-nya.

Struktur direktori yang disarankan:
```
nama-repo-anda/
├── main.py             # File Python utama Anda
├── do.mp3
├── re.mp3
├── mi.mp3
├── fa.mp3
├── sol.mp3
├── README.md
└── ... (file lainnya)
```

## 🎮 Cara Penggunaan

Setelah semua setup selesai, Anda dapat menjalankan aplikasinya:

1.  **Jalankan Skrip:** Buka terminal/command prompt di direktori proyek, lalu jalankan perintah:
    ```bash
    python main.py
    ```
    *(Ganti `main.py` dengan nama file Python Anda jika berbeda)*

2.  **Posisikan Wajah:** Arahkan wajah Anda ke kamera. Posisikan wajah tepat di tengah oval yang muncul di layar. Oval akan berubah warna menjadi hijau dan menampilkan "Wajah Tepat, OK!" jika posisi sudah benar.

3.  **Interaksi dengan Tangan:** Setelah wajah valid, angkat salah satu tangan Anda ke depan kamera. Arahkan ujung jari telunjuk Anda ke salah satu dari 5 kotak berwarna.

4.  **Dengarkan Suara:** Saat jari Anda memasuki area kotak, aplikasi akan memutar nada musik yang sesuai dengan kotak tersebut dan menampilkan nama kotak di layar.

5.  **Keluar:** Tekan tombol `q` pada keyboard untuk menutup aplikasi.

## 📁 Struktur Proyek

```
.
├── main.py                 # Skrip utama aplikasi
├── do.mp3                  # File suara untuk kotak Merah (Do)
├── re.mp3                  # File suara untuk kotak Hijau (Re)
├── mi.mp3                  # File suara untuk kotak Biru (Mi)
├── fa.mp3                  # File suara untuk kotak Kuning (Fa)
├── sol.mp3                 # File suara untuk kotak Ungu (Sol)
└── README.md               # File dokumentasi ini
```

## 🤝 Kontribusi

Kontribusi sangat dihargai! Jika Anda memiliki ide untuk fitur baru, menemukan bug, atau ingin meningkatkan kode, silakan buat *issue* atau ajukan *pull request*.

1.  Fork proyek ini
2.  Buat fitur branch (`git checkout -b fitur/FiturBaru`)
3.  Commit perubahan Anda (`git commit -m 'Menambahkan fitur baru'`)
4.  Push ke branch (`git push origin fitur/FiturBaru`)
5.  Buka Pull Request

## 📝 Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat file [LICENSE](LICENSE) untuk detailnya.

## 👤 Kontak

Jika Anda memiliki pertanyaan, silakan hubungi saya melalui [email Anda] atau [profil GitHub Anda].

---
