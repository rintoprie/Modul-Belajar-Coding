## Membuat Virtual Environment untuk Python di Linux dan MacOS

Saat membuat aplikasi menggunakan bahasa pemrograman Python kita kadang membutuhkan beberapa library yang harus di-install atau download lebih dahulu. Kadang dalam komputer yang sama terdapat beberapa aplikasi Python yang membutuhkan library yang sama dengan versi yang berbeda. Dengan membuat virtual environment untuk setiap project kita bisa menginstall library hanya untuk project itu saja sehingga tidak mengganggu project lain yang membutuhkan versi berbeda.  
  
Cara membuat virtual environment untuk project Python berikut ini diambil dari situs resmi Python yang bisa dilihat versi aslinya [di sini](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/). Sebelum menjalankan langkah-langkah di bawah ini pastikan Python dan Pip telah ter-install. Perintah-perintah yang digunakan di bawah ini adalah untuk sistem operasi Linux dan MacOS.  
  
Untuk membuat virtual environment, buka console/terminal, pindah ke direktori project dan jalankan perintah **venv** diikuti dengan nama folder yang akan digunakan untuk menyimpan file-file library yang akan di-install. Nama foldernya bebas. Dalam contoh di bawah ini nama foldernya adalah **env**.  
```
python3 -m venv env
```
Sebelum dapat digunakan untuk meng-install library sebelumnya virtual environment yang sudah dibuat harus diaktifkan dulu seperti contoh di bawah ini.
```
source env/bin/activate
```
Untuk memastikan sudah berada di dalam virtual environment adalah dengan mengecek lokasi interpreter Python dengan perintah which yang akan menampilkan lokasi interpreter Python di dalam direktori env atau virtual environment yang sudah dibuat
```
which python
```
Untuk berpindah ke project lain atau menonaktifkan virtual environment adalah dengan menjalankan perintah di bawah ini.
```
deactivate
```
Setelah berada di dalam virtual environment silakan meng-install library menggunakan perintah pip.
```
pip install requests
```
