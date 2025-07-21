# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju




## Business Understanding

Jaya Jaya Maju merupakan salah satu perusahaan multinasional yang telah berdiri sejak tahun 2000. Ia memiliki lebih dari 1000 karyawan yang tersebar di seluruh penjuru negeri. 

Walaupun telah menjadi menjadi perusahaan yang cukup besar, Jaya Jaya Maju masih cukup kesulitan dalam mengelola karyawan. Hal ini berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%.

Untuk mencegah hal ini semakin parah, manajer departemen HR ingin meminta bantuan Anda mengidentifikasi berbagai faktor yang mempengaruhi tingginya attrition rate tersebut. Selain itu, ia juga meminta Anda untuk membuat business dashboard untuk membantunya memonitori berbagai faktor tersebut.

### Permasalahan Bisnis

Tingginya attrition rate yang melebihi 10% sehingga memberikan dampak negatif bagi perusahaan, seperti  gangguan pada produktivitas.

### Cakupan Proyek

- Analisis dan Prediksi Employee Attrition dengan model Machine Learning
- Pembuatan Dashboard di Metabase
- Automasi Prediksi dari File CSV

### Persiapan

Sumber data: https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/refs/heads/main/employee/employee_data.csv'

Setup environment:


```
## Setup Environment - Anaconda
```
conda create --name ds-project python=3.9
conda activate ds-project
pip install -r requirements.txt

```

## Setup Environment - Shell/Terminal
```
mkdir ds-project
cd ds-project
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Setup Metabase
```
docker run -d -p 3000:3000 --name metabase1 metabase/metabase

email = 'root@mail.com'
password = 'root123'
```

```

## Business Dashboard

Attrition Rate Total:

16.92% ➔ termasuk cukup tinggi. 

Attrition Tertinggi Berdasarkan Department:

Sales → attrition rate paling tinggi.

Attrition Berdasarkan Age Group:

Usia 25–35 tahun dan <25 tahun punya jumlah resign paling banyak.

Biasanya ini usia early-career, mencari peluang karier baru.

Marital Status:

Single memiliki angka resign lebih tinggi dibanding Married atau Divorced.

Years at Company:

Attrition tinggi di tahun-tahun awal (0–5 tahun kerja).

Setelah lebih dari 10 tahun, attrition stabil rendah.

Job Role:

Sales Representative dan Laboratory Technician paling banyak resign.

Top Faktor Penyebab Attrition:

Work Life Balance buruk.

Overtime tinggi.

Job Satisfaction rendah.


## Conclusion

- Attrition rate tinggi 16.92%
Perusahaan menghadapi tingkat attrisi yang cukup tinggi dengan 179 karyawan keluar dari total 1.058 karyawan, melebihi ambang batas ideal (umumnya di bawah 10%). Ini menunjukkan adanya tantangan serius dalam retensi karyawan.

- Departemen dengan Tingkat Attrisi Tertinggi
Sales memiliki attrisi rate tertinggi dibanding departemen lain, disusul oleh Human Resources dan R&D.

Meskipun R&D memiliki jumlah karyawan terbanyak, Sales menunjukkan proporsi pengunduran diri yang jauh lebih tinggi.

- Lama Bekerja Tidak Berbanding Lurus dengan Loyalitas
Mayoritas pengunduran diri terjadi pada karyawan dengan masa kerja kurang dari 5 tahun, menunjukkan kemungkinan masalah dalam proses onboarding, pelatihan, atau kepuasan awal.

### Rekomendasi Action Items (Optional)

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- Perbaiki Work-Life Balance
- Kurangi Overtime
- Lakukan survei mendalam pada kelompok usia 25–35 tahun dan posisi Sales untuk mengetahui akar masalah.

