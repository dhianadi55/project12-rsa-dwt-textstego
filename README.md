# Tugas Besar Kriptografi (IF3027)

## Kelompok 12

### Anggota Kelompok / NIM
- Dhian Adi Nugraha — 121140055  
- Hafiza Eka Ramadhini — 121140048

---

## Informasi Mata Kuliah
- Mata Kuliah / Kelas : RA  
- Metode Kriptografi   : RSA  
- Metode Steganografi  : DWT  
- Pesan                : Text  
- Cover (Media Penampung) : Image  

---

## Evaluasi
1. **RSA:** Waktu Komputasi Enkripsi & Dekripsi, Avalanche Effect  
2. **DWT:** Payload Capacity, Robustness  

---

## Judul  
**Integrasi Kriptografi RSA dan Steganografi DWT untuk Keamanan Pesan Teks dalam Citra Digital**

---

## Jurnal Rujukan
1. Kumar, E. Yuva, and P. Padmaja. 2014. "RSA Based Secured Image Steganography Using DWT Approach." *International Journal of Engineering Research and Applications* 4, no. 8 (Version 1): 1–4. Accessed May 17, 2025. www.ijera.com.  
2. Tushara, M., and K. A. Navas. 2016. "Image Steganography Using Discrete Wavelet Transform – A Review." *International Journal of Innovative Research in Electrical, Electronics, Instrumentation and Control Engineering (IJIREEICE)* 3 (Special Issue 1): February 2016.  
3. Sitoresmi, Galuh, and Wijanarto. 2025. "Analisis Algoritma RSA dan LSB pada One Time Password untuk Financial Technology." *Jurnal Eksplora Informatika*, no. 122–131. Jurusan Teknik Informatika, Fakultas Ilmu Komputer UDINUS, Semarang. Accessed May 17, 2025.  
4. Mido, Agus Rakhmadi, and Erik Iman Heri Ujianto. 2022. "Analisis Pengaruh Citra Terhadap Kombinasi Kriptografi RSA dan Steganografi LSB." *Jurnal Teknologi Informasi dan Ilmu Komputer (JTIIK)* 9, no. 2: 279–86. https://doi.org/10.25126/jtiik.202294852.  
5. Tampubolon, Tamardi Pranata, Rita Magdalena, and Nur Andini. 2016. "Simulasi dan Analisis Keamanan Teks Menggunakan Metode Steganografi Discrete Wavelet Transform (DWT) dan Metode Enkripsi Cellular Automata." *e-Proceeding of Engineering* 3, no. 2 (August): 1470.  
6. Ibrahim, Ade. 2021. *Menggabungkan Teknik Steganografi Discrete Wavelet Transform Dua Dimensi (2-D) dan Algoritma Kriptografi RSA pada Perancangan dan Analisis Keamanan Pesan.* Tugas Akhir, Program Studi Teknik Elektro, Fakultas Sains dan Teknologi, Universitas Islam Negeri Sultan Syarif Kasim Riau, Pekanbaru.  
7. Umam, Chaerul, and Muslih. 2023. "Enkripsi Data Teks dengan AES dan Steganografi DWT." *InComTech: Jurnal Telekomunikasi dan Komputer* 13, no. 1 (April): 28–39. https://doi.org/10.22441/incomtech.v13i1.15059.

---

## Cara Menjalankan Aplikasi

Berikut adalah langkah-langkah untuk menjalankan aplikasi ini, tergantung pada preferensi Anda:

### Menggunakan Terminal di VS Code

1.  **Pastikan Python Terpasang:**
    Buka terminal di VS Code (Ctrl+\` atau Cmd+\`). Jalankan perintah berikut untuk memeriksa versi Python Anda:
    ```bash
    python --version
    ```
    Pastikan Python 3 terinstal.

2.  **Perbarui pip (Opsional tetapi Disarankan):**
    Pastikan Anda menggunakan versi pip terbaru dengan menjalankan:
    ```bash
    pip install --upgrade pip
    ```

3.  **Instal Dependensi:**
    Aplikasi ini memiliki dependensi yang tercantum dalam file `requirements.txt`. Instal dependensi tersebut menggunakan perintah:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Jalankan Aplikasi:**
    Setelah semua dependensi terinstal, jalankan aplikasi utama dengan perintah:
    ```bash
    python main.py
    ```

### Menggunakan Command Prompt (CMD) atau Command Line Interface (CLI)

1.  **Navigasi ke Direktori Proyek:**
    Buka Command Prompt (CMD) di Windows atau terminal di sistem operasi lain. Gunakan perintah `cd` untuk berpindah ke direktori proyek Anda. Dalam kasus ini:
    ```bash
    cd /d D:\VSCode\cryptography\project
    ```
    (Pastikan jalur di atas sesuai dengan lokasi proyek Anda.)

2.  **Buat dan Aktifkan Virtual Environment (Disarankan):**
    Membuat virtual environment akan mengisolasi dependensi proyek Anda.
    ```bash
    python -m venv .project12
    ```
    Setelah dibuat, aktifkan virtual environment:
    ```bash
    .project12\Scripts\activate
    ```
    (Di Linux/macOS, perintah aktivasi mungkin sedikit berbeda, contohnya: `source .project12/bin/activate`)

3.  **Instal Dependensi (Jika Belum Dilakukan di Lingkungan Global):**
    Jika Anda baru membuat virtual environment, Anda perlu menginstal dependensi di dalamnya:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Jalankan Aplikasi:**
    Setelah virtual environment aktif dan dependensi terinstal, jalankan aplikasi utama:
    ```bash
    python main.py
