# Tugas Chatbot RAG PDF

Tugas ini adalah aplikasi chatbot berbasis RAG (Retrieval-Augmented Generation) yang bisa menjawab pertanyaan berdasarkan isi file PDF. Aplikasi ini berjalan di terminal menggunakan Python. 

## Tools yang digunakan
- Python
- LangChain
- Google Gemini 1.5 Flash
- Google Embedding (gemini-embedding-001)
- Chroma (untuk database vektor)
- PyPDFLoader

## Cara Instalasi
1. Pastikan Python sudah terinstall di komputer.
2. Buka terminal atau command prompt, lalu masuk ke folder project ini.
3. Install semua library yang dibutuhkan dengan perintah:
   ```bash
   pip install -r requirements.txt
   ```

## Persiapan API Key
Catatan: API Key dari Google sangat rahasia dan harus disimpan pada file `.env`.
1. Buat file baru bernama `.env` di folder utama project.
2. Buka file `.env.example` dan copy isinya ke file `.env` yang baru dibuat.
3. Ganti `YOUR_API_KEY_HERE` dengan API key milikmu.

## Cara Menjalankan Program
Setelah semua library diinstall dan `.env` sudah disiapkan, jalankan program dengan perintah:
```bash
python app.py
```

## Contoh Penggunaan
Saat program dijalankan, akan muncul tampilan seperti ini:
```text
===================================
CHATBOT RAG PDF
===================================
Ketik pertanyaan atau ketik exit untuk keluar.

Pertanyaan:
> 
```
Kamu tinggal mengetik pertanyaan dan menekan Enter. Jika ingin keluar, cukup ketik `exit`.

## Struktur Folder
- `app.py`: File utama berisi kode program chatbot.
- `requirements.txt`: Daftar library Python yang digunakan.
- `data/`: Folder untuk menyimpan file PDF (contoh: `BERT (Devlin dkk., 2019).pdf`).
- `chroma_db/`: Folder database Chroma (otomatis dibuat oleh program saat dijalankan).
- `screenshots/`: Folder untuk menyimpan gambar hasil atau screenshot aplikasi.
- `.env.example`: Contoh format file untuk menaruh API Key.
