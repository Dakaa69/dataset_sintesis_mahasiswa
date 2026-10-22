# Analisis Bedah Kasus 2: Dataset Profil Mahasiswa

## Identitas
**Nama:** Raka Ramadhan  
**NIM:** 241051016

## 1. Tujuan
Analisis ini mengembangkan dua observasi awal pada soal menjadi 1.000 observasi sintetis. Dataset kemudian dianalisis dengan statistik deskriptif dan divisualisasikan dalam dashboard Streamlit.

## 2. Data awal
- Sistem Informasi | Semester 3 | IPK 3,85 | Usia 20 tahun
- Manajemen | Semester 1 | IPK 3,50 | Usia 19 tahun

## 3. Desain sintesis
Seed yang digunakan adalah **42**. Jurusan dipertahankan menjadi dua kategori. Semester dibuat sebagai variabel ordinal 1 sampai 8. IPK dan usia dibuat sebagai variabel numerik kontinu/diskrit dengan variasi acak yang tetap berada dalam rentang realistis untuk data latihan.

Karena sumber hanya terdiri dari dua observasi, distribusi sintetis tidak dapat dianggap sebagai estimasi populasi mahasiswa yang sebenarnya.

## 4. Statistik deskriptif
- Jumlah observasi: **1,000**
- Rata-rata IPK: **3.69**
- Median IPK: **3.70**
- IPK minimum-maksimum: **3.17 sampai 4.00**
- Rata-rata usia: **21.88 tahun**
- Usia minimum-maksimum: **18 sampai 28 tahun**
- Rata-rata semester: **3.55**

## 5. Perbandingan jurusan
Sistem Informasi menghasilkan **503 mahasiswa** dengan rata-rata IPK **3.85** dan rata-rata usia **22.83 tahun**.

Manajemen menghasilkan **497 mahasiswa** dengan rata-rata IPK **3.53** dan rata-rata usia **20.93 tahun**.

Perbedaan rata-rata IPK terutama mencerminkan desain sintesis yang mempertahankan dua nilai acuan dari soal. Karena itu, perbedaan tersebut tidak boleh dipakai untuk menyimpulkan kualitas akademik antarkelompok pada populasi nyata.

## 6. Semester sebagai data ordinal
Semester memiliki urutan yang jelas dari 1 sampai 8. Bar chart berurutan cocok untuk menunjukkan distribusi. Analisis tambahan memakai rata-rata IPK per semester untuk melihat pola deskriptif.

## 7. Variabel numerik
Histogram dan box plot digunakan untuk IPK dan usia. Visualisasi ini membantu melihat pusat data, penyebaran, serta nilai ekstrem. Scatter plot digunakan untuk membandingkan usia dengan IPK.

## 8. Korelasi
Matriks korelasi dihitung untuk Semester, IPK, dan Usia. Interpretasinya terbatas pada hubungan linear dan tidak menyatakan sebab-akibat. Karena dataset merupakan sintesis, korelasi lebih tepat digunakan sebagai latihan analitik daripada bukti empiris.

## 9. Kesimpulan
Dataset 1.000 baris sudah memenuhi kebutuhan latihan untuk variabel nominal, ordinal, dan numerik. Dashboard menyediakan filter jurusan, semester, IPK, dan usia serta visualisasi distribusi, perbandingan, hubungan numerik, dan tabel data.
