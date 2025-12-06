# Learning Python — Coding Studio

**Deskripsi:** Proyek ini berisi kumpulan materi dan contoh latihan untuk belajar Python (notebook dan skrip kecil), disusun per sesi.

**Struktur Proyek:**

- **`exercise 2/`**: `latihan-1.ipynb` — latihan praktis.
- **`sesi 1/`**: `sesi-1.ipynb`, `test.html` — materi sesi 1 dan contoh HTML kecil.
- **`sesi 2/`**: `sesi-2.ipynb` — materi sesi 2.
- **`sesi 3/`**: `sesi-3.ipynb` — materi sesi 3.
- **`sesi 4/`**: `sesi-4.ipynb` — materi sesi 4.
- **`sesi 5/`**: `sesi-5.ipynb`, `random.txt`, `test.txt` — materi sesi 5 dan file teks pendukung.
- **`sesi 6/`**: beberapa skrip Python kecil untuk GUI/Tkinter:
  - `button.py` — contoh tombol.
  - `entry.py` — contoh input teks.
  - `error-handling.py` — contoh penanganan error.
  - `grid.py` — contoh layout grid.
  - `label.py` — contoh label.
  - `pack.py` — contoh layout pack.
  - `place.py` — contoh layout place.

**Cara Menjalankan**

- Membuka Jupyter Notebook (file `.ipynb`): jalankan Jupyter di folder proyek lalu buka file terkait.

  Contoh (cmd.exe):

```
pip install jupyter        # jika belum terpasang
jupyter notebook
```

- Menjalankan skrip Python (`sesi 6`): skrip ini menggunakan Tkinter (biasanya sudah ada di instalasi Python standar pada Windows). Jalankan dari `cmd.exe`:

```
python "sesi 6\button.py"
python "sesi 6\entry.py"
```

**Dependensi**

- Python 3.7+ (disarankan). Tkinter biasanya sudah tersedia pada distribusi standar Python di Windows.
- `jupyter` untuk membuka notebook: `pip install jupyter`.

**Catatan**

- Skrip di `sesi 6` adalah contoh GUI sederhana — jalankan satu per satu.
- File `.ipynb` berisi materi interaktif; buka di Jupyter atau VS Code yang mendukung notebook.

**Kontribusi & Penggunaan Selanjutnya**

- Untuk menambahkan materi baru, buat folder `sesi X/` dan tambahkan notebook atau skrip.
- Jika ingin, saya bisa bantu menambahkan file `requirements.txt`, atau menulis instruksi setup lebih lengkap.

--
_Jika kamu mau, saya bisa: commit perubahan ini, menambahkan `requirements.txt`, atau membuat contoh README versi Inggris._
