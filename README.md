## 📄 PCD_DocFixer

**DocFixer: Aplikasi Peningkatan Kontras Dokumen Tercetak**  
Proyek ini dibuat sebagai bagian dari tugas mata kuliah Pengolahan Citra Digital di Universitas Pancasakti Tegal.

---

## 🎯 Deskripsi

**DocFixer** adalah aplikasi berbasis Python yang berfungsi untuk meningkatkan kejelasan teks pada dokumen tercetak dengan cara:
- Meningkatkan kontras teks (menggunakan CLAHE)
- Melakukan thresholding adaptif
- Menampilkan hasil sebelum dan sesudah
- Menyimpan hasil ke folder otomatis

Tersedia dua mode input:
- 📷 Ambil gambar dari **file foto**
- 📸 Scan langsung menggunakan **webcam**

---

## 🛠️ Fitur Utama

- ✅ Peningkatan kontras teks dokumen (CLAHE)
- ✅ Thresholding adaptif (untuk teks tidak merata)
- ✅ Input dari file atau kamera
- ✅ Simpan hasil ke folder `output/`
- ✅ UI sederhana menggunakan Tkinter

---

## 📦 Instalasi

1. Clone repository:
   ```bash
   git clone https://github.com/namakamu/PCD_DocFixer.git
   cd PCD_DocFixer
