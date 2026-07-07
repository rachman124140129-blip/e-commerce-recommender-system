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
> `Hari ke-1: Inisialisasi Proyek & Persiapan Lingkungan Kerja`
    Hari pertama difokuskan pada perencanaan arsitektur dan penerapan best practices software engineering sebelum menulis kode analitik.

    Perumusan Masalah & Desain Arsitektur: Menentukan pendekatan awal (apakah menggunakan Collaborative Filtering, Content-Based, atau Deep Learning) dan merancang alur pemrosesan data dari input menuju output rekomendasi.

    Strukturisasi Repositori GitHub: Membangun direktori proyek yang modular untuk memisahkan tanggung jawab kode:

    - /data: Untuk menyimpan data mentah (raw) dan data yang telah diproses (processed).
    - /notebooks: Untuk eksperimentasi, analisis data interaktif (EDA), dan pembuatan prototipe.
    - /src: Untuk menyimpan skrip modular (source code) Python yang bersih dan siap untuk deployment atau automasi pipeline.

    Isolasi Lingkungan (Virtual Environment): Mengatur virtual environment dan memasang pustaka (dependencies) dasar agar proyek bersifat reprodusibel dan terisolasi dari konflik pustaka di sistem operasi utama.

> `Hari ke-2: Pengumpulan Data, Eksplorasi (EDA), & Definisi Masalah`
    Hari kedua adalah tahap memahami karakteristik data untuk memastikan model yang dibangun nantinya sesuai dengan realitas dataset.

    Integrasi Dataset: Memasukkan dataset (seperti dataset MovieLens dari Kaggle) ke dalam direktori /data.

    Exploratory Data Analysis (EDA): Menulis notebook eksplorasi untuk menganalisis distribusi rating, tingkat kelangkaan data (sparsity), populasi pengguna, serta film-film terpopuler. Tahap ini membantu menemukan anomal-anomali data serta menentukan strategi pembersihan (preprocessing).

    Definisi Masalah Formal: Menajamkan rumusan masalah ML secara spesifik berdasarkan hasil EDA—menentukan fitur input eksplisit/implisit, target prediksi (misalnya prediksi angka rating atau Top-N ranking), dan metrik evaluasi yang akan dicapai.

> `Hari ke-3: Pemodelan Baseline & Benchmarking`
    Sebelum melangkah ke model yang rumit, hari ketiga didedikasikan untuk membuat model acuan (baseline model) sebagai tolok ukur performa.

    Implementasi Algoritma Dasar: Membangun model awal menggunakan pendekatan tradisional yang mudah diinterpretasikan (explainable):

    Item-Based Collaborative Filtering: Menggunakan Cosine Similarity pada matriks User-Item untuk menemukan kemiripan antar film berdasarkan riwayat rating pengguna.

    Content-Based Filtering (TF-IDF): Menggunakan metadata (seperti genre atau teks deskripsi) untuk merekomendasikan item serupa, yang sekaligus berfungsi sebagai solusi untuk masalah Cold-Start.

    Evaluasi & Benchmarking: Menguji model baseline menggunakan data test set dengan metrik evaluasi seperti RMSE (Root Mean Squared Error) untuk prediksi rating. Angka error dari model ini menjadi target minimum yang harus dikalahkan oleh model Deep Learning di hari berikutnya.

> `Hari ke-4: Implementasi Deep Learning (Neural Collaborative Filtering)`
    Implementasi Arsitektur NCF: Membangun model Neural Collaborative Filtering (NCF) yang menggabungkan kekuatan Generalized Matrix Factorization (GMF) dan Multi-Layer Perceptron (MLP) dalam satu jaringan saraf tiruan (Neural Network).

    Menangkap Hubungan Non-Linear: Berbeda dengan model baseline (seperti Cosine Similarity atau SVD tradisional) yang hanya mengandalkan interaksi linier, NCF menggunakan lapisan embedding dan hidden layers untuk mempelajari pola interaksi non-linear yang jauh lebih kompleks antara pengguna dan item.