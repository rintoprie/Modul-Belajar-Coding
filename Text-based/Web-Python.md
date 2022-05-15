# Membuat website dengan Python

Membuat website dengan Python bisa dilakukan dengan mudah menggunakan library **Flask** atau **Django**

## Menggunakan Flask
Instalasi Flask: 
```
pip install Flask  
```
Contoh kode (hello.py)
```
from flask import Flask  

app = Flask(__name__)  

@app.route("/")  
def hello():  
    return "Hello World!"  

if __name__ == "__main__":  
    app.run()  
```
Jalankan server dengan perintah: 
```
python hello.py  
```
Buka http://localhost:5000/ di browser anda dan akan muncul **Hello World!**

Silakan pilih salah satu tutorial berikut ini untuk memulai:
- https://belajarpython.com/tutorial/pengembangan-web-python
- https://ngodingdata.com/tutorial-flask-web-framework-python/
- https://kelasprogrammer.com/membuat-aplikasi-web-di-python-dengan-flask/

## Menggunakan Django

*TBD*
