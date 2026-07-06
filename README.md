# Deep Learning & Visual Recommender System

## Deskripsi Singkat
 Dalam platform e-commerce/hiburan modern, pengguna sering kali mengalami *information overload* akibat banyaknya pilihan produk atau konten yang tersedia. Proyek ini bertujuan untuk membangun sebuah **Sistem Rekomendasi (Recommender System)** interaktif yang mampu memprediksi dan menyarankan item paling relevan bagi pengguna guna meningkatkan *engagement* dan personalisasi.

**Pendekatan Deep Learning / Computer Vision (DL/CV):**
* **Deep Collaborative Filtering:** Menggunakan arsitektur Deep Learning (*Neural Collaborative Filtering* / NCF) untuk menangkap interaksi non-linear yang kompleks antara pengguna dan item dari data historis.
* **Visual Content-Based Filtering (CV):** Memanfaatkan model Computer Vision (seperti CNN / ResNet) untuk mengekstraksi fitur visual dari gambar produk/poster film, sehingga sistem dapat merekomendasikan item dengan kemiripan visual.

---

## Minimum Viable Product (MVP)
MVP yang akan dibangun dalam proyek ini mencakup:
1. **Pipeline Pemrosesan Data:** Skrip pembersihan data tabular (interaksi user-item) dan data visual (gambar produk/item).
2. **Model Baseline & Deep Learning:** Implementasi model rekomendasi dasar sebagai pembanding (*baseline*) dan model Deep Learning/CV yang sudah dilatih.
3. **Fungsi Prediksi Top-N:** Sebuah skrip/modul yang menerima input `user_id` atau `image_input` dan menghasilkan *Top-N Recommendations* beserta skor relevansinya.
4. **Dokumentasi & Evaluasi:** Visualisasi hasil evaluasi model menggunakan metrik standar industri seperti *Precision@K*, *Recall@K*, atau *NDCG*.

---

## Tech Stack Sementara
* **Bahasa Pemrograman:** Python
* **Manipulasi & Analisis Data:** Pandas, NumPy
* **Deep Learning & Computer Vision:** PyTorch / TensorFlow, OpenCV
* **Visualisasi Data:** Matplotlib, Seaborn
* **Lingkungan Pengembangan:** Jupyter Notebook, Git & GitHub

---

## Status Proyek
> `Hari ke-1`
> Menentukan rumusan masalah dan arsitektur pendekatan (DL/CV).
> Inisialisasi struktur repositori GitHub (`/data`, `/notebooks`, `/src`).
> Pengaturan *virtual environment* dan instalasi *dependencies* awal.

> `Hari ke-2`
> Menmbah dataset
> Notebook EDA
> Definisi Maalah

> `Hari ke-3`
> Bangun baseline model (item-based CF / content-based TF-IDF)
> Evaluasi

> `Hari ke-4`
